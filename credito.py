# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:56:53 2020

@author: Windows
"""
def D_append(x):
    debito.append(x)
    credito.append(0)

def C_append(x):
    credito.append(x)
    debito.append(0)

def credito_amortizacion_bullet(plz,m,mc,mp,c): 
    
    global debito 
    debito=[]
    global credito
    credito=[]
    
    # Dia del prestamo
    D_append(m)
    C_append(m)

    # Fin de mes
    C_append(mc)
    D_append(mc)
    
    for i in range(plz-1):
        # Día de pago
        C_append(mp)
        D_append(mp)
        D_append(c)
        C_append(c)

        # Fin de mes
        C_append(mc)
        D_append(mc)
    
    # Final
    C_append(mp)
    D_append(mp)
    D_append(c)
    C_append(c+m)
    D_append(m)
    
    return [debito,credito]