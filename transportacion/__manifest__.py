# -*- coding: utf-8 -*-
{
    'name': "App Transportacion",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Onily Valera | Lorenzo Peña",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Mitur/Transportacion',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','hr'],
    'installable': True,
    'application': True,
    'auto_install': False,
    # always loaded
    'data': [
        'views/transportacion_menu.xml',
        'views/trip_view.xml',
        'views/vehicle_view.xml',
        'security/transportacion_security.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}