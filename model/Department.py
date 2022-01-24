# coding=utf-8
from openerp import models, fields, api


class Departement(models.Model):
    _name = 'tbrh.department'
    _inherit = 'hr.department'

    name = fields.Char()

    # employee_id = fields.One2many('hr.employee', 'department_id', string=' Id département')
