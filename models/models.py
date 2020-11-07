# -*- coding: utf-8 -*-

from odoo import models, fields,api

class Custom_Dimension(models.Model):
    _inherit = 'sale.order.line'
    
    dimension = fields.Char(String="XxX")

    
class Custom_StockMove(models.Model):
    _inherit='stock.move'

    dimension = fields.Char(String="XxX",compute='get_data',inverse='_inverse_get_data')

    def get_data(self):
        for move in self:
            picking = move.picking_id
            if not (picking and picking.group_id):
                continue
            
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
            picking = move.picking_id
            sale_order = self.env['sale.order'].sudo().search([
                ('procurement_group_id', '=', picking.group_id.id)], limit=1)
            
        for line in sale_order.order_line:
            if line.product_id.id != move.product_id.id:
                continue
            line.update({
                'dimension': line.dimension,
            })  
            if not (picking and picking.group_id):
                continue
            
            
        
class Custom_Invoice(models.Model):
    _inherit='account.move'
    dimension = fields.Char(String="XxX",compute='get_data')

    def get_data(self):
        for move in self:
            picking = move.id
            if not (picking and picking.group_id):
                continue
            
            picking = self.env['stock.move'].sudo().search([
                ('procurement_group_id', '=', picking.group_id.id)], limit=1)
        for line in picking.move_id:
            if line.product_id.id != picking.product_id.id:
                continue
            move.update({
                'dimension': line.dimension,
            })
