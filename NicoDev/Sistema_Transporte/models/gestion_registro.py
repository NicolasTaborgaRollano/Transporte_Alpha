from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime

class GestionRegistro(models.Model):
    _name = 'gestion.registro'
    _description = 'Gestión de Registro de Transporte'

    # Nombre del registro para mostrar en Odoo
    name = fields.Char(string='Nombre del registro', compute='_compute_name', store=True)

    # Datos del solicitante
    persona_que_llamo = fields.Char(string='Persona que llamó', required=True)
    nombre = fields.Char(string='Nombre', required=True)
    apellido_paterno = fields.Char(string='Apellido Paterno', required=True)
    password = fields.Char(string='Password', password=True)

    # Fecha y hora
    fecha = fields.Date(string='Fecha', default=fields.Date.context_today)
    hora = fields.Char(string='Hora', default=lambda self: datetime.now().strftime('%H:%M:%S'))

    # Relaciones
    destino_id = fields.Many2one('gestion.destino', string='Destino', required=True)
    tecnico_id = fields.Many2one('res.partner', string='Técnico', domain="[('is_company','=',False)]")
    departamento_id = fields.Many2one('hr.department', string='Departamento')
    empresa_id = fields.Many2one('res.partner', string='Empresa Cliente', domain="[('is_company','=',True)]")
    tipo_reporte_id = fields.Many2one('gestion.tipo_reporte', string='Tipo de Reporte')

    # Informe y finanzas
    numero_informe = fields.Char(string='N° Informe')
    cantidad_bs = fields.Float(string='Monto (Bs)', default=0.0)
    facturable = fields.Boolean(string='Facturable', default=False)
    observaciones = fields.Text(string='Observaciones')

    # Líneas de transporte
    lineas_transporte = fields.One2many('gestion.registro.linea', 'registro_id', string='Planilla de uso de transporte')

    @api.depends('nombre', 'apellido_paterno', 'numero_informe')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.nombre or ''} {record.apellido_paterno or ''} - {record.numero_informe or ''}".strip()


class GestionRegistroLinea(models.Model):
    _name = 'gestion.registro.linea'
    _description = 'Línea de Planilla de Transporte'

    registro_id = fields.Many2one('gestion.registro', string='Registro principal', ondelete='cascade')
    tecnico_id = fields.Many2one('gestion.tecnico', string='Técnico')
    destino_id = fields.Many2one('gestion.destino', string='Destino')
    vuelta = fields.Integer(string='Vuelta', default=1)
    bs = fields.Float(string='Bs.', default=0.0)
    firma = fields.Char(string='Firma')
    salida = fields.Char(string='Salida (Hora)')
    cliente = fields.Char(string='Cliente')
    informe = fields.Char(string='Informe')
    detalle = fields.Char(string='Detalle')

    @api.constrains('bs', 'vuelta')
    def _check_positive_values(self):
        for record in self:
            if record.bs < 0 or record.vuelta < 0:
                raise ValidationError("Los valores numéricos no pueden ser negativos.")
