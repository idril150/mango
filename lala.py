from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"

MONGO_BASEDATOS="escuela"
MONGO_COLECCION="alumnos"
cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
baseDatos=cliente[MONGO_BASEDATOS]
coleccion=baseDatos[MONGO_COLECCION]
def mostrarDatos():
    try:
        registros=tabla.get_children()
        for registro in registros:
            tabla.delete(registro)
        for documento in coleccion.find():
            tabla.insert('',0,text=documento["_id"],values=documento["nombre"])
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
def crearRegistro():
    if len(nombre.get())!=0 and len(calificacion.get())!=0 and len(sexo.get())!=0 :
        try:
            documento={"nombre":nombre.get(),"calificacion":calificacion.get(),"sexo":sexo.get()}
            coleccion.insert(documento)
            nombre.delete(0,END)
            sexo.delete(0,END)
            calificacion.delete(0,END)
        except pymongo.errors.ConnectionFailure as error:
            print(error)
    else:
        messagebox.showerror(message="Los campos no pueden estar vacios")
    mostrarDatos()
ventana=Tk()
tabla=ttk.Treeview(ventana,columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading("#0",text="ID")
tabla.heading("#1",text="NOMBRE")

#Nombre
Label(ventana,text="Nombre").grid(row=2,column=0)
nombre=Entry(ventana)
nombre.grid(row=2,column=1)
#Sexo
Label(ventana,text="Sexo").grid(row=3,column=0)
sexo=Entry(ventana)
sexo.grid(row=3,column=1)
#Calificacion
Label(ventana,text="Calificacion").grid(row=4,column=0)
calificacion=Entry(ventana)
calificacion.grid(row=4,column=1)
#Boton crear
crear=Button(ventana,text="Crear alumno",command=crearRegistro,bg="green",fg="white")
crear.grid(row=5,columnspan=2)
mostrarDatos()
ventana.mainloop()