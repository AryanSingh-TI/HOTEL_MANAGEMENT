from odoo import models, fields, api , _

class HotelTodo(models.Model):
    _name = 'hotel.todo'
    _description = "Hotel To-Do List"

    
    assigned_employee_id = fields.Many2many('hotel.employees', string="Assigned Employee", required=True)
    start_date = fields.Date(string="Start Date")
    due_date = fields.Date(string="Due Date")
    is_done = fields.Boolean(string="Done",default=True)

    
