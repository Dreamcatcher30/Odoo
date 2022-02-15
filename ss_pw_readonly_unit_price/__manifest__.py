# -*- coding: utf-8 -*-

{
    'name': 'IDS Price Unit Readonly, Sale and Invoice Unit Price Readonly',
    'category': 'Sale',
    'summary': 'This module will help you to sales and invoice unit price readonly for specific user.',
    'version': '13.0',
    'author': 'Sourav Sinha',
    'description': """Readonly unit price for specific users : 
- Invoice unit price readonly
- Sale order unit price readonly
- Invoice unit price readonly for specific user
- Sale order unit price readonly for specific user
    """,
    'depends': ['account', 'sale_management'],
    'data': [
        'security/sale_invoice_security.xml',
        'views/sale_invoice_view.xml',
    ],
    'price': 100.0,
    'currency': "EUR",
    'application': True,
    'installable': True,
    'images': ["static/description/Banner.png"],
}
