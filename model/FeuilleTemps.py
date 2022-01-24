  # coding=utf-8

from datetime import timedelta
from openerp import models, fields, api


class FeuilleTemps(models.Model):
    _name = 'tbrh.feuilletemps'
    _rec_name = 'name_emp'

    employee_id = fields.Many2one('hr.employee', ondelete='cascade', string="Id employee")
    # M2O utiliser related fields pour afficher dans la view feuilletemp les fields de model employee
    name_emp = fields.Many2one('hr.employee', string="Employé", required='True')
    name_dep = fields.Many2one(related='name_emp.department_id', string="Département", readonly="1")

    absence_ids = fields.One2many('tbrh.absences', 'feuille_id', string="Feuille de temps")
    date_jour = fields.Date(default=fields.Date.today, store=True, use_parent_address=False)
    # O2M utiliser related fields pour afficher dans la view feuilletemp les fields de model absence
    date2 = fields.Date(related='absence_ids.date', store=True, use_parent_address=False)
    statut2 = fields.Selection(related='absence_ids.statut', store=True)
    h_arrive2 = fields.Float(related='absence_ids.h_arrive')
    h_sortie2 = fields.Float(related='absence_ids.h_sortie')
    motif2 = fields.Many2one(related='absence_ids.motif')

    somme_h_absence = fields.Float(string="somme des heures d'absence", compute='_compute_somme_h_absence', store=True)
    somme_h_supp = fields.Float(string="somme d'heures supplémentaire", compute='_compute_somme_h_supp', store=True)
    count_line = fields.Float(compute='_calc_line_ids')
    taux_abs = fields.Float(string="taux d'absentéisme ", store=True, compute='_taux_abs')
    color = fields.Integer()  # for kanban's view

    @api.depends('absence_ids')
    def _calc_line_ids(self):
        self.count_line = len(self.absence_ids)

    _sql_constraints = [
        ('Time_sheet_uniq', 'UNIQUE(name_emp)', 'Une seule feuille de temps par employé!')

    ]

    @api.depends('somme_h_absence', 'somme_h_supp', 'count_line')
    def _taux_abs(self):
        for r in self:
            if r.somme_h_absence == 0:
                r.taux_abs = 0.0
            else:
                r.taux_abs = (100.0 * (r.somme_h_absence - r.somme_h_supp)) / (8 * r.count_line)

    @api.one
    @api.depends('absence_ids.nbr_h_absence')
    def _compute_somme_h_absence(self):
        self.somme_h_absence = sum(absence_id.nbr_h_absence for absence_id in self.absence_ids)

    @api.one
    @api.depends('absence_ids.nbr_h_supp')
    def _compute_somme_h_supp(self):
        self.somme_h_supp = sum(absence_id.nbr_h_supp for absence_id in self.absence_ids)

    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
    ]  # , default='draft'
    )

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'

