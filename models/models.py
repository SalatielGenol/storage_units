# -*- coding: utf-8 -*-
import base64

from odoo import models, fields, modules


class Module(models.Model):
    _name = 'storage_units.module'
    _description = 'storage_units.module'

    name = fields.Char(required=True)
    address = fields.Text(required=True)
    map = fields.Char()
    door = fields.Integer()
    blueprint = fields.Image(default=lambda self: _get_default_image())
    comments = fields.Text()
    spaces = fields.One2many(comodel_name='storage_units.space',
                             inverse_name='module')


def _get_default_image():
    with open(modules.get_module_resource(
            'storage_units',
            'static/img/storage-blueprint-template.png'), 'rb') as f:
        return base64.b64encode(f.read())


class MeasureUnit(models.Model):
    _name = 'storage_units.measure_unit'
    _description = 'storage_units.measure_unit'

    name = fields.Char('Measure Unit')
    items = fields.One2many(comodel_name='storage_units.item',
                            inverse_name='measure_unit')


class Item(models.Model):
    _name = 'storage_units.item'
    _description = 'storage_units.item'

    name = fields.Char(string='Item name', required=True)
    measure_unit = fields.Many2one(comodel_name='storage_units.measure_unit')
    item_stock = fields.One2many(comodel_name='storage_units.item_stock',
                                 inverse_name='item')


class ItemStock(models.Model):
    _name = 'storage_units.item_stock'
    _description = 'storage_units.item_stock'

    item = fields.Many2one(string='Item name',
                           comodel_name='storage_units.item')
    name = fields.Integer(string='Quantity')
    measure_unit = fields.Many2one(related='item.measure_unit')
    space = fields.Many2one(comodel_name="storage_units.space")
    module = fields.Many2one(related='space.module')


class Space(models.Model):
    _name = 'storage_units.space'
    _description = 'storage_units.space'

    name = fields.Char(required=True)
    type = fields.Many2many(comodel_name='storage_units.type')
    location = fields.Char()
    module = fields.Many2one(comodel_name='storage_units.module')
    items = fields.One2many(comodel_name='storage_units.item_stock',
                            inverse_name='space')


class Type(models.Model):
    _name = 'storage_units.type'
    _description = 'storage_units.type'

    name = fields.Char(string='Type')
    space = fields.Many2many(comodel_name='storage_units.space')

#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
