from odoo import models, fields


class Jadwal(models.Model):
    _name = 'addonssekolah.jadwal'
    _description = 'addonssekolah.jadwal'

    name = fields.Selection([
        ('senin', 'Senin'),
        ('selasa', 'Selasa'),
        ('rabu', 'Rabu'),
        ('kamis', 'Kamis'),
        ('jumat', 'Jumat'),
        ('minggu', 'Minggu')
    ], string="Hari")
    kelas = fields.Many2one('addonssekolah.kelaskelas', string="Kelas")
    jam = fields.Char("Jam")
    mata_pelajaran = fields.Many2one('addonssekolah.matapelajaran', string="Mata Pelajaran")
