# -*- coding: utf-8 -*-

from odoo import models, fields,api

class Custom_Dimension(models.Model):
    _inherit = 'sale.order.line'
    
    dimension = fields.Char(String="XxX")
    
    def _prepare_procurement_values(self, group_id=False):
        res = super(Custom_Dimension, self)._prepare_procurement_values(group_id)
        res.update({'dimension': self.dimension}) #list of fields you want to move with the sale order line to stock move 
        return res    


class Custom_StockRule(models.Model):
    _inherit = 'stock.rule'
    def _get_stock_move_values(self, product_id, product_qty, product_uom, location_id, name, origin, values, group_id):
        res = super(Custom_StockMove, self)._get_stock_move_values(product_id, product_qty, product_uom, location_id,
                                                            name, origin, values, group_id)
        res['dimension'] = values.get('dimension', False)
        return res   
    
class Custom_StockMove(models.Model):
    _inherit='stock.move'
    
    dimension = fields.Char(String="XxX",compute='get_data',inverse='_inverse_get_data')

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
    
    def _inverse_get_data(self):
        for move in self:
            if not (move.picking_id and move.picking_id.group_id):
                continue
            picking = move.picking_id
            sale_order = self.env['sale.order'].sudo().search([
                ('procurement_group_id', '=', picking.group_id.id)], limit=1)
        for line in sale_order.order_line:
            if line.product_id.id != move.product_id.id:
                continue
            line.update({
                'dimension': line.dimension,
            })        
                    
