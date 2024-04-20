# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ecommerce_market(models.Model):
    _name = 'ecommerce_market.ecommerce_market'
    _description = 'ecommerce_market.ecommerce_market'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 100

