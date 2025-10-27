# -*- coding: utf-8 -*-

from odoo import models, fields, api


class IdnProvinsi(models.Model):
    _name = 'idn.provinsi'
    _description = 'Data Provinsi'
    _order = 'name asc'
    
    name = fields.Char(string="provinsi")
    id_provinsi = fields.Integer(string="id provinsi")