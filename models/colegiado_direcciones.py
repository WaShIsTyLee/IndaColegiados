from odoo import models, fields, api


class ColegiadoDireccion(models.Model):
    _name = 'colegiado.direccion'
    _description = 'Dirección de Colegiado'

    direccion = fields.Char(string='Dirección')
    calle2 = fields.Char(string='Calle 2')
    codigo_postal = fields.Char(string='Código Postal')
    ciudad = fields.Char(string='Ciudad')
    provincia = fields.Many2one('res.country.state', string='Provincia')
    pais = fields.Many2one('res.country', string='País')
    colegiado_id = fields.Many2one('colegiado', string='Colegiado', ondelete='cascade')

    # NUEVOS CAMPOS:
    es_correspondencia = fields.Boolean(string='Dirección de correspondencia')
    es_fiscal = fields.Boolean(string='Dirección fiscal')
    tipo_direccion = fields.Selection([
    ('personal', 'Personal'),
    ('profesional', 'Profesional'),
], string='Tipo de Dirección')



    @api.model
    def create(self, vals):
        direccion = super().create(vals)
        colegiado = direccion.colegiado_id

        if colegiado and len(colegiado.direccion_ids) == 1 and colegiado.partner_id:
            # Solo si esta es la primera dirección
            colegiado.partner_id.write({
                'street': direccion.direccion,
                'street2': direccion.calle2,
                'zip': direccion.codigo_postal,
                'city': direccion.ciudad,
                'state_id': direccion.provincia.id if direccion.provincia else False,
                'country_id': direccion.pais.id if direccion.pais else False,
            })
        return direccion
    
    def unlink(self):
        for direccion in self:
            colegiado = direccion.colegiado_id
            partner = colegiado.partner_id

            # Verificamos si esta dirección es la primera (la que está en contactos)
            if (
                partner and
                partner.street == direccion.direccion and
                partner.street2 == direccion.calle2 and
                partner.zip == direccion.codigo_postal and
                partner.city == direccion.ciudad and
                (partner.state_id.id if partner.state_id else False) == (direccion.provincia.id if direccion.provincia else False) and
                (partner.country_id.id if partner.country_id else False) == (direccion.pais.id if direccion.pais else False)
            ):
                # La dirección eliminada es la que está en res.partner → limpiamos o reemplazamos
                otras_direcciones = colegiado.direccion_ids - direccion  # quitamos la que se va a borrar
                if otras_direcciones:
                    nueva = otras_direcciones[0]  # usamos la siguiente
                    partner.write({
                        'street': nueva.direccion,
                        'street2': nueva.calle2,
                        'zip': nueva.codigo_postal,
                        'city': nueva.ciudad,
                        'state_id': nueva.provincia.id if nueva.provincia else False,
                        'country_id': nueva.pais.id if nueva.pais else False,
                    })
                else:
                    # No hay más direcciones, limpiamos
                    partner.write({
                        'street': False,
                        'street2': False,
                        'zip': False,
                        'city': False,
                        'state_id': False,
                        'country_id': False,
                    })

        return super().unlink()
