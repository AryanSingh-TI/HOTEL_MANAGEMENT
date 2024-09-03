from odoo import models, fields

class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'

    name = fields.Char(string='Customer Name', required=True)
    contact_info = fields.Char(string='Contact Information',required=True)
    booking_ids = fields.One2many( comodel_name = 'hotel.booking' , inverse_name='customer_id', string = 'Booking Details', readonly=True)