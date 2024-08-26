from odoo import models, fields


class KelasKelas(models.Model):
    _name = 'addonssekolah.kelaskelas'
    _description = 'addonssekolah.kelaskelas'

    name = fields.Char(string="Nama Kelas")
    nm_siswa = fields.Many2many('addonssekolah.siswa', string='Siswa')
    wali_kelas = fields.Many2one('addonssekolah.guru', string="Wali Kelas")
