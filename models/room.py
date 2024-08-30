from odoo import models, fields , api , _

class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Hotel Room'

    name = fields.Char(string='Room Number', required=True)
    floor_id = fields.Many2one('hotel.floor', string='Floor', required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite')
    ], string='Room Type', required=True)
    price = fields.Float(string='Price per Night', required=True)
    availability = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied')
    ], string='Availability', default='available', required=True)

    booking_ids = fields.One2many('hotel.booking','room_id',string="Bookings")

    room_image = fields.Binary(string = "Room Image")

    @api.depends('booking_ids.check_in_date')
    def _compute_availability(self):
        for room in self:
        
            nearest_check_in = min(room.booking_ids.mapped('check_in_date'), default=None)
            if nearest_check_in and nearest_check_in > date.today():
                room.availability = f"Available until {nearest_check_in.strftime('%Y-%m-%d')}"
            else:
                room.availability = "Available"