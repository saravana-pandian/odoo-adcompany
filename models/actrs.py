from odoo import api, fields, models
class Adflim(models.Model):
    _name = "ad.flim"
    _description = "actrs"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    country = fields.Char(string='Country')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'other'),
    ], required=True, default='male')
    availability = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ], required=True, default='unavailable')

    note = fields.Text(string='Description')