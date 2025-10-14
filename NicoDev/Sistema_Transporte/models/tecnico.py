from odoo import models, fields

class Tecnico(models.Model):
    _name = 'gestion.tecnico'
    _description = "Técnicos disponibles"

    name = fields.Char(string="Nombre del técnico", required=True)
    especialidad = fields.Char(string="Especialidad")
    telefono = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo electrónico")
