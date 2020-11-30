# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 21:33:03 2020

@author: Windows
"""

import datetime

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

def fechas_amortizacion_bullet(fecha,plz):    
    w=fecha.day
    x=fecha.month
    z=fecha.year
    plazo=plz
    lista=[]
    
    año_cambiante=z
    
    lista.append(str(datetime.date(z,x,w)))
    lista.append(str(datetime.date(z,x,w)))
    lista.append(str(last_day_of_month(datetime.date(z, x, w))))
    lista.append(str(last_day_of_month(datetime.date(z, x, w))))
    for month in range(x+1,x+plazo):     
        año_cambiante += int(month // 12.0000001)
            
        if month % 12 != 0:    
            month = month % 12
        else:
            month = 12
            
        for k in range(4):
            lista.append(str(datetime.date(año_cambiante,month,w))) 
        for j in range(2): 
            lista.append(str(last_day_of_month(datetime.date(año_cambiante, month, w))))
                
        año_cambiante=z
    
    month = x + plazo
    año_cambiante += int(month // 12.0000001)
            
    if month % 12 != 0:    
        month = month % 12
    else:
        month = 12  
    for i in range(5):
        lista.append(str(datetime.date(año_cambiante,month,w)))
    return lista

def fechas_amortizacion_cf_cc(fecha,plz):    
    w=fecha.day
    x=fecha.month
    z=fecha.year
    plazo=plz
    lista=[]
    
    año_cambiante=z
    
    lista.append(str(datetime.date(z,x,w)))
    lista.append(str(datetime.date(z,x,w)))
    for month in range(x+1,x+plazo):     
        año_cambiante += int(month // 12.0000001)
            
        if month % 12 != 0:    
            month = month % 12
        else:
            month = 12
            
        if month == 1:    
            for j in range(2): 
                lista.append(str(last_day_of_month(datetime.date(año_cambiante, 12, w))))
        else:    
            for j in range(2): 
                lista.append(str(last_day_of_month(datetime.date(año_cambiante, month-1, w))))    
        
        for k in range(5):
            lista.append(str(datetime.date(año_cambiante,month,w))) 
        año_cambiante=z
    
    return lista

def fechas_sociedad_limitada(fecha,factor):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista = []
    if factor:    
        for i in range(4):
            lista.append(str(datetime.date(z,x,w)))
    else:
        for i in range(2):
            lista.append(str(datetime.date(z,x,w)))
    return lista

def fechas_sociedad_anonima(fecha):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista = []
    for i in range(2):
        lista.append(str(datetime.date(z,x,w)))
    
    return lista

def fechas_venta_acciones(fecha,factor):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista=[]
    
    if  factor == "igual":
        for i in range(2):
            lista.append(str(datetime.date(z,x,w)))
    else:
        for i in range(3):
            lista.append(str(datetime.date(z,x,w)))
    
    return lista

def fechas_nomina(fecha,factor):    
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista=[]
    if factor:
        for i in range(19):
            lista.append(str(last_day_of_month(datetime.date(z, x, w))))
    else:
        for i in range(20):
            lista.append(str(last_day_of_month(datetime.date(z, x, w))))
    
    if factor:
        for i in range(19):
            lista.append(str(datetime.date(z, x+1, w)))
    else:
        for i in range(20):
            lista.append(str(datetime.date(z, x+1, w)))       
            
    for i in range(3):
        lista.append(str(datetime.date(z, x+1, w)))

    return lista

def first_day_of_next_month(date):
    day = 1
    if date.month == 12:
        month = 1
        year = date.year + 1
    else:
        month = date.month + 1
        year = date.year
    new_date = datetime.date(year,month,day)
    return new_date

def same_day_n_months(date,months):
    s_months = date.month + months
    if s_months > 12:
        month = s_months%12
        year = date.year + s_months//12
    else: 
        month = s_months
        year = date.year
    meses_de_30 = [4,6,9,11]
    if month in meses_de_30 and date.day == 31:
        day = 30
    elif month == 2 and date.day > 28:
        day = 28
    else:
        day = date.day
    new_date = datetime.date(year,month,day)
    return new_date

def fecha_compra(fecha):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista = []
    fecha = datetime.date(z,x,w)
    for i in range(4):
        lista.append(str(fecha))
    return lista
    
def fecha_venta(fecha):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista = []
    fecha = datetime.date(z,x,w)
    for i in range(6):
        lista.append(fecha)
    return lista

def fecha_depreciacion(fecha,meses):
    w=fecha.day
    x=fecha.month
    z=fecha.year
    lista = []
    fecha = datetime.date(z,x,w)
    for i in range(0,meses,1):
        fecha_nt = same_day_n_months(fecha,i)
        lista.append(fecha_nt)
    return lista
