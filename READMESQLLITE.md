# ordenproduccionSQLLITE

## Descripción

**ordenproduccion** es una aplicación en Python que permite gestionar órdenes de producción utilizando una base de datos SQLite. La aplicación facilita el registro, consulta, actualización y eliminación de órdenes de producción de manera sencilla desde la terminal.

## Características

- Conexión automática a SQLite.
- Registro de nuevas órdenes de producción.
- Listado de todas las órdenes almacenadas.
- Búsqueda de órdenes por RUC.
- Modificación y eliminación de órdenes existentes.
- Ejemplo de uso de todas las operaciones CRUD.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/ordenproduccion.git
   cd ordenproduccion
   ```

2. No se requieren dependencias externas, solo Python estándar.

## Uso

Ejecuta la aplicación principal:
```bash
python ordenproduccion/sqllite.py
```

El script realiza las siguientes operaciones:
- Crea la tabla si no existe.
- Limpia la tabla antes de insertar datos de prueba.
- Inserta varias órdenes de ejemplo.
- Lista todas las órdenes.
- Busca una orden por RUC.
- Actualiza el estado de una orden.
- Elimina una orden.
- Muestra el estado de la base de datos tras cada operación.

## Estructura de la base de datos

Cada orden contiene los siguientes campos:
- `ruc` (clave primaria)
- `fecha`
- `razon_social`
- `descripcion_trabajo`
- `cantidad`
- `precio_total`
- `estado`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerencias o mejoras.

## Licencia

Este proyecto está bajo la licencia MIT.