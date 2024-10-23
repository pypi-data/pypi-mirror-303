# -*- coding: utf-8 -*-

from odoo import models, fields, _, Command
from odoo.exceptions import UserError

from ..utils.parse_utils import abs_float


# This are the only allowed mappings for the moment
ALLOWED_MAPPINGS = [
    "payroll_import_mapping_gross",
    "payroll_import_mapping_net",
    "payroll_import_mapping_total_tc1rlc",
    "payroll_import_mapping_irpf_employee",
    "payroll_import_mapping_ss_company",
    "payroll_import_mapping_discounts",
    "payroll_import_mapping_embargoes",
    "payroll_import_mapping_ss_bonus",
]


class PayrollImportSetup(models.Model):
    _name = "payroll.import.setup"
    _description = "Payroll Import Setup"
    _check_company_auto = True

    NUMBER_DELIMITERS = [
        (".", _("Dot (.)")),
        (",", _("Comma (,)")),
        ("", _("None")),
    ]

    ALL_DELIMITERS = [
        (".", _("Dot (.)")),
        (",", _("Comma (,)")),
        (";", _("Semicolon (;)")),
        ("\t", _("Tabulation")),
        ("&nbsp;", _("Space")),
    ]

    ENCODINGS = [
        ("utf-8", "UTF-8"),
        ("latin1", "Latin1"),
        ("ascii", "ASCII"),
    ]

    def _default_import_mappings(self):
        """
        This version only allows the default mappings in payroll_import_defaults.xml
        """
        return [
            Command.link(self.env.ref("account_move_payroll_import.%s" % xml_id).id)
            for xml_id in ALLOWED_MAPPINGS
        ]

    def _default_custom_concepts(self):
        return [
            Command.create(
                {
                    "name": "FUNDAE",
                    "col_index": 13,
                    "default_account_xml_id": "account_common_642",
                }
            ),
            Command.create(
                {
                    "name": "AN TANDEM",
                    "col_index": 15,
                    "default_account_xml_id": "account_common_640",
                }
            ),
            Command.create(
                {
                    "name": "RET FLEXIB",
                    "col_index": 16,
                    "default_account_xml_id": "account_common_642",
                }
            ),
        ]

    name = fields.Char(
        string="Name",
        default=_("Payroll Import A3 2024"),
        help=_("Indicate a name describing the payroll file."),
    )
    thousands_delimiter = fields.Selection(
        selection=NUMBER_DELIMITERS, string="Thousands Separator", default=","
    )
    decimal_delimiter = fields.Selection(
        selection=NUMBER_DELIMITERS, string="Decimal Separator", default="."
    )
    encoding = fields.Selection(selection=ENCODINGS, string="Encoding", default="utf-8")
    delimiter = fields.Selection(
        selection=ALL_DELIMITERS, string="Column Separator", default=";"
    )
    header_lines = fields.Integer(
        string="Header Lines",
        default=9,
        help=_("Specify the number of header lines in the file."),
    )
    header_ref_line = fields.Integer(
        string="Header Reference (Tag) Line",
        default=4,
        help=_("Specify in case of a header line with the account move reference."),
    )
    journal_id = fields.Many2one(
        string="Journal",
        comodel_name="account.journal",
        help=_("Indicate the journal where data will be posted."),
    )
    column_employee_id = fields.Integer(
        string="Employee ID Column Number",
        required=True,
        default=2,
        help=_("Indicate the column number with employee reference."),
    )
    column_gross = fields.Integer(
        string="Gross Salary Column Number",
        required=True,
        default=4,
        help=_("Indicate the column number with gross salary in the file."),
    )
    gross_account_id = fields.Many2one(
        string="Gross Salary Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_640" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    gross_tax_id = fields.Many2one(
        string="Gross Salary Tax",
        comodel_name="account.tax",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_tax_template_p_irpf21td" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the tax to be applied to the data."),
    )
    gross_to_single_line = fields.Boolean(
        string="Gross Single Move Line",
        default=True,
        help=_("Aggregate amounts in a single move line if True."),
    )
    column_net = fields.Integer(
        string="Net Salary Column Number",
        required=True,
        default=5,
        help=_("Indicate the column number with net salary in the file."),
    )
    net_account_id = fields.Many2one(
        string="Net Salary Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_465" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    column_total_tc1rlc = fields.Integer(
        string="Total TC1RLC Column Number",
        required=True,
        default=7,
        help=_("SS quotes from all employees."),
    )
    total_tc1rlc_account_id = fields.Many2one(
        string="Total TC1RLC Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_476" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    total_tc1rlc_to_single_line = fields.Boolean(
        string="Total TC1RLC Single Move Line",
        default=True,
        help=_("Aggregate amounts in a single move line if True."),
    )
    column_irpf_employee = fields.Integer(
        string="IRPF Employee Column Number",
        required=True,
        default=8,
        help=_("Indicate the column number with IRPF employee in the file."),
    )
    irpf_employee_account_id = fields.Many2one(
        string="IRPF Employee Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_4751" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    irpf_employee_to_single_line = fields.Boolean(
        string="IRPF Single Move Line",
        default=True,
        help=_("Aggregate amounts in a single move line if True."),
    )
    column_ss_employee = fields.Integer(
        string="SS Employee Column Number",
        required=True,
        default=9,
        help=_(
            "Specify the position in the file."
            " This column is used to verify total values of TC1 - SS company."
            " It won't be registered in the account move."
        ),
    )
    column_ss_company = fields.Integer(
        string="SS Company Column Number",
        required=True,
        default=10,
        help=_("Specify the position in the file."),
    )
    ss_company_account_id = fields.Many2one(
        string="SS Company Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_642" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    ss_company_to_single_line = fields.Boolean(
        string="SS Company Single Move Line",
        default=True,
        help=_("Aggregate amounts in a single move line if True."),
    )
    column_discounts = fields.Integer(
        string="Discounts Column Number",
        required=True,
        default=11,
        help=_("Indicate the column number with discounts in the file."),
    )
    discounts_account_id = fields.Many2one(
        string="Discounts Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_460" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    column_embargoes = fields.Integer(
        string="Embargoes Column Number",
        required=True,
        default=12,
        help=_("Indicate the column number with embargoes in the file."),
    )
    embargoes_account_id = fields.Many2one(
        string="Embargoes Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_465" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    column_ss_bonus = fields.Integer(
        string="SS Bonus Column Number",
        required=True,
        default=14,
        help=_("Indicate the column number with SS bonus in the file."),
    )
    ss_bonus_account_id = fields.Many2one(
        string="SS Bonus Account",
        comodel_name="account.account",
        required=True,
        default=lambda self: self.env.ref(
            "l10n_es.%s_account_common_642" % self.env.company.id,
            raise_if_not_found=False,
        ),
        help=_("Indicate the account where data will be posted."),
    )
    custom_concepts_ids = fields.One2many(
        string="Custom Concepts",
        comodel_name="payroll.custom.concept",
        inverse_name="payroll_import_setup_id",
        default=_default_custom_concepts,
    )
    payroll_import_mapping_ids = fields.Many2many(
        string="Payroll Import Mapping",
        comodel_name="payroll.import.mapping",
        default=_default_import_mappings,
    )
    company_id = fields.Many2one(
        string="Company",
        comodel_name="res.company",
        default=lambda self: self.env.company,
    )

    _sql_constraints = [
        (
            "name_company_uniq",
            "unique(name, company_id)",
            _("The name must be unique by company."),
        )
    ]

    def get_file_options(self):
        """
        Get file options in a dictionary formatted as required by
        the base_import.import module method _read_file.
        """
        return {
            "encoding": self.encoding,
            "separator": self.delimiter,
            "float_thousand_separator": self.thousands_delimiter,
            "float_decimal_separator": self.decimal_delimiter,
            "header_lines": self.header_lines,
            "headers": False,
            "quoting": '"',
        }

    def validate_column_numbers(self, data_length):
        for field in [k for k in self._fields.keys() if k.startswith("column_")]:
            if getattr(self, field) > data_length:
                raise UserError(_("Column %s is out of range." % field))

    def compute_tc1rlc_ss_cumulative(self, row, cumulative):
        """
        Calculate the cumulative of TC1RLC - (SS employee + SS company).
        It should be zero once all rows are processed.
        """
        cumulative += (
            abs_float(
                row[self.column_total_tc1rlc - 1],
                self.thousands_delimiter,
                self.decimal_delimiter,
            )
            - abs_float(
                row[self.column_ss_employee - 1],
                self.thousands_delimiter,
                self.decimal_delimiter,
            )
            - abs_float(
                row[self.column_ss_company - 1],
                self.thousands_delimiter,
                self.decimal_delimiter,
            )
        )
        return cumulative

    def _get_partner_id(self, employee_id):
        """
        Get the partner id from the employee id.
        """
        employee = self.env["hr.employee"].search(
            [("identification_id", "=", employee_id)], limit=1
        )
        if not employee:
            raise UserError(
                _("Employee with identification id %s not found." % employee_id)
            )

        partner = employee.address_home_id
        if not partner:
            raise UserError(
                _("Employee %s has no home address (partner)." % employee.name)
            )

        return partner.id

    def _prepare_line_vals(self, row, line_mapping):
        """
        Prepare the line values for the account move line.
        """
        if not line_mapping.res_field:  # skip validation columns
            return {}

        column = getattr(self, line_mapping.column_field, False)
        value = abs_float(
            row[column - 1], self.thousands_delimiter, self.decimal_delimiter
        )

        if not value:
            return {}  # skip lines with no amounts

        vals = {"tax_ids": False, "account_id": False, line_mapping.res_field: value}

        if line_mapping.tax_field and not vals.get("tax_ids"):
            tax_id = getattr(self, line_mapping.tax_field, False)
            vals.update({"tax_ids": [(6, 0, [tax_id.id])] if tax_id else False})

        if line_mapping.account_field and not vals.get("account_id"):
            account_id = getattr(self, line_mapping.account_field, False)
            vals.update({"account_id": account_id.id if account_id else False})

        if (
            line_mapping.column_field == "column_gross"
            and self.gross_to_single_line
            and not vals.get("tax_tag_ids")
        ):
            tax_tag_ids = self.gross_tax_id.get_tax_tags(
                is_refund=False, repartition_type="base"
            ).ids
            vals.update({"tax_tag_ids": [(6, 0, tax_tag_ids)]})

        if (
            line_mapping.column_field == "column_irpf_employee"
            and self.irpf_employee_to_single_line
            and not vals.get("tax_line_id")
        ):
            tax_tag_ids = self.gross_tax_id.get_tax_tags(
                is_refund=False, repartition_type="tax"
            ).ids
            vals.update(
                {
                    "name": self.gross_tax_id.name,
                    "tax_line_id": self.gross_tax_id.id,
                    "display_type": "tax",
                    "tax_tag_ids": [(6, 0, tax_tag_ids)],
                }
            )
        return vals

    def _prepare_custom_concept_vals_list(self, row, partner_id):
        """
        Prepare the line values for the account move lines related
        to custom concepts.
        """
        cc_vals_list = []
        for custom_concept in self.custom_concepts_ids:
            column = custom_concept.col_index
            value = abs_float(
                row[column - 1], self.thousands_delimiter, self.decimal_delimiter
            )

            if not value:
                continue

            cc_vals_list.append(
                {
                    "partner_id": partner_id,
                    "account_id": custom_concept.account_id.id,
                    "name": custom_concept.name,
                    "credit": value,
                }
            )

        return cc_vals_list

    def _create_account_move(self, lines_vals):
        """
        Create the payroll account move.
        """
        move = self.env["account.move"].with_context(
            is_payroll_import=True
        ).create(
            {
                "date": fields.Date.today(),
                "journal_id": self.journal_id.id,
                "line_ids": [(0, 0, vals) for vals in lines_vals],
            }
        )
        return move

    def process_data(self, data):
        """
        Process the data from the file and create the account move.
        """
        line_mappings = self.payroll_import_mapping_ids.filtered(
            lambda x: x.res_model == "account.move.line"
        )

        vals_list, agg_lines = [], {}
        for row in data:
            partner_id = self._get_partner_id(row[self.column_employee_id - 1])
            for mapping in line_mappings:
                vals = self._prepare_line_vals(row, mapping)
                if not vals:
                    continue

                if mapping.aggregate_field and getattr(self, mapping.aggregate_field):
                    current_amount = vals.get(mapping.res_field, 0.0)
                    if mapping.id in agg_lines:
                        agg_lines[mapping.id][mapping.res_field] += current_amount
                    else:
                        agg_lines[mapping.id] = vals
                    continue

                vals_list.append({**vals, "partner_id": partner_id})

            vals_list.extend(self._prepare_custom_concept_vals_list(row, partner_id))

        vals_list.extend(agg_lines.values())
        return self._create_account_move(vals_list)
