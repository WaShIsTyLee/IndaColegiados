IndaColegiados
IndaColegiados es un módulo personalizado para Odoo que permite gestionar la información de colegiados, incluyendo datos personales, académicos, contratos en farmacias, documentos asociados y procesos relacionados, todo el modulo está relacionado con el modulo de Documentos Entrada Salida ademaás de con los modulos de Odoo: Documentos y Contactos.

📦 Características
Gestión completa de colegiados con campos personalizados.

Registro de direcciones, contratos en farmacias y procesos asociados.

Integración con documentos de Odoo y documentos externos.

Generación de informes PDF personalizados para cada colegiado.

Control de accesos mediante reglas de seguridad definidas.

**🛠️ Instalación
Clona este repositorio en tu carpeta de addons de Odoo:

git clone https://github.com/WaShIsTyLee/IndaColegiados.git
Reinicia el servidor de Odoo para que detecte el nuevo módulo.**

Activa el modo desarrollador en Odoo.

Ve a Aplicaciones, actualiza la lista de aplicaciones y busca IndaColegiados.

Instala el módulo.

🧩 Dependencias
Este módulo depende de los siguientes módulos de Odoo:

base

contacts

documents

Asegúrate de que estos módulos estén instalados antes de instalar IndaColegiados.

📁 Estructura del Repositorio
models/: Contiene los modelos de datos personalizados (colegiado, colegiado.direccion, etc.).

views/: Define las vistas y formularios para la interfaz de usuario.

reports/: Plantillas para la generación de informes PDF.

security/: Reglas de acceso y control de permisos.

static/description/: Archivos estáticos y descripción del módulo.

__manifest__.py: Archivo de manifiesto del módulo.

📄 Uso
Una vez instalado el módulo:

Accede al menú de Colegios Colegiados en Odoo.

Crea un nuevo colegiado y completa la información requerida.

Añade direcciones, contratos, documentos y procesos asociados según sea necesario.

Genera informes PDF personalizados desde la vista del colegiado.

🔒 Seguridad
El módulo define reglas de acceso específicas para garantizar que solo los usuarios autorizados puedan ver o modificar la información de los colegiados.

🧑‍💻 Autor
Nombre: [Juan Jesús López Solano]

Correo electrónico: [lopezsolanojuanjesus@gmail.com]

GitHub: https://github.com/WaShIsTyLee
