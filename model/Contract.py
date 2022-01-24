from openerp import models, fields, api


class Contract(models.Model):
    _inherit = 'hr.contract'

    employee_cont_id = fields.Many2one('hr.employee', ondelete='cascade')

    type_id = fields.Many2one('hr.contract.type', ondelete='cascade', string="type contract"
                              , store=True, required='True')
    # cont1 = fields.Char(RELATED='hr.contract;rel.name;', store=True, use_parent_address=False)
    # cont2 = fields.Char(related='contract_type.name', store=True)

    nbr_cdd = fields.Float(compute="get_count_cdd_cdi", store=True)
    nbr_cdi = fields.Float(compute="get_count_cdd_cdi", store=True)

    @api.multi
    @api.depends('type_id')
    def get_count_cdd_cdi(self):
        for r in self:
            r.nbr_cdd = r.search_count([('type_id', '=', 'cdd')])
            r.nbr_cdi = r.search_count([('type_id', '=', 'cdi')])

    nbr_employee = fields.Float(compute='get_count_employee', store='True')

    @api.multi
    def get_count_employee(self):
        for t in self:
            t.nbr_employee = t.env['hr.employee'].sudo().search_count([('active', '=', True)])
