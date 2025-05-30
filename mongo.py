from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client['ordenesproduccion']
collection = db['ordenes']

lista = [
    {"razon_social": "indumaster", "ruc": "1390140858001", "telefono": "0987107295",
     "descripcion_trabajo": "flayers", "fecha_entrega": "2025-10-01",
     "cantidad": 5000, "precio_unitario": 0.5, "total": 500},   
    
    {"razon_social": "epespo", "ruc": "1709271514001", "telefono": "0936148523",
     "descripcion_trabajo": "rollup", "fecha_entrega": "2025-10-05",
     "cantidad": 5, "precio_unitario": 75, "total": 375},
    
    {"razon_social": "rav", "ruc": "157894269001", "telefono": "052689352",
     "descripcion_trabajo": "revistas", "fecha_entrega": "2025-10-05",
     "cantidad": 5, "precio_unitario": 75, "total": 375},

    {"razon_social": "servicios_veep", "ruc": "1234567890123", "telefono": "0987654321",
     "descripcion_trabajo": "block_formulario", "fecha_entrega": "2025-10-10",
     "cantidad": 20, "precio_unitario": 15, "total": 300}                                               
]

collection.insert_many(lista)
print("Documentos insertados correctamente.")
