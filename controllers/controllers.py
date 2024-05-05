# -*- coding: utf-8 -*-
# from odoo import http


# class Trasteros(http.Controller):
#     @http.route('/trasteros/trasteros', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trasteros/trasteros/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trasteros.listing', {
#             'root': '/trasteros/trasteros',
#             'objects': http.request.env['trasteros.trasteros'].search([]),
#         })

#     @http.route('/trasteros/trasteros/objects/<model("trasteros.trasteros"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trasteros.object', {
#             'object': obj
#         })
