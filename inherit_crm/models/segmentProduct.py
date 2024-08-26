from odoo import models, fields

class SegmentProduct(models.Model):
    _name = 'segment.product'
    _description = 'Segment Product'

    name = fields.Char(string='Segment Name', required=True)
    description = fields.Text(string='Description')
