{
    'name': "Gestión de Transporte",
    'summary': "Módulo para gestionar reportes, técnicos, destinos, registros y empresas",
    'description': """
        Gestión de Transporte
        ===================
        Permite administrar destinos, técnicos, departamentos, empresas, tipos de reporte
        y la creación de gestiones de registro y reportes de manera centralizada.
    """,
    'version': "18.0.0.1",
    'author': "Nicolas Taborga",
    'category': "Tools",
    'website': "https://www.alphasys.com.bo/es_BO",
    'license': "AGPL-3",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/destino_views.xml',
        'views/tecnico_views.xml',
        'views/departamento_views.xml',
        'views/empresa_views.xml',
        'views/tipo_reporte_views.xml',
        'views/gestion_registro_views.xml',
        'views/gestion_reporte_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
