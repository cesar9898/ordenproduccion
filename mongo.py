from pymongo import MongoClient

class Orden_Produccion:
    def __init__(self, razon_social, ruc, fecha, descripcion_trabajo, cantidad, precio_total, estado):
        self.razon_social = razon_social
        self.ruc = ruc
        self.fecha = fecha
        self.descripcion_trabajo = descripcion_trabajo
        self.cantidad = cantidad
        self.precio_total = precio_total
        self.estado = estado            

def connect_to_mongo():
    """
    este metodo conecta a Mongo.
    """
    
    client = MongoClient('mongodb://localhost:27017/')
    db = client ['ordenesproduccion']
    return db ['ordenes']
     

def add_orden(collection):
    print("\nagregar orden")
    razon_social = input('ingrese razon social: ')
    ruc = input('ingrese numero de orden: ')
    fecha = input('ingrese fecha: ')
    descripcion_trabajo = input('ingrese descripcion: ')
    cantidad = input('ingrese cantidad: ')
    precio_total = input('ingrese precio total: ')
    estado = input('ingrese estado: ')  

    orden_produccion = { 
        'razon_social': razon_social,
        'ruc': ruc,
        'fecha': fecha,
        'descripcion_trabajo': descripcion_trabajo,
        'cantidad': cantidad,
        'precio_total': precio_total,
        'estado': estado
    }
    
    collection.insert_one(orden_produccion)
    print("\nOrden agregada exitosamente.")




    
    """
    este metodo agrega una orden a la base de datos.
    """
    collection.insert_one(orden_produccion)
    print("ordenes")


def list_users():
    print("\nlista ordenes de produccion: ")
    orden_produccion = collection.find()
    for orden in orden_produccion:
        print(f"Razon Social: {orden['razon_social']}, RUC: {orden['ruc']}, Fecha: {orden['fecha']}, "
              f"Descripcion: {orden['descripcion_trabajo']}, Cantidad: {orden['cantidad']}, "
              f"Precio Total: {orden['precio_total']}, Estado: {orden['estado']}") 


def main():
    collection = connect_to_mongo()
    """
    este metodo lista las ordenes de la base de datos.
    """
    
    while True:
        print('orden de produccion')
        print('1. agregar orden')
        print('2. listar ordenes')
        print('3. modificar orden')
        print('4. anular orden')
        print('5. salir')

        opcion = input('ingrese una opcion:  ')  
        if opcion == '1':
            add_user(collection)
        elif opcion == '2':     
            list_users()
        elif opcion == '3':
            modify_user()
        elif opcion == '4':
            delete_user()
        elif opcion == '5':
            print('saliendo de ordenes de produccion')
            break
        else:
            print('opcion no valida, intente nuevamente')


if __name__ == '__main__':  
    main()