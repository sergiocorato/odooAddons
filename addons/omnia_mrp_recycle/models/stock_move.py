'''
Created on 5 Jun 2018

@author: dsmerghetto
'''
from odoo import api, fields, models, _


class StockMove(models.Model):
    _inherit = "stock.move"

    recycle_id = fields.Many2one('stock.recicle_product')
