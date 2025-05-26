{
    'name': 'Colegios - Contactos Personalizados',
    'version': '1.0',
    'summary': 'Gestión de colegiados con sincronización a contactos',
    'description': 'Módulo que permite gestionar colegiados y crea automáticamente un contacto en res.partner.',
    'author': 'Juan Jesús López Solano / Inda Group S.L',
    'category': 'Custom',
    'depends': ['base', 'contacts', 'web', 'documents'],  
    'data': [
        'security/ir.model.access.csv',
        'reports/ir_actions_report.xml',     
        'reports/product_report.xml',
        'views/contacts_view.xml'
        
    ],

    'installable': True,
    'application': True,
    'icon': "colegiados_inda/static/description/icono.png"

}
