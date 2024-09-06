from odoo import models, fields , api  , _

class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Hotel Customer'

    name = fields.Char(string='Customer Name', required=True)
    contact_info = fields.Char(string='Contact Information',required=True)
    booking_ids = fields.One2many( comodel_name = 'hotel.booking' , inverse_name='customer_id', string = 'Booking Details', readonly=True)
    is_verified = fields.Boolean(string = 'is Verified',default=False)
    customer_ratings = fields.One2many('hotel.rating','customer_id',string = "Customer Ratings")
    def perform_clean_up(self):
        
        customers_without_bookings = self.env['hotel.customer'].search([('booking_ids', '=', False)])
        customers_without_bookings.unlink()
    
    def perform_verification(self):

        valid_phone_customers = self.env['hotel.customer'].search([])

        for customer in valid_phone_customers:
            if len(customer.contact_info)==10 and customer.contact_info.isdigit():
                customer.is_verified =  True
    @api.model
    def create(self, vals):
        
        new_record = super(HotelCustomer, self).create(vals)
        self._merge_duplicate_customers(new_record.id)
        return new_record

    def _merge_duplicate_customers(self, new_customer_id):

        customer_groups = self.env['hotel.customer'].read_group(
            [('name', '!=', False), ('contact_info', '!=', False)],
            ['name', 'contact_info', 'ids:array_agg(id)'], 
            ['name', 'contact_info'],  
            lazy=False
        )

        for group in customer_groups:
            customer_ids = group['ids']
            if len(customer_ids) > 1:  

                if new_customer_id in customer_ids:
                    
                    existing_ids = [cid for cid in customer_ids if cid != new_customer_id]

                    if existing_ids:
                        new_customer = self.env['hotel.customer'].browse(new_customer_id)

        
                        existing_customers = self.env['hotel.customer'].browse(existing_ids)
                        for existing_customer in existing_customers:
                    
                            for booking in existing_customer.booking_ids:
                                booking.customer_id = new_customer.id  

                            
                            for rating in existing_customer.customer_ratings:
                                rating.customer_id = new_customer.id 

                            existing_customer.unlink()

        return True

