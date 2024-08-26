from odoo import models, fields


class Guru(models.Model):
    _name = 'addonssekolah.guru'
    _description = 'addonssekolah.guru'

    name = fields.Char(string="Nama Guru")
    nip = fields.Char(string="NIP")
    jns_kelamin = fields.Selection([
        ('lk', 'Laki-Laki'),
        ('pr', 'Perempuan')
    ], string="Jenis Kelamin")
    mata_pelajaran = fields.Many2one('addonssekolah.matapelajaran', string="Mata Pelajaran")
    usia = fields.Char(string="Usia")
    no_telp = fields.Char(string="Nomor Telepon")
    alamat = fields.Char(string="Alamat")