from odoo import models, fields


class HospitalDisease(models.Model):
    _name = "hospital.disease"
    _description = "Disease"

    name = fields.Char(required=True)
    description = fields.Text()
