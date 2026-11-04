from odoo import models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def do_print_picking(self):
        """Print Store Issue Voucher instead of Picking Operations."""
        self.write({'printed': True})
        return self.env.ref(
            'internal_transfer.action_report_store_issue_voucher'
        ).report_action(self)
