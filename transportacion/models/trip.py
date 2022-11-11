from odoo import models, fields, api

class Trip(models.Model):
    _name = "trip"
    _inherit = ['mail.thread','mail.activity.mixin']
    
    destination = fields.Char(string='Destino', required=True, tracking=True)
    calle = fields.Char(string='Calle')
    ciudad = fields.Char(string='Ciudad')
    pais = fields.Many2one(field='country_id', comodel_name='res.country', string='Pais', required=True)
    provincia = fields.Many2one(field='country_id.name', comodel_name='res.country.state', string='Provincia', required=True)
    description = fields.Char(string='Motivo', required=True)
    datetime1 = fields.Datetime(string='Fecha y hora de salida', required=True, tracking=True)
    datetime2 = fields.Datetime(string='Fecha y hora llegada', required=True, tracking=True)
    pickup_location = fields.Char(string='Punto de encuentro', required=True, tracking=True)
    department_id = fields.Many2one(field='name', comodel_name='hr.department', string='Departamento', required=True)
    driver_id = fields.Many2one(comodel_name='hr.employee', string="Chofer")
    cantidad_pasajeros = fields.Char(string="Cantidad de pasajeros", required=True)  
    state = fields.Selection(selection=[
        ('draft', 'Borrador'),
        ('enviado', 'Enviado'),
        ('in_progress', 'En Progreso'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
        ('cancel', 'Cancelado'),
    ], string='Status', required=True, readonly=True, copy=False,
    tracking=True, default='draft')
    
    def button_send(self):
       self.write({
           'state': "enviado"
       })
    
    