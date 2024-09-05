from odoo import fields,models,api,_
from odoo.exceptions import ValidationError 

class HotelRating(models.Model):
    _name="hotel.rating"
    _description="Ratings of Hotel Rooms"

    customer_id = fields.Many2one('hotel.customer', string='Customer', required=True)
    room_id = fields.Many2one('hotel.room',string="Room Number",required=True)
    rating = fields.Float(string="Rating of the Room",required=True,help="Enter a Rating from  1 to 10")

    @api.constrains('rating')
    def check_ratings(self):
        for record in self:
            if record.rating > 10 or record.rating < 1:
                raise ValidationError(_("Error! Rating Should be between the range 1 to 10"))
    
    

