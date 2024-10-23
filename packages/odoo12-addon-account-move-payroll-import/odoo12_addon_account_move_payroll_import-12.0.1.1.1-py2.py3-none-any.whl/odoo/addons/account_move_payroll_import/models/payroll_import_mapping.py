from odoo import models, fields, _


class PayrollImportMapping(models.Model):
    _name = "payroll.import.mapping"
    _description = "Payroll Import Mapping"

    name = fields.Char(string="Name", required=True, default="payroll.import.setup")
    res_model = fields.Char(string=_("Model"))
    res_field = fields.Char(string=_("Field"))
    column_field = fields.Char(string=_("Column Field"), required=True)
    account_field = fields.Char(string=_("Account Field"))
    tax_field = fields.Char(string=_("Tax Field"))
    aggregate_field = fields.Char(string=_("Aggregate Flag Field"))
    payroll_import_setup_id = fields.Many2many(
        comodel_name="payroll.import.setup",
        string="Payroll Import Setup",
    )

    _sql_constraints = [
        (
            "unique_mapping",
            "unique(name, res_model, res_field, column_field)",
            "This mapping already exists.",
        )
    ]
