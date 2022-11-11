from odoo import models, fields, api

class Vehicle(models.Model):
    _name = "vehicle"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Mantenimiento de vehiculos"

    tipo_vehiculo = fields.Selection([
        ('50 pasajeros', '50 Pasajeros'),
        ('30 pasajeros', '30 Pasajeros'),
        ('15 pasajeros', '15 Pasajeros'),
        ('5 pasajeros', '5 Pasajeros'),
    ], string = 'Cantidad de pasajeros', default='other', tracking=True, required = True)
    brand = fields.Char(string = "Marca", required = True)
    car_model = fields.Char(string = "Modelo", required = True)
    year = fields.Date(string = "Año", required = True)
    plate_number = fields.Char(string = "Placa", required = True)
    image = fields.Binary(string = "Imagen")
    state = fields.Selection([
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
    ], string='States', required=True, readonly=True, copy=False,
    tracking=True, default='disponible')
    
    def button_disponible(self):
        self.state = 'disponible'
        
    def button_reservado(self):
        self.state = 'reservado'