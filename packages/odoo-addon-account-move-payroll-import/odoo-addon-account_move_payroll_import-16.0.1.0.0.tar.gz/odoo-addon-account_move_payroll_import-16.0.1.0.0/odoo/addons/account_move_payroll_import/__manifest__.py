# -*- coding: utf-8 -*-
# Copyright 2024-SomItCoop SCCL(<https://gitlab.com/somitcoop>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
{
    "name": "SomItCoop ODOO accounting spanish payroll import",
    "version": "16.0.1.0.0",
    "depends": ["account", "hr", "web", "l10n_es"],
    "author": """
        Som It Cooperatiu SCCL,
        Som Connexió SCCL
    """,
    "category": "Accounting & Finance",
    "website": "https://gitlab.com/somitcoop/erp-research/odoo-accounting",
    "license": "AGPL-3",
    "summary": """
        ODOO account move spanish payroll data import for social cooperatives.
    """,
    "description": """
        This module provides an import wizard to create account moves
        and its corresponding lines from spanish payroll data in *.csv/*.xlsx
        uploaded files.
    """,
    "data": [
        "security/ir.model.access.csv",
        "data/payroll_import_defaults.xml",
        "views/assets_template.xml",
        "views/payroll_import_views.xml",
        "wizards/payroll_import_wizard.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "account_move_payroll_import/static/src/*/**.js",
            "account_move_payroll_import/static/src/*/**.css",
            "account_move_payroll_import/static/src/*/**.xml",
        ],
    },
    "application": False,
    "installable": True,
}
