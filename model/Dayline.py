# coding=utf-8
from stdnum.exceptions import ValidationError

from openerp import models, fields, api


class Absences(models.Model):
    _name = 'tbrh.absences'

    # incomplet for many2many relation
    # date_id = fields.many2many('tbrh.date', id1='statut', id2='date_jour', relation='date_dayline_relation')
    # date = fields.Date(related='??????????????????', use_parent_address=False, store=True)
    feuille_id = fields.Many2one('tbrh.feuilletemps', ondelete='cascade', string="feuille")

    date_id = fields.Many2one('tbrh.date', ondelete='cascade', string="ID Date")
    date = fields.Date(RELATED='tbrh.absences;date_id.date_jour;', store=True, use_parent_address=False)

    statut = fields.Selection([('absent', 'Absent'), ('present', 'Présent')], string="Statut", required='true')
    motif = fields.Many2one('tbrh.motifs_absences',
                            ondelete='cascade', string="Motif d'absence")
    h_arrive = fields.Float(help="H arrivé", default="09")
    h_sortie = fields.Float(help="H sortie", default="17")
    current_day = fields.Date(default=fields.Date.today, store=True)
    nbr_h_absence = fields.Float(help="nbr h absence", compute='_calc_heure_absence', store=True)
    nbr_h_supp = fields.Float(help="nbr h supplémentaire", compute='_calc_heure_absence', store=True)

    @api.one
    @api.constrains('date', 'current_day')
    def _check_description(self):
        if self.current_day < self.date:
            raise ValidationError("DATE INVALIDE : Veuillez saisir une autre date jour")

    @api.onchange('statut', 'h_arrive', 'h_sortie')
    def _verify_hour_entree_sortie(self):
        for r in self:
            if r.statut == 'present':
                if r.h_sortie == 0 or r.h_arrive == 0:
                    return {
                        'warning': {
                            'title': "Incorrect 'h_arrive' or 'h_sortie'  value",
                            'message': "verifiez l'heure d'entrée et  sortie saisie ou changez le statut à absent !",
                        },
                    }
                if r.h_arrive < 9:
                    return {
                        'warning': {
                            'title': "Incorrect 'h_arrive' value",
                            'message': "verifiez l'heure d'arriver saisie",
                        },
                    }

    var = 0

    @api.depends('statut', 'h_arrive', 'h_sortie', 'motif')
    def _calc_heure_absence(self):
        for r in self:
            if r.statut == 'present':
                var = r.h_sortie - r.h_arrive
                if var == 8:
                    r.nbr_h_absence = 0
                    r.nbr_h_supp = var - 8
                elif var != 8:
                    if var < 8:
                        r.nbr_h_absence = 8 - var
                        r.nbr_h_supp = 0
                    elif var > 8:
                        r.nbr_h_absence = 0
                        r.nbr_h_supp = var - 8

            elif r.statut == 'absent':
                r.nbr_h_absence = 8
                r.h_sortie = 0
                r.h_arrive = 0
                r.nbr_h_supp = 0
