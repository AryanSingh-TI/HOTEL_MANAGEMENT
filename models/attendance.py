from odoo import models,fields,api,_
from odoo.exceptions import ValidationError 
import datetime

class HotelAttendance(models.Model):

    _name =  "hotel.attendance"
    _description = "this model is for storing the attendance of hotel employees"

    employee_id = fields.Many2one('hotel.employees',string = "Employee ID",required=True)
    date = fields.Date(string="Date",readonly=True)
    check_in_time = fields.Char(string="Check-in time",readonly=True)
    check_out_time = fields.Char(string="Check-out time",readonly=True)
    checkin = fields.Datetime(string="Check-in Datetime",readonly=True)
    checkout = fields.Datetime(string="Check-out Datetime",readonly=True)
    is_present = fields.Boolean(string = "Is Present",readonly=True)
    time_spent = fields.Char(string =  "Time Spent",readonly=True)
    
    def check_in_the_employee(self):
        for record in self:
            if not record.check_in_time:
                record.checkin = fields.Datetime.now()
                record.date = record.checkin.date()
                record.check_in_time = (record.checkin + datetime.timedelta(hours=5,minutes=30)).strftime("%H:%M")
                 
    def check_out_the_employee(self):

        for record in self:
            record.checkout = fields.Datetime.now() + datetime.timedelta(hours=9,minutes=30)
            record.date = record.checkout.date()
            record.check_out_time = (record.checkout + datetime.timedelta(hours=5,minutes=30)).strftime("%H:%M")
            
            existing_records = self.env['hotel.attendance'].search(
                [('employee_id','=',record.employee_id.id),
                 ('check_out_time','=',False),
                 ('check_in_time','!=',False),
                 ('date','=',record.date)]
                 ,limit = 1
                 )

            if existing_records:
                existing_record = existing_records[0]

                record.checkin =  existing_record.checkin 
                record.check_in_time = existing_record.check_in_time 

                record.is_present = False

                time_difference =  record.checkout - record.checkin

                record.is_present = time_difference > datetime.timedelta(hours=8,minutes=30) and time_difference < datetime.timedelta(hours=24)
                
                total_seconds = time_difference.total_seconds()

                hours = int(total_seconds // 3600)
                minutes = int((total_seconds % 3600) // 60)


                record.time_spent = f"{hours:02d} {minutes:02d}"

                existing_records.unlink()

            else:

                raise ValidationError(_("No check in existing attendanc list on this date by this employee"))

