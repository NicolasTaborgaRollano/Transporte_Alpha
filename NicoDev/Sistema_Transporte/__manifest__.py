{
    'name': "Gestión de Transporte",
    'summary': "Módulo para gestionar registros, técnicos, destinos y departamentos",
    'description': """
        Gestión de Transporte
        ===================
        Permite administrar destinos, técnicos, departamentos y la creación de registros
        integrados con empleados y clientes del sistema.
    """,
    'version': "18.0.0.2",
    'author': "Nicolas Taborga",
    'category': "Tools",
    'website': "https://www.alphasys.com.bo/es_BO",
    'license': "AGPL-3",
    'depends': ['base', 'hr', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/destino_views.xml',
        'views/tecnico_views.xml',
        'views/departamento_views.xml',
        'views/gestion_registro_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
