from odoo import models, fields

class TituloUniversitario(models.Model):
    _name = 'colegiado.titulo'
    _description = 'Títulos Universitarios Adicionales'

    colegiado_id = fields.Many2one('colegiado', string='Colegíado', required=True, ondelete='cascade')
    titulo = fields.Char(string='Título', required=True)
    universidad = fields.Char(string='Universidad')
    fecha = fields.Date(string='Fecha Obtención')
    observaciones = fields.Text(string='Observaciones')

    archivo_titulo = fields.Binary(string='Archivo')
    archivo_nombre = fields.Char(string='Nombre del Archivo')
