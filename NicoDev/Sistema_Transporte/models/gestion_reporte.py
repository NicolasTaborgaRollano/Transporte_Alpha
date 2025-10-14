from odoo import models, fields

class GestionReporte(models.Model):
    _name = 'gestion.reporte'
    _description = 'Gestión de Reportes'

    name = fields.Char(string='Título', required=True)
    descripcion = fields.Text(string='Descripción')
    fecha = fields.Datetime(string='Fecha', default=fields.Datetime.now)
    registro_id = fields.Many2one('gestion.registro', string='Registro')
    destino_id = fields.Many2one('gestion.destino', string='Destino')
    tecnico_id = fields.Many2one('gestion.tecnico', string='Técnico')
    empresa_id = fields.Many2one('gestion.empresa', string='Empresa')
    tipo_reporte_id = fields.Many2one('gestion.tipo_reporte', string='Tipo de Reporte')
