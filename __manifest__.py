{
    'name': 'Meter Reading Invoice',
    'version': '18.0.2.0.0',
    'category': 'Accounting',
    'summary': 'Adds meter readings to customer invoices',
    'license': 'LGPL-3',

    'depends': [
        'account',
    ],

    'data': [
        'views/account_move_views.xml',
        'views/account_report.xml',
    ],

    'installable': True,
    'application': False,
}
