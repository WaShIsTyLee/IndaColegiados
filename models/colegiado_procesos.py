from odoo import models, fields, api

class ColegiadoProcesos(models.Model):
    _name = 'colegiado.procesos'
    _description = 'Documentos Procesos'

    colegiado_id = fields.Many2one('colegiado', string='Colegiado', required=True, ondelete='cascade')
    expediente = fields.Char(string='Expediente', required=True)
    denominacion = fields.Char(string='Denominación', required=True)
    asunto = fields.Text(string='Asunto')
    estado = fields.Selection([
        ('borrador', 'Borrador'),
        ('en_proceso', 'En proceso'),
        ('finalizado', 'Finalizado'),
    ], string='Estado', default='borrador')

    documento = fields.Binary(string='Archivo PDF', required=True, attachment=True)
    nombre = fields.Char(string='Nombre del Documento')  # Campo simple, no compute
    fecha = fields.Date(string='Fecha')
    tamaño = fields.Integer(string='Tamaño (KB)', compute='_compute_tamano', store=True)

    @api.depends('documento')
    def _compute_tamano(self):
        for rec in self:
            rec.tamaño = len(rec.documento or b'') // 1024
