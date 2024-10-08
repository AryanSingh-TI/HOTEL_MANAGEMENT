from odoo import fields,models,api,_
from odoo.exceptions import ValidationError 

class HotelRating(models.Model):
    _name="hotel.rating"
    _description="Ratings of Hotel Rooms"

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True,ondelete='cascade')
    room_id = fields.Many2one('hotel.room',string="Room Number",required=True)
    rating = fields.Float(string="Rating of the Room",required=True,help="Enter a Rating from  1 to 10")

    @api.constrains('rating')
    def check_ratings(self):
        for record in self:
            if record.rating > 10 or record.rating < 1:
                raise ValidationError(_("Error! Rating Should be between the range 1 to 10"))
    
    @api.constrains('customer_id', 'room_id')
    def _verify_rating(self):
        for record in self:
            
            if not record.customer_id:
                raise ValidationError(_("The customer must exist before adding a rating."))

            
            if not record.room_id:
                raise ValidationError(_("The room must exist before adding a rating."))


            booking_exists = self.env['hotel.booking'].search_count([
                ('customer_id', '=', record.customer_id.id),
                ('room_id', '=', record.room_id.id)
            ])
            
            if booking_exists == 0:
                raise ValidationError(_("The customer must have a booking record for the specified room before adding a rating."))

    
    
    

