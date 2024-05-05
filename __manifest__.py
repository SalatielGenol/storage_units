# -*- coding: utf-8 -*-
{
    'name': "Storage Units Management",

    'summary': """
        Simple module to manage storage units. 
        """,

    'description': """
        Module that allows you to add storage units in
        different locations, and keep them organized by
        creating spaces (shelves, delimited zones,
        refrigerators) where the objects to be stored
        are registered.
    """,

    'author': "Salatiel Genol",
    'website': "https://github.com/SalatielGenol/storage_units",
    'license': "GPL-3 or any later version",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Inventory',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml'
    ],
}
