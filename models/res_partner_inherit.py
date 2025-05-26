from odoo import models, fields, api
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'

    image_128 = fields.Image("Imagen", max_width=128, max_height=128)

    def write(self, vals):
        res = super().write(vals)
        for partner in self:
            colegiado = self.env['colegiado'].search([('partner_id', '=', partner.id)], limit=1)
            if colegiado:
                cambios = {}
                if 'name' in vals and vals['name'] != colegiado.nombre:
                    cambios['nombre'] = vals['name']
                if 'phone' in vals and vals['phone'] != colegiado.telefono:
                    cambios['telefono'] = vals['phone']
                if 'street' in vals and vals['street'] != colegiado.direccion:
                    cambios['direccion'] = vals['street']
                if 'mobile' in vals and vals['mobile'] != colegiado.movil:
                    cambios['movil'] = vals['mobile']
                if 'street2' in vals and vals['street2'] != colegiado.calle2:
                    cambios['calle2'] = vals['street2']
                if 'zip' in vals and vals['zip'] != colegiado.codigo_postal:
                    cambios['codigo_postal'] = vals['zip']
                if 'city' in vals and vals['city'] != colegiado.ciudad:
                    cambios['ciudad'] = vals['city']
                if 'state_id' in vals and vals['state_id'] != colegiado.provincia.id:
                    cambios['provincia'] = vals['state_id']
                if 'country_id' in vals and vals['country_id'] != colegiado.pais.id:
                    cambios['pais'] = vals['country_id']
                if 'vat' in vals and vals['vat'] != colegiado.nif:
                    cambios['nif'] = vals['vat']
                if 'email' in vals and vals['email'] != colegiado.email:
                    cambios['email'] = vals['email']

                if cambios:
                    colegiado.write(cambios)
        return res

  #  def unlink(self):
  #      for partner in self:
  #          colegiado = self.env['colegiado'].search([('partner_id', '=', partner.id)], limit=1)
  #          if colegiado and not colegiado._context.get('unlinking', False):
  #              colegiado = colegiado.with_context(unlinking=True)
  #              colegiado.unlink()  
  #      return super().unlink()  

    def unlink(self):
        for partner in self:
            colegiado = self.env['colegiado'].search([('partner_id', '=', partner.id)], limit=1)
            # Solo lanzamos error si NO venimos desde el unlink del modelo colegiado
            if colegiado and not self.env.context.get('force_unlink_from_colegiado', False):
                raise UserError("No puedes eliminar este contacto porque está vinculado a un colegiado.")
        return super().unlink()

