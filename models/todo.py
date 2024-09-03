from odoo import models, fields, api , _

class HotelTodo(models.Model):
    _name = 'hotel.todo'
    _description = "Hotel To-Do List"

    name = fields.Char(string="Task Name", required=True)
    description = fields.Text(string="Task Description")
    assigned_employee_id = fields.Many2one('hotel.employees', string="Assigned Employee", required=True)
    start_date = fields.Date(string="Start Date")
    due_date = fields.Date(string="Due Date")
    is_done = fields.Boolean(string="Done", default=False)
