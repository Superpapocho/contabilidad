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
