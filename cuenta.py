# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:38:07 2020

@author: Windows
"""

def cuenta_amortizacion_bullet(plz):
    lista=[]
    # Dia del prestamo
    lista.append("Efectivo")
    lista.append("Obligaciones financieras")
    # Fin de mes
    lista.append("Intereses por pagar")
    lista.append("Gastos por intereses")
    
    for i in range(plz-1):
        # Día de pago
        lista.append("Intereses por pagar")
        lista.append("Gastos por intereses")
        lista.append("Intereses por pagar")
        lista.append("Efectivo")
        # Fin de mes
        lista.append("Intereses por pagar")
        lista.append("Gastos por intereses")
    
    # Final
    lista.append("Intereses por pagar")
    lista.append("Gastos por intereses")
    lista.append("Intereses por pagar")
    lista.append("Efectivo")
    lista.append("Obligaciones financieras")
    
    return lista

def cuenta_amortizacion_cf_cc(plz):
    lista=[]
    # Dia del prestamo
    lista.append("Efectivo")
    lista.append("Obligaciones financieras")
    
    for i in range(plz):
        # Fin de mes
        lista.append("Intereses por pagar")
        lista.append("Gastos por intereses")
        
        # Día de pago
        lista.append("Intereses por pagar")
        lista.append("Gastos por intereses")
        lista.append("Efectivo")
        lista.append("Intereses por pagar")
        lista.append("Obligaciones financieras")

    return lista

def cuenta_sociedad_limitada(efectivo,ppe,factor):
    lista=[]
    # Dia del prestamo
    if factor:
        lista.append("Efectivo")
        lista.append("PP&E")
        lista.append("Aportes de capital (Efectivo)")
        lista.append("Aportes de capital (PP&E)")
    else:
        if efectivo == 0:
            lista.append("PP&E")
            lista.append("Aportes de capital (PP&E)")
        elif ppe==0:
            lista.append("Efectivo")
            lista.append("Aportes de capital (Efectivo)")

    return lista

def cuenta_sociedad_anonima():
    lista= []
    lista.append("Capital autorizado")
    lista.append("Capital por suscribir")
    
    return lista

def cuenta_venta_acciones(socio,factor):
    lista=[]
    
    lista.append("Capital por suscribir ("+socio+")")
    lista.append("Efectivo")
        
    if factor == "menor":
        lista.append("Perdida en colocacion de acciones")
    elif factor == "mayor":
        lista.append("Prima en colocacion de acciones")
    
    return lista

def cuenta_nomina(factor):
    lista=[]
    
    for i in range(2):
        lista.append("Sueldo a pagar")
        if factor==False:
            lista.append("Auxilio de transporte")
        lista.append("Sueldo")
        
        lista.append("Cesantias")
        lista.append("Intereses por cesantias")
        lista.append("Vacaciones")
        lista.append("Prima de servicios")
        lista.append("Dotación")
        lista.append("Salud")
        lista.append("Pensión")
        lista.append("ARL")
        lista.append("Caja de compensación")
        
        lista.append("Cesantias")
        lista.append("Intereses por cesantias")
        lista.append("Vacaciones")
        lista.append("Prima de servicios")
        lista.append("ARL")
        lista.append("Caja de compensación")
        lista.append("Salud")
        lista.append("Pensión")
        
def cuenta_compra_admin():
    lista = []
    lista.append("PP&E")
    lista.append("IVA")
    lista.append("Efectivo")
    lista.append("Retefuente")
    return lista

def cuenta_compra_prod():
    lista = []
    lista.append("IVA")
    lista.append("Efectivo")
    lista.append("Retefuente")
    return lista

def cuenta_venta():
    lista = []
    lista.append("Costo de ventas")
    lista.append("Efectivo")
    lista.append("Anticipo de impuestos")
    lista.append("Ingreso de ventas")
    lista.append("IVA")
    return lista

def cuenta_depreciacion(meses):
    lista = []
    for i in range(meses):
        lista.append("Depreciación")
    return lista
    
    
    lista.append("Sueldo a pagar")
    lista.append("Aportes a nomina")
    lista.append("Efectivo")
    
    return lista
