from odoo import fields, models


class EstateType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char("Type Name", required=True)
