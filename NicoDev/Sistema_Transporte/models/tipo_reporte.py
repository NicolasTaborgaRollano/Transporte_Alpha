from odoo import models, fields

class TipoReporte(models.Model):
    _name = 'gestion.tipo_reporte'
    _description = 'Tipo de Reporte'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
