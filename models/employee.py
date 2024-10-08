from odoo import models, fields, api, _

class HotelEmployee(models.Model):
    _name = 'hotel.employees'
    _description = "Hotel Employees"

    name = fields.Char(string="Name of the Employee", required=True)
    default_salary = fields.Float(string="Salary of the Employee", required=True)
    role_id = fields.Selection([
        ('managers', 'Managers'),
        ('security', 'Security'),
        ('restaurant_staff', 'Restaurant Staff'),
        ('regular_staff', 'Regular Staff')
    ], string='Role Type', required=True)

    sub_role_id = fields.Selection([
        ('head_manager', 'Head Manager'),
        ('assistant_manager', 'Assistant Manager'),
        ('security_head', 'Security Head'),
        ('security_guard', 'Security Guard'),
        ('chef', 'Chef'),
        ('waiter', 'Waiter'),
        ('bartender', 'Bartender'),
        ('housekeeping', 'Housekeeping'),
        ('receptionist', 'Receptionist')
    ], string='Sub Role')
    
    
    ratings = fields.Selection([
            ('0', 'Low'),
            ('1', 'Moderate'),
            ('2', 'High'),
            ('3', 'Very High')
        ], string="Performance Rating", default='0')
    
    employee_document = fields.Binary(string='Employee Document')
    attendance =  fields.One2many('hotel.attendance','employee_id',string='Attendance',readonly=True)

    