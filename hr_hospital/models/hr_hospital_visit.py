from odoo import models, fields


class HospitalVisit(models.Model):
    _name = "hospital.visit"
    _description = "Patient Visit"

    patient_id = fields.Many2one("hospital.patient", required=True)
    doctor_id = fields.Many2one("hospital.doctor", required=True)
    disease_id = fields.Many2one("hospital.disease",)
    visit_date = fields.Datetime(default=fields.Datetime.now)
    notes = fields.Text()
