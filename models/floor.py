from odoo import models, fields , api , _

class HotelFloor(models.Model):
    _name = 'hotel.floor'
    _description = 'Hotel Floor'

    name = fields.Char(string='Floor Name', required=True)
    room_ids = fields.One2many('hotel.room', 'floor_id', string='Rooms',readonly=True)
    room_count = fields.Integer(string='Number of Rooms', compute='_compute_room_count', store=True)

    @api.depends('room_ids')
    def _compute_room_count(self):
        for floor in self:
            floor.room_count = len(floor.room_ids)