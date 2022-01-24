from openerp import models, fields, api


class Employee(models.Model):
    _inherit = 'hr.employee'

    # department_id = fields.Many2one('tbrh.department',
    # ondelete='cascade', string="Departement")

    admin_id = fields.Many2one('tbrh.admin', ondelete='cascade', string="admin")
    timesheet_id = fields.One2many('tbrh.feuilletemps',
                                   'employee_id', string=' Id timesheet')
    contract_id = fields.One2many('hr.contract',
                                  'employee_cont_id', string=' Id contract')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], store='True')

    situation_handicap = fields.Boolean(Default='false', String="Travailleur en situation de handicap ")

