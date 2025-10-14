from odoo import models, fields

class Destino(models.Model):
    _name = 'gestion.destino'
    _description = 'Destino'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
