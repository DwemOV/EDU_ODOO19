from odoo import models, fields


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient"

    name = fields.Char(required=True)
    birth_date = fields.Date()
    phone = fields.Char()
    address = fields.Text()
