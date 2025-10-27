# -*- coding: utf-8 -*-
{
    'name': "Indonesia",

    'summary': """Data Indonesia""",

    'description': """Data Indonesia""",

    'author': "Isa Mujahid Islam",
    'website': "https://isa.web.id",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'data/idn.provinsi.csv',
        'data/idn.kabupaten_kota.csv',
        'data/idn.kecamatan.csv',
        'views/menu.xml',
        'views/provinsi.xml',
        'views/kabupaten_kota.xml',
        'views/kecamatan.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
