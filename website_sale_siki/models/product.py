# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import openerp
import re
from openerp import models, api, fields

class product_template(models.Model):
    _inherit = 'product.template'

    website_description_shorty = fields.Char('Descripción Producto Sitio Web', sanitize=False)
    website_features = fields.Char('Características Producto Sitio Web', sanitize=False, strip_style=True )

    #value_field_website_description = fields.Boolean(compute='_compute_website_description', store=False)
    #value_field_website_features = fields.Boolean(compute='_compute_website_features', store=False)



    @api.model
    def _compute_website_description(self):

        value = self.website_description_shorty

        if value == '<p><br></p>' or value == '<br>' or value == '' or value == False:
            return True

    @api.model
    def _compute_website_features(self):

        value = self.website_features

        if value == '<p><br></p>' or value == '<br>' or value == '' or value == False:
            return True