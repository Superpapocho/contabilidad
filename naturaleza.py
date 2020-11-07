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