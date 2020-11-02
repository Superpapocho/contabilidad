# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:42:52 2020

@author: Carlos Rubio
"""
import tkinter
from tkinter import ttk

#Creación del programa

root = tkinter.Tk()
root.title("Prueba de contabilidad")
root.iconbitmap()
root.geometry("750x300")

#Creación de las columnas
my_tree = ttk.Treeview(root)

my_tree["columns"] = ("Fecha", "Descripción","Cuenta" ,"Activo", "Pasivo")
my_tree.column("#0",width=25)
my_tree.column("Fecha",width=40)
my_tree.column("Descripción",width=150)
my_tree.column("Cuenta",width=150)
my_tree.column("Activo",width=80)
my_tree.column("Pasivo",width=80)

#Creación de los títulos de la tabla

my_tree.heading("#0",text="")
my_tree.heading("Fecha",text="Fecha")
my_tree.heading("Descripción",text="Descripción")
my_tree.heading("Cuenta",text="Cuenta")
my_tree.heading("Activo",text="Activo")
my_tree.heading("Pasivo",text="Pasivo")

#Lista de productos que pertenecen a cada cuenta
#Ejemplo de una empresa que fabrica mesas y sillas

Materias_primas = ["Fórmica","Aglomerado","Tubería metálica","Pegante","Tornillos"]

Propiedades = ["Vehiculos","Edificios","Muebles y enseres","Equipo de cómputo",
             "Maquinaria y equipo"]

Productos_terminados = ["Mesas","Sillas"]

#Añadirel texto a la ventana

my_tree.pack(pady=20)


#Función para registrar una nueva transacción en la cuenta manualmente

def registro_manual(Entra):
    fecha = str(input("Fecha: "))
    producto = str(input("Producto: "))
    cuenta = ""
    if producto in Materias_primas:
        cuenta = "Inventarios"
    elif producto in Productos_terminados:
        cuenta = "Inventarios"
    elif producto in Propiedades:
        cuenta = "Propiedades"
    cantidades = int(input("Cantidades: "))
    precio = float(input("Precio: "))
    valor = cantidades * precio
    contado = float(input("Porcentaje a pagar de contado: "))
    pago = valor*contado/100
    credito = valor - contado
    if Entra == True:
        my_tree.insert("","end",values = (fecha,producto,cuenta,valor,0))
        my_tree.insert("","end",values = (fecha,producto,"Efectivo",0,pago))
        my_tree.insert("","end",values = (fecha,producto,"Comerciales por pagar",0,credito))
    if Entra == False:
        my_tree.insert("","end",values = (fecha,producto,cuenta,0,valor))
        my_tree.insert("","end",values = (fecha,producto,"Efectivo",pago,0))
        my_tree.insert("","end",values = (fecha,producto,"Comerciales por cobrar",credito,0))

#Función que le permite al usuario añadir una nueva transacción a la contabilidad

def nueva_entrada():                      
    while input("Nueva entrada (escriba +) o finalizar (escriba cualquier otro): ") == "+":
        q = str(input("Clase:"))
        if q == "Compra":
            registro_manual(True)
        elif q == "Venta":
            registro_manual(False)

###Ejemplo para revisar el funcionamiento del programa
#Función para registar una nueva transacción en la cuenta automáticamente

def auto_registro(fecha,producto,cantidades,precio,contado,Entra):
    cuenta = ""
    if producto in Materias_primas:
        cuenta = "Inventarios"
    elif producto in Productos_terminados:
        cuenta = "Inventarios"
    elif producto in Propiedades:
        cuenta = "Propiedades"
    valor = cantidades * precio
    pago = valor * contado/100
    credito = valor - pago
    if Entra == True:
        my_tree.insert("","end",values = (fecha,producto,cuenta,valor,0))
        my_tree.insert("","end",values = (fecha,producto,"Efectivo",0,pago))
        my_tree.insert("","end",values = (fecha,producto,"Comerciales por pagar",0,credito))
    if Entra == False:
        my_tree.insert("","end",values = (fecha,producto,cuenta,0,valor))
        my_tree.insert("","end",values = (fecha,producto,"Efectivo",pago,0))
        my_tree.insert("","end",values = (fecha,producto,"Comerciales por cobrar",credito,0))

#Ejemplo de datos y contabilidad

auto_registro("1/04","Equipo de cómputo",1,11000,60,True)
auto_registro("14/04","Tornillos",750,10,50,True)
auto_registro("20/04","Mesas",20,1000,40,False)     

#Cerrar programa

root.mainloop()
