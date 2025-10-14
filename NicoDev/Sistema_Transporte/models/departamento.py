from odoo import models, fields

class Departamento(models.Model):
    _name = 'gestion.departamento'
    _description = 'Departamento'

    name = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')
