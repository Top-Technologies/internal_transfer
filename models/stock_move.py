from odoo import api, fields, models


class StockMove(models.Model):
    _inherit = 'stock.move'

    sales_price = fields.Float(
        string='Sales Price',
        related='product_id.list_price',
        readonly=True,
        digits='Product Price',
    )
    cost = fields.Float(
        string='Cost',
        compute='_compute_cost',
        digits='Product Price',
    )

    @api.depends('product_uom_qty', 'product_id', 'product_id.list_price')
    def _compute_cost(self):
        for move in self:
            move.cost = move.product_uom_qty * (move.product_id.list_price or 0.0)
