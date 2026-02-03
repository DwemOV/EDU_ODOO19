from odoo import models, fields


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"

    name = fields.Char(required=True)
    specialty = fields.Char()
    phone = fields.Char()
    email = fields.Char()
