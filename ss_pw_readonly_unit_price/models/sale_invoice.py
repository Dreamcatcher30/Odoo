# -*- coding: utf-8 -*-

from odoo import fields, models, api, _
from odoo.exceptions import UserError, ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_readonly_price = fields.Boolean(compute="_compute_is_readonly_price", readonly=True)

    def _compute_is_readonly_price(self):
        for order in self:
            order.is_readonly_price = self.env.user.has_group('ids_pw_readonly_unit_price.group_sale_unit_price')

    @api.model
    def default_get(self,default_fields):
        res = super(SaleOrder, self).default_get(default_fields)
        res['is_readonly_price'] = self.env.user.has_group('ids_pw_readonly_unit_price.group_sale_unit_price')
        return res

class AccountMove(models.Model):
    _inherit = 'account.move'

    is_readonly_price = fields.Boolean(compute="_compute_is_readonly_price", readonly=True)

    def _compute_is_readonly_price(self):
        for order in self:
            order.is_readonly_price = self.env.user.has_group('ids_pw_readonly_unit_price.group_invoice_unit_price')

    @api.model
    def default_get(self,default_fields):
        res = super(AccountMove, self).default_get(default_fields)
        res['is_readonly_price'] = self.env.user.has_group('ids_pw_readonly_unit_price.group_invoice_unit_price')
        return res
