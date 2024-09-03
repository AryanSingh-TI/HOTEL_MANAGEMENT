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
    price = fields.Monetary(string='Price per Day', required=True, currency_field='currency_id')
    availability = fields.Selection([
        ('available', 'Available'),
        ('occupied', 'Occupied')
    ], string='Availability', compute='_compute_availability')

    booking_ids = fields.One2many('hotel.booking','room_id',string="Bookings",readonly=True)

    room_image = fields.Binary(string = "Room Image")
    currency_id = fields.Many2one('res.currency', string='Currency')

    @api.depends('booking_ids.check_in_date','booking_ids.check_out_date')
    def _compute_availability(self):
        today = fields.Date.today()
        for room in self:
            room.availability = 'available'
            for booking in room.booking_ids:
                if booking.check_in_date <= today and today <= booking.check_out_date:
                    room.availability = 'occupied'
                    break
        