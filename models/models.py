# -*- coding: utf-8 -*-

from odoo import models, fields

class Custom_Dimension(models.Model):
    _inherit = 'sale.order.line'
    
    dimension = fields.Char(String="XxX")
    
    def _prepare_procurement_values(self, group_id=False):
        res = super(Custom_Dimension, self)._prepare_procurement_values(group_id)
        res.update({'dimension': self.dimension}) #list of fields you want to move with the sale order line to stock move 
        return res    

# class Custom_StockMove(models.Model):
#     _inherit = 'stock.move'
#     dimension = fields.Char(String="XxX")
#     @api.model
#     def get_data(self):
#         for move in self:
#             if not (move.picking_id and move.picking_id.group_id):
#                 continue
#             picking = move.picking_id
#             sale_order = self.env['sale.order'].sudo().search([
#                 ('procurement_group_id', '=', picking.group_id.id)], limit=1)
#             for line in sale_order.order_line:
#                 if line.product_id.id != move.product_id.id:
#                     continue
#                 move.update({
#                     'x_serialnumber': line.x_serialnumber,
#                 })

class Custom_StockMove(models.Model):
    _inherit = 'stock.picking'
    
    #field in stock.picking model
    dimension = fields.Char(String="XxX",compute='get_date')

    def get_data(self):
        for move in self:
            if not (move.picking_id and move.picking_id.group_id):
                continue
            picking = move.picking_id
            sale_order = self.env['sale.order'].sudo().search([
                ('procurement_group_id', '=', picking.group_id.id)], limit=1)
            for line in sale_order.order_line:
                if line.product_id.id != move.product_id.id:
                    continue
                move.update({
                    'dimension': line.dimension,
                })