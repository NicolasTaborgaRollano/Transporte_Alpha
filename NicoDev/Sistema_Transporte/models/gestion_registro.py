from odoo import models, fields, api

class GestionRegistro(models.Model):
    _name = 'gestion.registro'
    _description = 'Gestión de Registro'

    # Campo name obligatorio para Odoo
    name = fields.Char(string='Nombre completo', compute='_compute_name', store=True)

    # Datos personales
    nombre = fields.Char(string='Nombre', required=True)
    apellido_paterno = fields.Char(string='Apellido Paterno', required=True)
    password = fields.Char(string='Contraseña')

    # Datos del registro
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today)
    hora = fields.Float(string='Hora')  # o fields.Datetime si quieres fecha+hora
    numero_informe = fields.Char(string='Número de Informe')
    cantidad_bs = fields.Monetary(string='Cantidad en Bs', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Moneda', default=lambda self: self.env.ref('base.BOB'))

    # Relaciones
    destino_id = fields.Many2one('gestion.destino', string='Destino')
    tecnico_id = fields.Many2one('gestion.tecnico', string='Técnico')
    departamento_id = fields.Many2one('gestion.departamento', string='Departamento')
    empresa_id = fields.Many2one('gestion.empresa', string='Empresa')
    tipo_reporte_id = fields.Many2one('gestion.tipo_reporte', string='Tipo de Reporte')

    # Persona que llamó
    persona_que_llamo = fields.Char(string='Persona que llamó')

    # Computed field para name
    @api.depends('nombre', 'apellido_paterno')
    def _compute_name(self):
        for record in self:
            record.name = (record.nombre or '') + ' ' + (record.apellido_paterno or '')
