# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.odoo.exceptions import ValidationError


class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = 'hospital__managment__system.hospital__managment__system'

    name = fields.Char()
    capacity = fields.Integer()
    is_opend = fields.Boolean()
    patients_id = fields.One2many('hms.patients', 'department_id')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

    # @api.constrains('is_opend')
    # def _check_isOpend(self):
    #     if self.is_opend:
    #         raise ValidationError('value 2 must be less than 200')

    # @api.onchange('is_opend')
    # def on_change(self):
    #     # self.float = self.value / 3
    #     # if self.is_opend:
    #          raise ValidationError('value 2 must be less than 200')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100

class HmsDoctor(models.Model):
    _name = 'hms.doctors'
    _description = 'This is Doctors'
    _rec_name = 'fname'

    fname = fields.Char()
    lname = fields.Char()
    image = fields.Binary()

class HmsPatient(models.Model):
    _name = 'hms.patients'
    _description = 'hThis is patients'
    # _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'fname'

    department_id = fields.Many2one('hms.department', 'Department Name')


#
    fname = fields.Char(string='First Name',  default='Ahmed', required=True)
    lname = fields.Char(string='Last Name', required=True)
    date_of_birth = fields.Date()
    history = fields.Html()
    cr_ratio = fields.Float()
    blood_type = fields.Selection(
        [('a', 'A'), ('b', 'B'), ('o', 'O'), ('ab', 'AB')], default='a')
    state = fields.Selection(
        [('undetermined', 'Undetermined'), ('good', 'Good'), ('fair', 'Fair'), ('serious', 'Serious')], default='undetermined', tracking=True)

    pcr = fields.Boolean()
    image = fields.Binary()
    address = fields.Text()
    age = fields.Integer()

    # @api.onchange('age')
    # @api.constrains('age')
    # @api.depends('age')
    # def on_change(self):
    #     for record in self:
    #         if record.age < 30:
    #             record.pcr = True
            # # if self.is_opend:
            #      raise ValidationError('value 2 must be less than 200')
    @api.onchange('age')
    def on_change(self):
        if self.age < 30:
            self.pcr = True
            # raise ValidationError('PCR is Ckecked')
        else:
            self.pcr = False


