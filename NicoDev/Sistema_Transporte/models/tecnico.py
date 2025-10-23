from odoo import models, fields

class Tecnico(models.Model):
    _inherit = 'hr.employee'  # Heredamos de empleados
    _description = "Técnico"

    especialidad = fields.Char(string="Especialidad")
    telefono = fields.Char(string="Teléfono", related='work_phone', store=True)
    email = fields.Char(string="Correo electrónico", related='work_email', store=True)
