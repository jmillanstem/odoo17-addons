# -*- coding: utf-8 -*-
# © 2024 Jaime Millán <jmillan@stemdo.io>

{
    'name': 'Custom Invoice',
    'version': '1.0',
    'summary': 'Customized Invoice Template with Additional Information and Styles',
    'description': 'A module to customize the invoice template in Odoo 17, adding extra information and styles.',
    'author': 'Jaime Millán',
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'views/custom_invoice_view.xml',
        'report/custom_invoice_template.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_invoice/static/src/css/custom_invoice_styles.css',
        ],
    },
    'installable': True,
    'application': False,
}
