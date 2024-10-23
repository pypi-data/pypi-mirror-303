# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PayrollCustomConcept(models.Model):
    _name = "payroll.custom.concept"
    _description = "Payroll Custom Concept"
    _check_company_auto = True

    @api.model
    def create(self, vals):
        default_account_ext_id = "l10n_es.%s_%s" % (
            self.env.company.id, vals.get("default_account_xml_id", False)
        )
        if default_account_ext_id:
            account = self.env.ref(default_account_ext_id, False)
            vals.update({"account_id": account.id if account else False})

        return super(PayrollCustomConcept, self).create(vals)

    def _default_account(self):
        default_account_ext_id = "l10n_es.%s_%s" % (
            self.env.company.id, self.default_account_xml_id
        )
        default_account = self.env.ref(default_account_ext_id, False)
        return default_account.id if default_account else False

    name = fields.Char(
        string="Tag",
        required=True,
        help=_("Indicate the name of the custom concept.")
    )
    col_index = fields.Integer(
        string="Column Number",
        required=True,
        help=_("Indicate the position in the file.")
    )
    account_id = fields.Many2one(
        comodel_name="account.account",
        string="Account",
        required=True,
        help=_("Indicate the account to post the data.")
    )
    default_account_xml_id = fields.Char("Default Account XML ID")
    payroll_import_setup_id = fields.Many2one(
        comodel_name="payroll.import.setup",
        string="Payroll Import Setup",
        required=True,
        ondelete="cascade",
    )
    company_id = fields.Many2one(
        related="payroll_import_setup_id.company_id",
        string="Company",
        store=True,
        readonly=True,
    )
