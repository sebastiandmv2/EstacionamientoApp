# Sistema de Gestión de Estacionamientos

## Introducción
Este proyecto ofrece una plataforma para la gestión de estacionamientos, permitiendo a usuarios registrados buscar, reservar y administrar estacionamientos disponibles en una determinada área.

## Acceso
### Usuarios Registrados
**Usuario Cliente:**
- **Usuario:** seba
- **Contraseña:** Elefante1234

**Usuario Dueño:**
- **Usuario:** nico
- **Contraseña:** Elefante1234

## Funcionalidades
### Inicio de Sesión y Registro
- **Login:** Ingresar con credenciales de usuario para acceder al sistema.
- **Registro de dos tipos de usuario:** Usuarios Cliente y Usuarios Dueños pueden registrarse y acceder a las funcionalidades correspondientes a su rol.

### Funcionalidades para Dueños de Estacionamientos
- **Crear Estacionamiento:** Los dueños pueden registrar nuevos estacionamientos indicando dirección, tamaño y costos.
- **Habilitar / Deshabilitar Estacionamiento:** Gestión del estado de disponibilidad de los estacionamientos.
- **Eliminar Estacionamiento:** Eliminar estacionamientos de la plataforma.

### Funcionalidades para Clientes y Dueños
- **Buscar Estacionamientos Disponibles:** Buscar estacionamientos disponibles en una ubicación específica.
- **Visualizar en Mapa:** Ver la ubicación de los estacionamientos disponibles en un mapa interactivo.
- **Street View de Google:** Acceso a Street View para obtener una mejor vista de la ubicación.
- **Reservar Estacionamiento:** Los usuarios pueden reservar estacionamientos disponibles.
- **Ver Registro de Estacionamientos Reservados:** Historial de estacionamientos reservados por el usuario.

## Configuración del Proyecto
Para ejecutar este proyecto localmente, sigue estos pasos:
1. Clona este repositorio
2. Instala las dependencias: `pip install -r requirements.txt`
3. Configura la base de datos: `python manage.py migrate`
4. Inicia el servidor: `python manage.py runserver`
5. Accede al sistema desde tu navegador: `http://localhost:8000/`
