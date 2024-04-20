# -*- coding: utf-8 -*-
# from odoo import http


# class EcommerceMarket(http.Controller):
#     @http.route('/ecommerce_market/ecommerce_market', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ecommerce_market/ecommerce_market/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('ecommerce_market.listing', {
#             'root': '/ecommerce_market/ecommerce_market',
#             'objects': http.request.env['ecommerce_market.ecommerce_market'].search([]),
#         })

#     @http.route('/ecommerce_market/ecommerce_market/objects/<model("ecommerce_market.ecommerce_market"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ecommerce_market.object', {
#             'object': obj
#         })

