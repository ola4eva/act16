# -*- coding: utf-8 -*-
{
    'name': "Employee KPI",

    'summary': """
        Key Performance Indicators for Employees""",

    'description': """
        Key Performance Indicators for Employees
    """,

    'license': "LGPL-3",

    'author': "Olalekan Babawale",
    'website': "http://obabawale.github.io",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['hr'],

    'data': [
        'security/access_groups.xml',
        'security/ir.model.access.csv',
        'data/email_data.xml',
        'views/employee_kpi_template_views.xml',
        'views/employee_kpi_views.xml',
    ],
    'license': 'LGPL-3',
}
