from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "Doctor"

    name = fields.Char(required=True)
    specialty = fields.Char()
    phone = fields.Char()
    email = fields.Char()
    mentor_id = fields.Many2one(
        'hospital.doctor',
        string='Mentor Doctor'
    )
    mentee_ids = fields.One2many(
        'hospital.doctor',
        'mentor_id',
        string='Mentees'
    )

    @api.constrains('mentor_id')
    def _check_mentor_not_self(self):
        for record in self:
            if record.mentor_id and record.mentor_id == record:
                raise ValidationError(
                    _('A doctor cannot be their own mentor.')
                )
