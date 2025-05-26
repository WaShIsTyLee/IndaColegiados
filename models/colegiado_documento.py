# models/colegiado_documento.py
from odoo import models, fields, api

class ColegiadoDocumento(models.Model):
    _name = 'colegiado.documento'
    _description = 'Documentos PDF de Colegiado'

    colegiado_id = fields.Many2one('colegiado', string='Colegiado', required=True, ondelete='cascade')
    documento = fields.Binary(string='Archivo PDF', required=True)
    nombre = fields.Char(string='Nombre del Documento')
    fecha = fields.Date(string='Fecha')
    tamaño = fields.Integer(string='Tamaño (KB)', compute='_compute_tamano', store=True)

    @api.depends('documento')
    def _compute_tamano(self):
        for rec in self:
            rec.tamaño = len(rec.documento or b'') // 1024
