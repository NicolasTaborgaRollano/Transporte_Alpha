from odoo import models, fields

class Departamento(models.Model):
    _inherit = 'hr.department'  # Podemos usar los departamentos existentes
    _description = 'Departamento extendido'

    descripcion = fields.Text(string='Descripción adicional')
