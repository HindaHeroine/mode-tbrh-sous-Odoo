from openerp import models, fields, api


class Administrateur(models.Model):
    _inherit = 'tbrh.admin'

    employee_id = fields.One2many('tbrh.employee',
                                  'admin_id', string=' Id employee')

    nbr_homme = fields.Float(compute='get_count_by_sex', store='True')
    nbr_femme = fields.Float(compute='get_count_by_sex', store='True')

    nbr_employees = fields.Float(compute='get_count_employee', store='True')
    nbr_handicap = fields.Float(compute='get_count_handicap', store='True')

    @api.one
    @api.depends('employee_id.situation_handicap')
    def get_count_handicap(self):
        self.nbr_handicap = self.env['hr.employee'].sudo().search_count([('situation_handicap', '=', True)])

    @api.one
    def get_count_employee(self):
        for t in self:
            t.nbr_employees = t.search_count([('active', '=', True)])


    @api.one
    @api.depends('employee_id.gender')
    def get_count_by_sex(self):
        self.nbr_homme = self.env['hr.employee'].sudo().search_count([('gender', '=', 'male')])
        self.nbr_femme = self.env['hr.employee'].sudo().search_count([('gender', '=', 'female')])
