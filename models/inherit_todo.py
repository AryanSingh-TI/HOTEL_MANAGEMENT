from odoo import api,fields,models,_

class inherit_todo(models.Model):
    _inherit =  'hotel.todo'

    is_done = fields.Boolean(default=False)

    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ], string="Priority", default='medium')

    description = fields.Text(string="Task Description")

    name = fields.Char(string="Task Name", required=True)

