# ordenproduccion

## Descripción

**ordenproduccion** es una aplicación en Python que permite gestionar órdenes de producción de la imprenta copimanta utilizando una base de datos MongoDB. La aplicación facilita el registro, consulta del gerente , modificación y anulación de órdenes de producción de manera sencilla desde la terminal.

## Características

- Conexión automática a MongoDB.
- Registro de nuevas órdenes de producción.
- Listado de todas las órdenes almacenadas.
- Modificación y anulación de órdenes existentes.
- Interfaz interactiva por consola.

## Requisitos

- Python 3.x
- [pymongo](https://pypi.org/project/pymongo/)
- MongoDB en ejecución (localhost:27017)

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tuusuario/ordenproduccion.git
   cd ordenproduccion
   ```

2. Instala las dependencias:
   ```bash
   pip install pymongo
   ```

3. Asegúrate de que MongoDB esté corriendo en tu máquina:
   ```bash
   sudo systemctl start mongod
   ```

## Uso

Ejecuta la aplicación principal:
```bash
python mongo.py
```

Sigue las instrucciones en pantalla para agregar, listar, modificar o anular órdenes de producción.

## Estructura de la base de datos

Cada orden contiene los siguientes campos:
- `razon_social`
- `ruc`
- `fecha`
- `descripcion_trabajo`
- `cantidad`
- `precio_total`
- `estado`

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para sugerencias o mejoras.