# -*- coding: utf-8 -*-
# from odoo import http


# class HospitalManagmentSystem(http.Controller):
#     @http.route('/hospital__managment__system/hospital__managment__system/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hospital__managment__system/hospital__managment__system/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hospital__managment__system.listing', {
#             'root': '/hospital__managment__system/hospital__managment__system',
#             'objects': http.request.env['hospital__managment__system.hospital__managment__system'].search([]),
#         })

#     @http.route('/hospital__managment__system/hospital__managment__system/objects/<model("hospital__managment__system.hospital__managment__system"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hospital__managment__system.object', {
#             'object': obj
#         })
