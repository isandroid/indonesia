# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IdnkabupatenKota(models.Model):
    _name = 'idn.kabupaten_kota'
    _description = 'Data Kabupaten dan Kota'

    name = fields.Char(string="kabupaten-kota")
    id_kabupaten_kota = fields.Integer(string="id kabupaten-kota")
    provinsi_id = fields.Many2one('idn.provinsi', string="provinsi")
