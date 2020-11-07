# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 16:26:33 2020

@author: Windows
"""
from tkinter import * 
from tkinter import ttk
from datetime import datetime
import Cambio_de_fecha
import cuenta
import naturaleza
import credito

def datos_amortizacion():
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    plazo = int(plazo_box.get())
    monto = int(monto_box.get())
    tasa = float(tasa_box.get())
    tipo = tipo_box.get()
    
    
    
    if tipo_box.get()=="Bullet":
        diferencia = 30 - int(fecha_dt.day)
        tasa_causar = (tasa/30)*diferencia
        tasa_pagar = tasa - tasa_causar
        
        monto_causar = monto * (tasa_causar/100)
        monto_pagar =  monto * (tasa_pagar/100)
        cuota = monto * tasa
        
        # Fecha
        x1 = Cambio_de_fecha.fechas_amortizacion_bullet(fecha_dt,plazo)
        print("x1: ",len(x1))
        print(x1)
        # Cuenta
        x2 = cuenta.cuenta_amortizacion_bullet(plazo)
        print("x2: ",len(x2))
        # Naturaleza
        x3 = naturaleza.naturaleza_amortizacion_bullet(plazo)
        print("x3: ",len(x3))
        #Crédito y Debito
        comodin = credito.credito_amortizacion_bullet(plazo,monto,monto_causar,monto_pagar,cuota)
        x4 = comodin[0]
        print("x4: ",len(x4))
        x5 = comodin[1]
        print("x5: ",len(x5))

    elif tipo_box.get()=="Cuota fija":
        pass
    elif tipo_box.get()=="Capital Constante":
        pass
    
    # Lista Unión
    y = [x1,x2,x3,x4,x5]
    global z
    z=[]
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    print(z)
    # Clear the boxes
    fecha_box.delete(0,END)
    plazo_box.delete(0,END)
    monto_box.delete(0,END)
    tasa_box.delete(0,END)
    tipo_box.delete(0,END)
    
    return z

def ventana_amortizacion(): 

    # Toplevel object which will be treated as a new window 
    newWindow = Toplevel() 
    newWindow.title("Amortización")  
    newWindow.geometry("500x500") 
    
    fl = Label(newWindow, text="Fecha",width=20,anchor=W)
    fl.grid(row=0,column=0, padx=5, pady=3)
    plazo = Label(newWindow, text="Plazo",width=20,anchor=W)
    plazo.grid(row=1,column=0, padx=5, pady=3)
    monto = Label(newWindow, text="Monto",width=20,anchor=W)
    monto.grid(row=2,column=0, padx=5, pady=3)
    tasa = Label(newWindow, text="Tasa mensual",width=20,anchor=W)
    tasa.grid(row=3,column=0, padx=5, pady=3)
    tipo = Label(newWindow, text="Tipo",width=20,anchor=W)
    tipo.grid(row=4,column=0, padx=5, pady=3)

    # Entry boxes
    global fecha_box
    fecha_box = Entry(newWindow)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    global plazo_box
    plazo_box = Entry(newWindow)
    plazo_box.grid(row=1,column=1, padx=5, pady=3)
    global monto_box
    monto_box = Entry(newWindow)
    monto_box.grid(row=2,column=1, padx=5, pady=3)
    global tasa_box
    tasa_box = Entry(newWindow)
    tasa_box.grid(row=3,column=1, padx=5, pady=3)
    global tipo_box
    options = ("Bullet","Cuota fija","Capital Constante")
    tipo_box = ttk.Combobox(newWindow, values = options)
    tipo_box.grid(row=4,column= 1)
    
    amortizacion = Button(newWindow, text = "Agregar datos",command=datos_amortizacion)
    amortizacion.grid(row=5,column=2,padx=5, pady=3)

    
    







  