{
    'name': 'Internal Transfer Cost & Store Issue Voucher',
    'version': '18.0.1.1.0',
    'category': 'Inventory',
    'summary': 'Show product cost on internal transfer lines and print Store Issue Voucher',
    'description': """
        - Adds a Cost column on stock picking Operations (Demand × Sales Price)
        - Print button opens an English Store Issue Voucher matching the paper form
    """,
    'author': 'TopTech',
    'depends': ['stock'],
    'data': [
        'report/store_issue_voucher_report.xml',
        'report/store_issue_voucher_template.xml',
        'report/report_deliveryslip_inherit.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
