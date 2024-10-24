from collections import defaultdict
from odoo import models, fields, api, exceptions
from odoo.tools.float_utils import float_compare


class EditorialLiquidacion(models.Model):
    """ Modelo de liquidación que extiende de account.move """

    # https://github.com/OCA/OCB/blob/13.0/addons/account/models/account_move.py
    _description = "Liquidacion Descontrol"
    _inherit = ['account.move']

    @api.model
    def default_get(self, fields):
        res = super(EditorialLiquidacion, self).default_get(fields)
        
        if 'journal_id' in fields and res['is_liquidacion']:
            if res['type'] == 'in_refund':
                journal = self.env.company.account_journal_deposito_compra_id
                res['journal_id'] = journal.id
            elif res['type'] == 'out_refund':
                journal = self.env['account.journal'].search([('code', '=', 'LIQ')], limit=1)
                res['journal_id'] = journal.id
        return res
    
    @api.model
    def _get_default_is_liquidacion(self):
        if self._context.get('invoice_type') and self._context['invoice_type'] == 'LIQ':
            return True
        else:
            return False
        
    is_liquidacion = fields.Boolean(
        "Es liquidacion", default=_get_default_is_liquidacion
    )

    @api.onchange('partner_id')
    def _set_partner_purchase_liq_pricelist(self):
        if self.type == 'in_invoice' and self.is_liquidacion and self.partner_id.purchase_liq_pricelist.id:
            self.pricelist_id = self.partner_id.purchase_liq_pricelist

    def action_post(self):
        if self.is_liquidacion and self.type == 'in_invoice':
            if not self.pricelist_id:
                raise exceptions.ValidationError(
                    "Es obligatorio seleccionar una tarifa.\nRecuerda aplicarla haciendo click en el botón \"Aplicar tarifa\"."
                )
        return super().action_post()
    
    # When using the button for create "Factura rectificativa" set is_liquidation = False
    def action_switch_invoice_into_refund_credit_note(self):
        self.is_liquidacion = False
        return super().action_switch_invoice_into_refund_credit_note()

    def checkLiquidacionIsValid(self, liquidacion, deposito_lines):
        products_to_check = defaultdict(lambda: {'total_liquidacion': 0, 'total_deposito': 0})

        for invoice_line in liquidacion.invoice_line_ids:
            products_to_check[invoice_line.product_id]['total_liquidacion'] += invoice_line.quantity
            deposito_lines_to_check = deposito_lines.filtered(
                lambda deposito_line: deposito_line.product_id
                == invoice_line.product_id
            )
            if deposito_lines_to_check:
                if self.type == 'out_invoice' or self.type == 'out_refund':
                    qty_total_deposito = sum(p.product_uom_qty - p.qty_done for p in deposito_lines_to_check)
                elif self.type == 'in_invoice':
                    qty_total_deposito = sum(p.qty_received - p.liquidated_qty for p in deposito_lines_to_check)
                elif self.type == 'in_refund':
                    invoice_line.product_id._compute_on_hand_qty()
                    stock = invoice_line.product_id.on_hand_qty
                    qty_total_deposito = min(sum(p.qty_received - p.liquidated_qty for p in deposito_lines_to_check), stock)

                products_to_check[invoice_line.product_id]['total_deposito'] = qty_total_deposito

        products_not_available = {}
        for product, qty in products_to_check.items():
            if qty['total_liquidacion'] > qty['total_deposito']:
                products_not_available[product.name] = qty['total_deposito']

        if len(products_not_available) > 0:
            msg = "No hay stock suficiente disponible en depósito con estos valores. Estos son valores disponibles en depósito:"
            for product_name, product_qty in products_not_available.items():
                msg += "\n* " + str(product_name) + ": " + str(product_qty)
            raise exceptions.UserError(msg)

    def get_deposito_lines(self, alphabetical_order=False):
        domain = []
        deposito_lines = []

        if self.type == 'out_invoice' or self.type == 'out_refund':
            domain = [
                ('owner_id', '=', self.partner_id.id),
                ('location_id', '=', self.env.company.location_venta_deposito_id.id),
                ('location_dest_id', '=', self.env.ref("stock.stock_location_customers").id),
                ('state', 'in', ('assigned', 'partially_available')),
            ]
            order_clause = 'product_id asc' if alphabetical_order else 'date asc'
            deposito_lines = self.env['stock.move.line'].search(domain, order=order_clause)

        elif self.type == 'in_invoice' or self.type == 'in_refund':
            domain = [
                    ('partner_id', '=', self.partner_id.id),
                    ('state', 'in', ['purchase', 'done']),
                    ('is_liquidated', '=', False),
                    ('order_id.picking_type_id', '=', self.env.company.stock_picking_type_compra_deposito_id.id)
                ]
            order_clause = 'name asc' if alphabetical_order else 'date_planned asc'
            deposito_lines = self.env['purchase.order.line'].search(domain, order=order_clause)

        return deposito_lines

    def get_invoice_lines_sum_quantity_by_product(self):
         # group invoice line by product and sum quantities
        totals = defaultdict(int)
        for invoice_line in self.invoice_line_ids:
            totals[invoice_line.product_id] += invoice_line.quantity
        return totals.items()

    def liquidate_deposito_ventas(self, deposito_lines):

        pickings_to_validate = set()
        invoice_product_qty_data = self.get_invoice_lines_sum_quantity_by_product()

        for product_id, quantity in invoice_product_qty_data:
            invoice_line_qty = quantity
            pendientes_liquidar_stock_lines = deposito_lines.filtered(
                lambda deposito_line: deposito_line.product_id
                == product_id
            )
            if (not pendientes_liquidar_stock_lines or len(pendientes_liquidar_stock_lines) <= 0):
                raise exceptions.ValidationError(
                    "No hay stock suficiente disponible en depósito con estos valores a liquidar. Intenta volver a comprobar el depósito"
                )
            for pendiente_stock_line in pendientes_liquidar_stock_lines:
                if invoice_line_qty > 0:
                    stock_line_reserved_qty = pendiente_stock_line.product_uom_qty
                    stock_line_done_qty = pendiente_stock_line.qty_done
                    qty_difference = invoice_line_qty - (
                        stock_line_reserved_qty - stock_line_done_qty
                    )
                    if (qty_difference >= 0):  # if the invoice_qty is greater (or equal) than the available stock_qty, we close the stock_line and continue
                        pendiente_stock_line.write(
                            {'qty_done': stock_line_reserved_qty}
                        )
                    else:
                        pendiente_stock_line.write(
                            {'qty_done': stock_line_done_qty + invoice_line_qty}
                        )
                    picking = pendiente_stock_line.picking_id
                    pickings_to_validate.add(picking)
                    invoice_line_qty = qty_difference
                else:
                    break
        # Here we validate all the pickings at once:
        for picking in pickings_to_validate:
            picking.button_validate()
            # Create backorder if necessary, because the button_validate()
            # method doesn't do it for us automaticly
            if picking._check_backorder():
                moves_to_log = {}
                for move in picking.move_lines:
                    if (
                        float_compare(
                            move.product_uom_qty,
                            move.quantity_done,
                            precision_rounding=move.product_uom.rounding,
                        )
                        > 0
                    ):
                        moves_to_log[move] = (move.quantity_done, move.product_uom_qty)
                picking._log_less_quantities_than_expected(moves_to_log)
                picking.with_context(cancel_backorder=False).action_done()

    def liquidate_deposito_compras(self, deposito_lines):

        invoice_product_qty_data = self.get_invoice_lines_sum_quantity_by_product()

        for product_id, quantity in invoice_product_qty_data:
            invoice_line_qty = quantity
            pendientes_liquidar_purchase_lines = deposito_lines.filtered(
                lambda deposito_line: deposito_line.product_id
                == product_id
            )
            if (not pendientes_liquidar_purchase_lines or len(pendientes_liquidar_purchase_lines) <= 0):
                raise exceptions.ValidationError(
                    "No hay stock suficiente disponible en depósito con estos valores a liquidar. Intenta volver a comprobar el depósito"
                )
            for purchase_line in pendientes_liquidar_purchase_lines:
                if invoice_line_qty > 0:
                    qty_to_liquidate = purchase_line.qty_received - purchase_line.liquidated_qty
                    if invoice_line_qty >= qty_to_liquidate:
                        purchase_line.write(
                            {'liquidated_qty': purchase_line.liquidated_qty + qty_to_liquidate}
                        )
                        invoice_line_qty -= qty_to_liquidate
                    else:
                        purchase_line.write(
                            {'liquidated_qty': purchase_line.liquidated_qty + invoice_line_qty}
                        )
                        invoice_line_qty = 0

    def devolver_deposito_ventas(self, deposito_lines):
        odoo_env = self.env
        pickings_to_assign = set()
        pickings_return = (
            {}
        )  # relation between done_picking (key) and the created_return (value)

        invoice_product_qty_data = self.get_invoice_lines_sum_quantity_by_product()

        for product_id, quantity in invoice_product_qty_data:
            liquidacion_line_qty = quantity
            if liquidacion_line_qty > 0.0:
                pendientes_cerrar_stock_lines = deposito_lines.filtered(
                    lambda deposito_line: deposito_line.product_id == product_id)
                if not pendientes_cerrar_stock_lines:
                    raise exceptions.ValidationError(
                        "No hay stock suficiente disponible en depósito para devolver. Intenta volver a comprobar el depósito"
                    )
                for pendiente_stock_line in pendientes_cerrar_stock_lines:
                    if liquidacion_line_qty <= 0:
                        break
                    stock_line_reserved_qty = pendiente_stock_line.product_uom_qty
                    stock_line_done_qty = pendiente_stock_line.qty_done
                    qty_deposito = stock_line_reserved_qty - stock_line_done_qty
                    qty_difference = liquidacion_line_qty - qty_deposito
                    # if the liquidacion_qty is greater (or equal) than the available qty_deposito,
                    # we look for the associated stock.picking that enabled the current move.line de depósito,
                    # and then we return an amount of qty_deposito of the product_id on the associated stock.picking

                    associated_done_picking = (
                        pendiente_stock_line.picking_id.sale_id.picking_ids.filtered(
                            lambda picking: picking.location_id.id == self.env.ref("stock.stock_location_stock").id
                            and picking.location_dest_id.id == self.env.company.location_venta_deposito_id.id
                            and picking.state == 'done'
                            and product_id.id in [li.product_id.id for li in picking.move_line_ids_without_package]
                        )
                    )
                    if len(associated_done_picking) > 1:
                        associated_done_picking = associated_done_picking[0]
                    elif len(associated_done_picking) <= 0:
                        continue

                    pickings_to_assign.add(
                        pendiente_stock_line.picking_id
                    )  # associated deposito picking

                    # Check if we have already created a return for this done_picking
                    if associated_done_picking not in pickings_return:
                        # New Wizard to make the return of one line
                        return_picking = odoo_env['stock.return.picking'].create(
                            {'picking_id': associated_done_picking.id}
                        )
                        pickings_return[associated_done_picking] = return_picking
                        return_picking._onchange_picking_id()  # what does this do?
                    return_picking = pickings_return.get(associated_done_picking)
                    # Correct the lines with negative prohibited values
                    for line in return_picking.product_return_moves:
                        if line.quantity < 0:
                            line.write({'quantity': 0})

                    return_picking_line = return_picking.product_return_moves.filtered(
                        lambda line: line.product_id == product_id
                    )
                    return_qty = (
                        qty_deposito if qty_difference >= 0 else liquidacion_line_qty
                    )
                    get_qty = return_picking_line.quantity
                    return_picking_line.write(
                        {'quantity': get_qty + return_qty}
                    )  # we add to the existing value
                    liquidacion_line_qty = qty_difference
        for return_picking in pickings_return.values():

            new_stock_picking_data = return_picking.create_returns()
            new_stock_picking = odoo_env['stock.picking'].browse(
                new_stock_picking_data['res_id']
            )
            for line in new_stock_picking.move_ids_without_package:
                line.write({'quantity_done': line.product_uom_qty})
            new_stock_picking.button_validate()
        for picking in pickings_to_assign:
            # Check availavility to load again the stock.move.lines after the return
            picking.action_assign()

    def devolver_deposito_compras(self, deposito_lines):
        odoo_env = self.env
        pickings_return = {}    # relation between done_picking (key) and the created_return (value)

        invoice_product_qty_data = self.get_invoice_lines_sum_quantity_by_product()

        for product_id, quantity in invoice_product_qty_data:
            liquidacion_line_qty = quantity
            if liquidacion_line_qty > 0.0:
                pendientes_cerrar_purchase_lines = deposito_lines.filtered(
                    lambda deposito_line: deposito_line.product_id == product_id)
                if not pendientes_cerrar_purchase_lines:
                    raise exceptions.ValidationError(
                        "No hay stock suficiente disponible en depósito para devolver. Intenta volver a comprobar el depósito"
                    )
                for pendiente_purchase_line in pendientes_cerrar_purchase_lines:
                    if liquidacion_line_qty <= 0:
                        break
                    qty_deposito = pendiente_purchase_line.qty_received - pendiente_purchase_line.liquidated_qty
                    qty_difference = liquidacion_line_qty - qty_deposito

                    associated_done_picking = (
                        pendiente_purchase_line.order_id.picking_ids.filtered(
                            lambda picking: (
                            picking.picking_type_id.id == self.env.company.stock_picking_type_compra_deposito_id.id
                            and picking.state == 'done'
                            and product_id.id in [li.product_id.id for li in picking.move_line_ids_without_package]
                            )
                        )
                    )
                    if len(associated_done_picking) > 1:
                        associated_done_picking = associated_done_picking[0]
                    elif len(associated_done_picking) <= 0:
                        continue

                    # Check if we have already created a return for this done_picking
                    if associated_done_picking not in pickings_return:
                        # New Wizard to make the return of one line
                        return_picking = odoo_env['stock.return.picking'].create(
                            {'picking_id': associated_done_picking.id}
                        )
                        pickings_return[associated_done_picking] = return_picking
                        return_picking._onchange_picking_id()  # what does this do?
                        for line in return_picking.product_return_moves:
                            line.write({'quantity': 0})
                    return_picking = pickings_return.get(associated_done_picking)

                    return_picking_line = return_picking.product_return_moves.filtered(
                        lambda line: line.product_id == product_id
                    )
                    return_qty = qty_deposito if qty_difference >= 0 else liquidacion_line_qty
                    return_picking_line.write(
                        {'quantity': return_picking_line.quantity + return_qty}
                    )
                    liquidacion_line_qty = qty_difference
        
        for return_picking in pickings_return.values():
            new_stock_picking_data = return_picking.create_returns()
            new_stock_picking = odoo_env['stock.picking'].browse(
                new_stock_picking_data['res_id']
            )
            for line in new_stock_picking.move_ids_without_package:
                line.write({'quantity_done': line.product_uom_qty})
            new_stock_picking.button_validate()

    def post_y_liquidar(self):
        if not self.is_liquidacion:
            raise exceptions.ValidationError(
                "Sólo se puede liquidar desde una factura tipo liquidación"
            )

        if not self.pricelist_id and self.type == 'in_invoice':
            raise exceptions.ValidationError(
                "Es obligatorio seleccionar una tarifa.\nRecuerda aplicarla haciendo click en el botón \"Aplicar tarifa\"."
            )

        deposito_lines = self.get_deposito_lines()   
        self.checkLiquidacionIsValid(self, deposito_lines)

        if self.type == 'out_invoice':
            self.liquidate_deposito_ventas(deposito_lines)
        elif self.type == 'in_invoice':
            self.liquidate_deposito_compras(deposito_lines)

        self.action_post()

    def post_y_devolver(self):
        if not self.is_liquidacion:
            raise exceptions.ValidationError(
                "Sólo se puede devolver depósito desde una factura tipo devolución depósito"
            )
        deposito_lines = self.get_deposito_lines()
        self.checkLiquidacionIsValid(self, deposito_lines)
        
        if self.type == 'out_refund':
            self.devolver_deposito_ventas(deposito_lines)
        elif self.type == 'in_refund':
            self.devolver_deposito_compras(deposito_lines)

        self.action_post()


class EditorialAccountMoveLine(models.Model):
    """ Extend account.move.line template for editorial management """

    _description = "Editorial Account Move Line"
    _inherit = 'account.move.line'  # odoo/addons/account/models/account_move.py

    product_barcode = fields.Char(
        string="Código de barras / ISBN", related='product_id.barcode', readonly=True
    )
