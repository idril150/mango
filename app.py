from ast import Try
import collections
from fileinput import close
from http import client
from tkinter import N
from typing import Collection
from unittest import result
import pymongo

MONGO_HOST = "127.0.0.1"
MONGO_PUERTO = "27017"
MONGO_TIEMPO_FUERA = 1000

MONGO_URI = "mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS = "escuela"
MONGO_COLECCION = "alumnos"

cliente = pymongo.MongoClient(
    MONGO_URI, serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
basedatos = cliente[MONGO_BASEDATOS]
coleccion = basedatos[MONGO_COLECCION]

print("mostramos los datos")
for hello in coleccion.find():
    print(hello["nombre"]+" "+hello["sexo"]+" "+str(hello["calificacion"]))

print("\nconsulta de pepe")
print(coleccion.find_one({"nombre": "Pepe"}))
    
coleccion.insert_one({"nombre": "juan", "sexo": "M", "calificacion": 7})
print("\nmostramos los datos con juan añadido y su consulta")
for kkdvk in coleccion.find():
    print(kkdvk["nombre"]+" "+kkdvk["sexo"]+" "+str(kkdvk["calificacion"]))

print(coleccion.find_one({"nombre": "juan"}))


print("\nborramos a juan y mostar los datos")
coleccion.find_one_and_delete({"nombre": "juan"})
for documento in coleccion.find():
    print(documento["nombre"]+" "+documento["sexo"] +
          " "+str(documento["calificacion"]))
cliente.close()
