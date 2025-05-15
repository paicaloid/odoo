from odoo import fields, models


class EstateTag(models.Model):
    _name = "estate.property.tag"
    _description = "Estate Property Tag"

    name = fields.Char("Tag Name", required=True)
