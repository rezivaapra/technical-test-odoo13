from odoo import models, fields


class Siswa(models.Model):
    _name = 'addonssekolah.siswa'
    _description = 'addonssekolah.siswa'

    name = fields.Char(string="Nama Siswa")
    nis = fields.Char(string="NIS")
    jns_kelamin = fields.Selection([
        ('lk', 'Laki-Laki'),
        ('pr', 'Perempuan')
    ], string="Jenis Kelamin")
    tgl_lahir = fields.Date(string="Tanggal Lahir")
    agama = fields.Selection([
        ('islam', 'Islam'),
        ('kristen', 'Kristen'),
        ('katolik', 'Katolik'),
        ('hindu', 'Hindu'),
        ('buddha', 'Buddha'),
        ('khonghucu', 'Khonghucu')
    ], string="Agama")
    nm_ayah = fields.Char(string="Nama Ayah")
    nm_ibu = fields.Char(string="Nama Ibu")
    usia = fields.Char(string="Usia")
    alamat = fields.Char(string="Alamat")