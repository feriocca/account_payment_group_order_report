# -*- coding: utf-8 -*-
{
    'name': "account_payment_group_order_report",

    'summary': """
        Payment Group Order Report""",

    'description': """
        A report to print a pdf report showing a payment group order detailed
    """,

    'author': "fernando iocca",
    'email': "feriocca@gmail.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Invoicing &amp; Payments',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_payment_group'],

    # always loaded
    'data': [
        'report/report_payment_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}