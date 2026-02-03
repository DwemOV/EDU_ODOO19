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
        'views/actions.xml',
        'views/patient.xml',
        'views/visit.xml',
        'views/doctor.xml',
        'views/disease.xml',
        'data/disease.xml',
        'views/menu.xml',
    ],

    'demo': [
        'demo/doctor_demo.xml',
        'demo/patient_demo.xml',
    ],
    'application': True,
    'auto_install': False,
    'installable': True,
    'images': ['static/description/icon.jpg'],

}
