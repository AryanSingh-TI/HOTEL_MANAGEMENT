from odoo import models, fields, api, _
from odoo.exceptions import ValidationError 
from datetime import datetime

class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Hotel Booking'

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True,ondelete='cascade')
    room_id = fields.Many2one('hotel.room', string='Room', required=True)
    check_in_date = fields.Date(string='Check-In Date', required=True)
    check_out_date = fields.Date(string='Check-Out Date',required=False)

    total_booking_price = fields.Monetary(string="Total Booking Price" , compute = '_compute_total_booking_price' , currency_field='currency_id',store=True)
    currency_id = fields.Many2one('res.currency',string = "Currency")

    days_count = fields.Integer(string='Number of Days', compute='_compute_days_count',store=True)

    @api.depends('check_in_date', 'check_out_date')
    def _compute_days_count(self):
        for record in self:
            if record.check_in_date and record.check_out_date and (record.check_in_date <= record.check_out_date):
                check_in = record.check_in_date
                check_out = record.check_out_date
                delta = check_out - check_in
                record.days_count = delta.days + 1
            else:
                record.days_count = 0

    @api.depends('room_id.price','days_count')
    def _compute_total_booking_price(self):
        for record in self:
            record.total_booking_price = record.days_count * record.room_id.price

    @api.constrains('check_in_date', 'check_out_date', 'room_id')
    def _check_no_overlap(self):
        for record in self:
        
            overlapping_bookings = self.env['hotel.booking'].search([
                ('room_id', '=', record.room_id.id),
                ('id', '!=', record.id),  
                ('check_in_date', '<=', record.check_out_date),
                ('check_out_date', '>=', record.check_in_date),
            ])
            if overlapping_bookings:
                raise ValidationError(_("The selected room is already booked for the given dates. Please choose different dates or a different room."))
    
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
    
    
