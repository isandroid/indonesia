# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IdnKecamatan(models.Model):
    _name = 'idn.kecamatan'
    _description = 'Data Kecamatan'

    name = fields.Char(string="kecamatan")
    id_kecamatan = fields.Integer(string="id kecamatan")
    kabupaten_kota_id = fields.Many2one('idn.kabupaten_kota', string="kabupaten-kota")
    provinsi_id = fields.Many2one('idn.provinsi', string="provinsi", compute="_compute_provinsi", store=True)

    @api.depends('kabupaten_kota_id')
    def _compute_provinsi(self):
        for record in self:
            record.provinsi_id = record.kabupaten_kota_id.provinsi_id