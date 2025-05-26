from odoo import models, fields, api
from odoo.exceptions import UserError

class Colegiado(models.Model):
    _name = 'colegiado'
    _description = 'Colegios Colegiados'

    contacto_id = fields.Many2one('res.partner', string='Contacto')
    direccion = fields.Char(string='Calle')
    partner_id = fields.Many2one('res.partner', string='Contacto Relacionado', readonly=True)
    calle2 = fields.Char(string='Calle 2')
    codigo_postal = fields.Char(string='Código Postal')
    ciudad = fields.Char(string='Ciudad')
    provincia = fields.Many2one('res.country.state', string='Provincia')
    pais = fields.Many2one('res.country', string='País')
    direccion_ids = fields.One2many(
    'colegiado.direccion',  # modelo relacionado
    'colegiado_id',         # campo many2one en direccion que apunta a colegiado
    string='Direcciones'
)
    documento_odoo_count = fields.Integer(
        string='Documentos Odoo',
        compute='_compute_documento_odoo_count',
        store=False  # No es necesario almacenarlo
    )
    documento_entrada_salida_count = fields.Integer(
    string='Documentos Entrada/Salida',
    compute='_compute_documento_entrada_salida_count',
    store=False
)

    @api.depends('partner_id')
    def _compute_documento_entrada_salida_count(self):
        Documento = self.env['registro.documento']
        for record in self:
            if record.partner_id:
                record.documento_entrada_salida_count = Documento.search_count([
                    ('contacto_id', '=', record.partner_id.id)
                ])
            else:
                record.documento_entrada_salida_count = 0



    
    #Documentos
    documento_ids = fields.One2many('colegiado.documento', 'colegiado_id', string='Documentos')
    procesos_ids = fields.One2many('colegiado.procesos', 'colegiado_id', string='Procesos')

    
    #Datos Academicos
    fecha_titulo = fields.Date(string='Fecha Titulo')
    numero_registro = fields.Char(string='Numero Registro')
    numero_folio = fields.Char(string='Numero Folio')
    universidad = fields.Char(string='Universidad')
    otros_titulos=fields.Text(string='Otros Titulos y Cursos')
    observaciones_academicas = fields.Text(string='Observaciones Academicas')
    titulo_universitario = fields.Binary(string='Título Universitario')
    titulo_ids = fields.One2many('colegiado.titulo', 'colegiado_id', string='Títulos Adicionales')


    
    #Datos Personales
    telefono = fields.Char(string='Teléfono')
    movil = fields.Char(string='Móvil')
    email = fields.Char(string='Email')
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    sexo = fields.Selection([
                ('masculino', 'Masculino'),
                ('femenino', 'Femenino'),
                ('otro', 'Otro'),
            ], string='Sexo')
    
    #Datos Generales
    nombre = fields.Char(string='Nombre y Apellidos', required=True)
    nif = fields.Char(string='NIF')
    estado = fields.Selection([
        ('alta', 'Alta'),
        ('baja', 'Baja')
    ], string='Estado', default='alta')
    modalidad = fields.Selection([
            ('ejerciente', 'Ejerciente'),
            ('desempleado', 'Desempleado')
        ], string='Modalidad', default='ejerciente')
    N1Colegiado = fields.Char(string='Número Colegiado', required=True)
    observaciones = fields.Text(string='Observaciones')
    
    #Datos Colegiado
    fecha_colegiacion = fields.Date(string='Fecha colegiación')
    es_perito = fields.Boolean(string='Perito Judicial')
    es_bolsa_trabajo = fields.Boolean(string='Bolsa Trabajo')
    otro_colegio=fields.Char(string='Otro Colegio')
    #Contratos en farmacias
    contrato_ids = fields.One2many('colegiado.contrato.farmacia', 'colegiado_id', string='Contratos en Farmacias')
      

    #Ejercicio Laboral
    adjunto=fields.Boolean(string="Adjunto")
    sustituto=fields.Boolean(string="Sustituto")
    administraciones_publicas=fields.Boolean(string="Administraciones Publicas")
    analista=fields.Boolean(string="Analista")
    cotitular=fields.Boolean(string="Cotitular")
    distribucion=fields.Boolean(string="Distribución")
    docencia=fields.Boolean(string="Docencia")
    industria=fields.Boolean(string="Industria")
    hospital=fields.Boolean(string="Hospital")
    optico=fields.Boolean(string="Óptico")
    ortopedia=fields.Boolean(string="Órtopedia")
    titular=fields.Boolean(string="Titular")
    otras_actividades=fields.Boolean(string="Otras Actividades")
    regente=fields.Boolean(string="Regente")
    facultativo=fields.Boolean(string="Facultativo")
    #Vocalias
    dermofarmacia=fields.Boolean(string="Dermofarmacia")
    oficina_farmacia=fields.Boolean(string="Oficina Farmacia")
    ortopedia=fields.Boolean(string="Ortopedia")
    alimentacion=fields.Boolean(string="Alimentacion")
    doc_investigacion=fields.Boolean(string="Doc. Investigación")
    optica=fields.Boolean(string="Óptica")
    analisis=fields.Boolean(string="Analisis")
    admin_publica=fields.Boolean(string="Admin Pulicas")
    hospital=fields.Boolean(string="Hospital")
    distribucion=fields.Boolean(string="Distribución")
    industria=fields.Boolean(string="Industria")
    formulacion_magistral=fields.Boolean(string="Formulación Magistral")
    
    # --------
    # estado = fields.Selection([
    #    ('alta', 'Alta'),
    #    ('baja', 'Baja')
    # --------
    

    @api.depends('partner_id')
    def _compute_documento_odoo_count(self):
        Document = self.env['documents.document']
        for record in self:
            if record.partner_id:
                record.documento_odoo_count = Document.search_count([
                    '|',
                    '&', ('res_model', '=', 'res.partner'), ('res_id', '=', record.partner_id.id),
                    ('partner_id', '=', record.partner_id.id)
                ])
            else:
                record.documento_odoo_count = 0
                
    @api.model
    def create(self, vals):
        partner = self.env['res.partner'].create({
            'name': vals.get('nombre'),
            'phone': vals.get('telefono'),
            'mobile': vals.get('movil'),
            'street': vals.get('direccion'),
            'street2': vals.get('calle2'),
            'zip': vals.get('codigo_postal'),
            'city': vals.get('ciudad'),
            'state_id': vals.get('provincia'),
            'country_id': vals.get('pais'),
            'vat': vals.get('nif'),
            'email': vals.get('email'),
        })
        vals['partner_id'] = partner.id
        return super(Colegiado, self).create(vals)

    def write(self, vals):
        for rec in self:
            partner_vals = {}
            if 'nombre' in vals and vals['nombre'] != rec.partner_id.name:
                partner_vals['name'] = vals['nombre']
            if 'telefono' in vals and vals['telefono'] != rec.partner_id.phone:
                partner_vals['phone'] = vals['telefono']
            if 'movil' in vals and vals['movil'] != rec.partner_id.mobile:
                partner_vals['mobile'] = vals['movil']
            if 'direccion' in vals and vals['direccion'] != rec.partner_id.street:
                partner_vals['street'] = vals['direccion']
            if 'calle2' in vals and vals['calle2'] != rec.partner_id.street2:
                partner_vals['street2'] = vals['calle2']
            if 'codigo_postal' in vals and vals['codigo_postal'] != rec.partner_id.zip:
                partner_vals['zip'] = vals['codigo_postal']
            if 'ciudad' in vals and vals['ciudad'] != rec.partner_id.city:
                partner_vals['city'] = vals['ciudad']
            if 'provincia' in vals and vals['provincia'] != rec.partner_id.state_id.id:
                partner_vals['state_id'] = vals['provincia']
            if 'pais' in vals and vals['pais'] != rec.partner_id.country_id.id:
                partner_vals['country_id'] = vals['pais']
            if 'nif' in vals and vals['nif'] != rec.partner_id.vat:
                partner_vals['vat'] = vals['nif']
            if 'email' in vals and vals['email'] != rec.partner_id.email:
                partner_vals['email'] = vals['email']

            if partner_vals and rec.partner_id:
                rec.partner_id.write(partner_vals)

        return super().write(vals)

    def unlink(self):
        for rec in self:
            if rec.partner_id:
                # Muy importante: forzamos el contexto aquí
                rec.partner_id.with_context(force_unlink_from_colegiado=True).unlink()
        return super(Colegiado, self).unlink()


    def action_print_colegiado_pdf(self):
        return self.env.ref('colegiados_inda.report_colegiado_pdf_action').report_action(self)
    
    def open_documentos_asociados(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Documentos Asociados',
            'res_model': 'registro.documento',
            'view_mode': 'tree,form',
            'domain': [('contacto_id', '=', self.partner_id.id)],
        }
            
    def action_open_odoo_documents(self):
        self.ensure_one()
        if not self.partner_id:
            raise UserError("Este colegiado no tiene un contacto asociado.")
        return {
            'type': 'ir.actions.act_window',
            'name': 'Documentos Odoo',
            'res_model': 'documents.document',
            'view_mode': 'tree,form',
            'domain': [
                '|',
                '&', ('res_model', '=', 'res.partner'), ('res_id', '=', self.partner_id.id),
                ('partner_id', '=', self.partner_id.id)
            ],
            'context': {
                'default_res_model': 'res.partner',
                'default_res_id': self.partner_id.id,
                'default_partner_id': self.partner_id.id,
            }
        }






