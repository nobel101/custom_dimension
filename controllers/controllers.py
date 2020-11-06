# -*- coding: utf-8 -*-
# from odoo import http


# class ../custom/addons/customDimension(http.Controller):
#     @http.route('/../custom/addons/custom_dimension/../custom/addons/custom_dimension/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../custom/addons/custom_dimension/../custom/addons/custom_dimension/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../custom/addons/custom_dimension.listing', {
#             'root': '/../custom/addons/custom_dimension/../custom/addons/custom_dimension',
#             'objects': http.request.env['../custom/addons/custom_dimension.../custom/addons/custom_dimension'].search([]),
#         })

#     @http.route('/../custom/addons/custom_dimension/../custom/addons/custom_dimension/objects/<model("../custom/addons/custom_dimension.../custom/addons/custom_dimension"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../custom/addons/custom_dimension.object', {
#             'object': obj
#         })
