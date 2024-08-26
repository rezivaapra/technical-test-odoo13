from odoo import models, fields


class MataPelajaran(models.Model):
    _name = 'addonssekolah.matapelajaran'
    _description = 'addonssekolah.pelajaran'

    name = fields.Char(string="Nama Matapelajaran")
    jurusan = fields.Char(string="Jurusan")
