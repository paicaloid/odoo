from dateutil.relativedelta import relativedelta

from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"

    name = fields.Char("Property Name", required=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date(
        "Date Availability",
        copy=False,
        default=lambda self: fields.Date.today() + relativedelta(months=3),
    )
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation = fields.Selection(
        string="Type",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        help="Orientation of the garden",
    )
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        string="Status",
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("cancelled", "Cancelled"),
        ],
        default="new",
        required=True,
        copy=False,
    )

    type_id = fields.Many2one(
        string="Property Type",
        comodel_name="estate.property.type",
        required=True,
    )
    user_id = fields.Many2one(
        "res.users",
        string="Salesman",
        index=True,
        default=lambda self: self.env.user,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Buyer",
        index=True,
        copy=False,
        # domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",
        # help="Linked partner (optional). Usually created when converting the lead. You can find a partner by its Name, TIN, Email or Internal Reference.",
    )

    tags_id = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many(
        "estate.property.offer",
        inverse_name="partner_id",
        string="Offers",
    )
