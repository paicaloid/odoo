from odoo import fields, models


class EstateOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"

    price = fields.Float("Price")
    status = fields.Selection(
        string="Type",
        copy=False,
        selection=[
            ("accepted", "Accepted"),
            ("refused", "Refused"),
        ],
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        index=True,
        required=True,
    )
    property_id = fields.Many2one(
        "estate.property",
        string="Property",
        index=True,
        required=True,
    )
