# Copyright 2023 Michael Tietz (MT Software) <mtietz@mt-software.de>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Shopfloor full location reservation",
    "summary": "Shopfloor full location reservation",
    "author": "MT Software, BCIM, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/wms",
    "category": "Warehouse Management",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "data": [
        "views/shopfloor_menu.xml",
    ],
    "depends": [
        "shopfloor",
        "stock_full_location_reservation",
    ],
    "auto_install": True,
    "post_init_hook": "post_init_hook",
}
