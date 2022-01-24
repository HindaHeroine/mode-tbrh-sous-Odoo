# coding=utf-8
from openerp import models, fields, api, exceptions


class Motifs_absences(models.Model):
    _name = 'tbrh.motifs_absences'

    name = fields.Char(string="Titre", required=True)
    description = fields.Text(string="Description")

    @api.multi
    def copy(self, default=None):
        default = dict(default or {})

        copied_count = self.search_count(
            [('name', '=like', u"Copy of {}%".format(self.name))])
        if not copied_count:
            new_name = u"Copy of {}".format(self.name)
        else:
            new_name = u"Copy of {} ({})".format(self.name, copied_count)

        default['name'] = new_name
        return super(Motifs_absences, self).copy(default)

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "le titre de motif d'absence ne doit pas etre sa description"),

        ('name_unique',
         'UNIQUE(name)',
         "Le titre de motif d'absence exist déja "),
    ]
