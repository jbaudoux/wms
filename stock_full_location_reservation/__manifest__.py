# Copyright 2023 Michael Tietz (MT Software) <mtietz@mt-software.de>
# Copyright 2023 Jacques-Etienne Baudoux (BCIM) <je@bcim.be>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl)
{
    "name": "Stock full location reservation",
    "summary": "Extend reservation to full content of location",
    "author": "MT Software, BCIM, Odoo Community Association (OCA)",
    "website": "https://github.com/OCA/wms",
    "category": "Warehouse Management",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "depends": ["stock"],
    "data": [
        "security/groups.xml",
        "views/stock_picking_views.xml",
        "views/stock_picking_type_views.xml",
    ],
    "application": False,
    "installable": True,
}
