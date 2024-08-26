# -*- coding: utf-8 -*-
{
    'name': "INHERIT CRM",

    'summary': """
        Menambahkan field Pelanggan baru, Segment pelanggan, dan segment product
        Menambahkan tab Task Progress
        Menambahkan Master data Segment Product""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/segment_product_views.xml',
        'views/templates.xml',
        'data/segment_product_data.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
