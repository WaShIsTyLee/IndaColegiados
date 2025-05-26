from odoo import models, fields

class ContratoFarmacia(models.Model):
    _name = 'colegiado.contrato.farmacia'
    _description = 'Contratos en Farmacias'

    colegiado_id = fields.Many2one('colegiado', string='Colegiado', ondelete='cascade')
    nombre_farmacia = fields.Char(string='Nombre de la Farmacia')
    desde = fields.Date(string='Desde')
    hasta = fields.Date(string='Hasta')
    ejerce_como = fields.Text(string='Ejerce Como')
