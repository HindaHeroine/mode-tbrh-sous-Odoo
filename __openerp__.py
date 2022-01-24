# -*- coding: utf-8 -*-
{
    'name': "tbrh",

    'summary': """Tableaux de bord et de reporting pour la destion des ressources humaines""",

    'description': """
       mazal la description n sah 
    """,

    'author': "goof company ",
    'website': "http://www.goof.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'hr_timesheet', 'hr_contract'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
        'views/employes.xml',
        'views/contract.xml',
        'views/Department.xml',
        'views/FeuilleTemps.xml',
        'views/motifs_abscences.xml',
        'views/employee_board.xml',
        'views/FeuilleTemps_board.xml',
        'views/Contract_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}