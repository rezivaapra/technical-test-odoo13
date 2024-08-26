from odoo import models, fields

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    is_new_customer = fields.Boolean(string="Pelanggan Baru?")
    customer_segment = fields.Selection([
        ('kontruksi', 'Kontruksi'),
        ('perbankan', 'Perbankan'),
        ('pemerintah', 'Pemerintah'),
        ('bumd_bumn', 'BUMD/BUMN'),
        ('kementrian', 'Kementrian'),
        ('swasta_lainnya', 'Swasta Lainnya')
    ], string="Segment Pelanggan")
    segment_product_id = fields.Many2one('segment.product', string="Segment Product")
    task = fields.Char(string="Task")
    deadline = fields.Date(string='Deadline')
    status = fields.Selection(
        [('to_do', 'To Do'),
         ('progress', 'In Progress'),
         ('done', 'Done')],
        string='Status',
        default='to_do'
    )