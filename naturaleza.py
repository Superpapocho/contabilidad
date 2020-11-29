# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:51:50 2020

@author: Windows
"""

def naturaleza_amortizacion_bullet(plz):
    lista=[]
    # Dia del prestamo
    lista.append("Activo")
    lista.append("Pasivo")
    # Fin de mes
    lista.append("Pasivo")
    lista.append("Gasto")
    
    for i in range(plz-1):
        # Día de pago
        lista.append("Pasivo")
        lista.append("Gasto")
        lista.append("Pasivo")
        lista.append("Activo")
        # Fin de mes
        lista.append("Pasivo")
        lista.append("Gasto")
    
    # Final
    lista.append("Pasivo")
    lista.append("Gasto")
    lista.append("Pasivo")
    lista.append("Activo")
    lista.append("Pasivo")
    
    return lista

def naturaleza_amortizacion_cf_cc(plz):
    lista=[]
    # Dia del prestamo
    lista.append("Activo")
    lista.append("Pasivo")
    
    for i in range(plz):
        # Fin de mes
        lista.append("Pasivo")
        lista.append("Gasto")
        # Día de pago
        lista.append("Pasivo")
        lista.append("Gasto")
        lista.append("Activo")
        lista.append("Pasivo")
        lista.append("Pasivo")
    
    return lista

def naturaleza_sociedad_limitada(factor):
    lista=[]
    # Dia del prestamo
    if factor:
        lista.append("Activo")
        lista.append("Activo")
        lista.append("Patrimonio")
        lista.append("Patrimonio")
    else:
        lista.append("Activo")
        lista.append("Patrimonio")

    return lista

def naturaleza_sociedad_anonima():
    lista=[]
    lista.append("Patrimonio")
    lista.append("Patrimonio")

    return lista

def naturaleza_venta_acciones(factor):
    lista=[]
    
    lista.append("Patrimonio")
    lista.append("Activo")

    if factor == "menor":
        lista.append("Gasto")
    elif factor == "mayor":
        lista.append("Patrimonio")
    
    return lista

def naturaleza_nomina(factor):
    lista=[]
    for i in range(2):
        lista.append("Pasivo")
        if factor==False:
            lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Gasto")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
        lista.append("Pasivo")
    
    
    lista.append("Pasivo")
    lista.append("Pasivo")
    lista.append("Activo")
    
    return lista