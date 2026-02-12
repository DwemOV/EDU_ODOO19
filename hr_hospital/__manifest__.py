{
    'name': 'hr_hospital',
    'version': '19.0.1.0.1',
    'author': 'Oleh Sorokotiaha',
    "summary": "task2",
    'website': 'https://www.odoo.com',
    'category': 'HR',
    'license': 'OPL-1',
    'depends': [
        'base'
    ],
    'external_dependencies': {
        'python': []
    },

    'data': [
        'security/ir.model.access.csv',
        'views/actions_views.xml',
        'views/patient_views.xml',
        'views/visit_views.xml',
        'views/doctor_views.xml',
        'views/disease_views.xml',
        'data/disease_data.xml',
        'data/doctor_data.xml',
        'data/patient_data.xml',
        'views/menu_views.xml',
    ],

    # 'demo': [
    #     'demo/doctor_demo.xml',
    #     'demo/patient_demo.xml',
    # ],
    'application': True,
    'auto_install': False,
    'installable': True,
    'images': ['static/description/icon.jpg'],

}
