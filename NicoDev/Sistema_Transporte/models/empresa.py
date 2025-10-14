from odoo import models, fields

class Empresa(models.Model):
    _name = 'gestion.empresa'
    _description = 'Empresa'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
    rubro = fields.Char(string='Rubro')  # <-- agregamos este campo
