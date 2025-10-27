# -*- coding: utf-8 -*-
# from odoo import http


# class Idn(http.Controller):
#     @http.route('/idn/idn', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/idn/idn/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('idn.listing', {
#             'root': '/idn/idn',
#             'objects': http.request.env['idn.idn'].search([]),
#         })

#     @http.route('/idn/idn/objects/<model("idn.idn"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('idn.object', {
#             'object': obj
#         })
