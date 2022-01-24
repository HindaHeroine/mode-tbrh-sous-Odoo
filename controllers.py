# -*- coding: utf-8 -*-
from openerp import http

# class Tbrh(http.Controller):
#     @http.route('/tbrh/tbrh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tbrh/tbrh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tbrh.listing', {
#             'root': '/tbrh/tbrh',
#             'objects': http.request.env['tbrh.tbrh'].search([]),
#         })

#     @http.route('/tbrh/tbrh/objects/<model("tbrh.tbrh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tbrh.object', {
#             'object': obj
#         })