# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    "name": "Real Estate",
    "version": "1.8",
    # "category": "Tutorial",
    "sunmmary": "Real Estate Management Module",
    "depends": ["base"],
    "data": [
        # "views/mymodule_view.xml",
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_menus.xml",
    ],
    # data files containing optionally loaded demonstration data
    "demo": [
        # "demo/demo_data.xml",
    ],
    # "installable": True,
    "application": True,
    # "module_type": "official",
    "license": "LGPL-3",
}
