from odoo import models, fields, api, _
from odoo.exceptions import ValidationError 
from datetime import datetime

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True)
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in_date = fields.Date(string='Check-In Date', required=True)
    check_out_date = fields.Date(string='Check-Out Date',required=False)

    @api.constrains('check_in_date')
    def _check_checkin_date(self):
        for record in self:
            if record.check_in_date < fields.Date.today():
                raise ValidationError(_("Check in Date Cannot be in the past, Please select a valid date!"))
    
    @api.constrains('check_out_date')
    def _check_checkout_date(self):
        for record in self:
            if record.check_out_date < record.check_in_date:
                raise ValidationError(_("Check out Date cannot be before the check in date, Please select a valid date!"))