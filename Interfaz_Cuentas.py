# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 16:42:52 2020

@author: Carlos Rubio
"""
import tkinter
from tkinter import ttk
import Cuentas_Pro

root = tkinter.Tk()
root.title("Prueba de contabilidad")
root.iconbitmap()
root.geometry("750x300")


#Columnas
my_tree = ttk.Treeview(root)

my_tree["columns"] = ("Fecha", "Descripción","Cuenta" ,"Activo", "Pasivo")
my_tree.column("#0",width=25)
my_tree.column("Fecha",width=120)
my_tree.column("Descripción",width=120)
my_tree.column("Cuenta",width=120)
my_tree.column("Activo",width=120)
my_tree.column("Pasivo",width=120)

#Headings

my_tree.heading("#0",text="")
my_tree.heading("Fecha",text="Fecha")
my_tree.heading("Descripción",text="Descripción")
my_tree.heading("Cuenta",text="Cuenta")
my_tree.heading("Activo",text="Activo")
my_tree.heading("Pasivo",text="Pasivo")

#Root 2


#Add Data

Materias_primas = ["Fórmica","Aglomerado","Tubería metálica","Pegante","Tornillos"]

Propiedades = ["Vehiculos","Edificios","Muebles y enseres","Equipo de cómputo",
             "Maquinaria y equipo"]

Productos_terminados = ["Mesas","Sillas"]

my_tree.pack(pady=20)

def nueva_entrada(Entra):
    r1 = str(input("Fecha: "))
    r2 = str(input("Descripción: "))
    r3 = ""
    if r2 in (Materias_primas or Productos_terminados):
        r3 = "Inventarios"
    elif r2 in Propiedades:
        r3 = "Propiedades"
    r4 = float(input("Valor: "))
    r5 = float(input("Porcentaje a pagar de contado: "))
    cont = r4*r5/100
    cred = r4 - cont
    if Entra == True:
        my_tree.insert("","end",values = (r1,r2,r3,r4,0))
        my_tree.insert("","end",values = (r1,r2,"Efectivo",0,cont))
        my_tree.insert("","end",values = (r1,r2,"Comerciales por pagar",0,cred))
    if Entra == False:
        my_tree.insert("","end",values = (r1,r2,r3,0,r4*r5))
        my_tree.insert("","end",values = (r1,r2,"Efectivo",0,cont))
        my_tree.insert("","end",values = (r1,r2,"Comerciales por pagar",0,cred))

lista_entradas = []
lista_salidas = []

while input("Nueva entrada (escriba +) o finalizar (escriba cualquier otro): ") == "+":
    q = str(input("Clase:"))
    if q == "Compra":
        nueva_entrada(True)
    elif q == "Venta":
        nueva_entrada(False)

#Close

root.mainloop()

