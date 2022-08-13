# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Variant process bar on website',
    'version' : '1.1',
    'summary': 'Variant process bar on website',
    'sequence': 10,
    'description': """ Select multiple products variant for product. """,
    'category': 'Ecommerce',
    'author': 'Odolution',
    'license': 'LGPL-3',
    'price': 10.00,
    'currency': "USD",
    'images' : [],
    'depends' : ['website','website_sale'],
    'data': [
        
        'views/variant_selection_bar.xml',
        
    ],

    'assets': {
        'web.assets_frontend': [
            'customize_variant_steps/static/src/css/style_variants.css',
            'customize_variant_steps/static/src/js/main_mixin.js',
        ],
        #'web.assets_qweb': ['customize_variant_steps/static/src/xml/variant_selection_bar.xml'],
        },           
    'demo': [],
    'images': ['static/description/background.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
