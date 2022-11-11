# -*- coding: utf-8 -*-
# from odoo import http


# class Transportacion(http.Controller):
#     @http.route('/transportacion/transportacion', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transportacion/transportacion/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('transportacion.listing', {
#             'root': '/transportacion/transportacion',
#             'objects': http.request.env['transportacion.transportacion'].search([]),
#         })

#     @http.route('/transportacion/transportacion/objects/<model("transportacion.transportacion"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transportacion.object', {
#             'object': obj
#         })
