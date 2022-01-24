# coding=utf-8
from openerp import models, fields


class Date(models.Model):
    _name = 'tbrh.date'

    date_jour = fields.Date(default=fields.Date.today, store=True)
    day_line = fields.One2many('tbrh.abscences', 'date_id', string=' Id dayline')

    # for many2any relation
    # dayline_id = fields.many2many('tbrh.abscences', id1='date_jour', id2='statut', relation='date_dayline_relation')

    _sql_constraints = [
        ('date_uniq', 'UNIQUE(date_jour)', 'Date de jour déja pointée!')

    ]
