from odoo import models, fields

class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'

    name = fields.Char(string='Customer Name', required=True)
    contact_info = fields.Char(string='Contact Information',required=True)
    booking_ids = fields.One2many( comodel_name = 'hotel.booking' , inverse_name='customer_id', string = 'Booking Details', readonly=True)
    is_verified = fields.Boolean(string = 'is Verified',default=False)

    def perform_clean_up(self):
        
        customers_without_bookings = self.env['hotel.customer'].search([('booking_ids', '=', False)])
        customers_without_bookings.unlink()
    
    def perform_verification(self):

        valid_phone_customers = self.env['hotel.customer'].search([])

        for customer in valid_phone_customers:
            if len(customer.contact_info)==10 and customer.contact_info.isdigit():
                customer.is_verified =  True
