# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:56:53 2020

@author: Windows
"""
import datetime

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

def credito_amortizacion_cfija(plz,m,c,t,dif): 
    mtemp = m
    interes=[]
    abono=[]
    cuota=[]
    
    for i in range(plz):
        interes.append(mtemp*t)
        cuota.append(c)
        abono.append(c-interes[i])
        mtemp -= abono[i]

    interes_causar=[]
    interes_pagar=[]
    for i in range(len(interes)):
        interes_causar.append((interes[i]/30)*dif)
        interes_pagar.append((interes[i]/30)*(30-dif))
        
    global debito
    debito=[]
    global credito
    credito=[]
    
    # Dia del prestamo
    D_append(m)
    C_append(m)
    
    for i in range(plz):
        C_append(round(interes_causar[i]))
        D_append(round(interes_causar[i]))
        C_append(round(interes_pagar[i]))
        D_append(round(interes_pagar[i]))
        
        C_append(round(c))
        D_append(round(interes[i]))
        D_append(round(abono[i]))
    
    return [debito,credito]

def credito_amortizacion_cc(plz,m,t,dif):
    capital_constante = m/plz
    mtemp = m
    interes=[]
    abono=[]
    cuota=[]
    
    for i in range(plz):
        interes.append(mtemp*t)
        abono.append(capital_constante)
        cuota.append(capital_constante+interes[i])
        mtemp -= capital_constante
    
    interes_causar=[]
    interes_pagar=[]
    for i in range(len(interes)):
        interes_causar.append((interes[i]/30)*dif)
        interes_pagar.append((interes[i]/30)*(30-dif))
    
    global debito
    debito=[]
    global credito
    credito=[]
    
    # Dia del prestamo
    D_append(m)
    C_append(m)
    
    for i in range(plz):
        C_append(round(interes_causar[i]))
        D_append(round(interes_causar[i]))
        C_append(round(interes_pagar[i]))
        D_append(round(interes_pagar[i]))
        
        C_append(round(cuota[i]))
        D_append(round(interes[i]))
        D_append(round(capital_constante))
    
    return [debito,credito]
    
def credito_sociedad_limitada(efectivo,ppe,factor):
    global debito
    debito=[]
    global credito
    credito=[]
    
    if factor:
        D_append(efectivo)    
        D_append(ppe)
        C_append(efectivo)
        C_append(ppe)
    else:
        if efectivo==0:
            D_append(ppe)
            C_append(ppe)
        elif ppe==0:
            D_append(efectivo)
            C_append(efectivo)
            
    return [debito,credito]
            
def credito_sociedad_anonima(capital):
    global debito
    debito=[]
    global credito
    credito=[]
    
    D_append(capital)
    C_append(capital)
    
    return [debito,credito]
            
def credito_venta_acciones(cantidad, precio_par, precio, factor, diferencia):
    global debito
    debito=[]
    global credito
    credito=[]
    C_append(round(precio_par*cantidad,2))
    D_append(round(precio*cantidad,2))
    
    if factor == "menor":
        D_append(round(cantidad*diferencia,2))
    elif factor == "mayor":
        C_append(round(cantidad*diferencia,2))
        
    return [debito,credito]
    
def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)
    # subtract the number of remaining 'overage' days to get last day of current month, or said programattically said, the previous day of the first of next month
    return next_month - datetime.timedelta(days=next_month.day)

def credito_nomina(fecha, trabajador, salario, dotacion, arl, factor): 
    global debito 
    debito=[]
    global credito
    credito=[]
    
    dif = (last_day_of_month(fecha).day - fecha.day + 1)/30
    print(dif)
    # Definición de variables
    salario = salario * trabajador
    aux_transporte = 0
    if factor==False:
        aux_transporte = 102854 * trabajador
    aporte_salud_t = salario * 0.04
    aporte_pension_t = salario * 0.04
    neto_pagar = salario + aux_transporte - aporte_pension_t - aporte_salud_t
    dotacion = dotacion * trabajador
    aporte_salud_e = salario * 0.085
    aporte_pension_e = salario * 0.12
    aporte_arl = salario * arl
    cesantias_prima = (salario+aux_transporte)*0.0833
    intereses_cesantias = (salario+aux_transporte)*0.01
    vacaciones = salario * 0.0417
    compensacion = salario * 0.04
    aportes_nomina = (2*cesantias_prima)+intereses_cesantias+vacaciones+aporte_salud_e+aporte_salud_t+aporte_pension_t+aporte_pension_e+aporte_arl+compensacion
    
    # Causación a fin de mes
    C_append((neto_pagar+dotacion)*dif)
    if factor==False:
        D_append(aux_transporte*dif)
    D_append(salario*dif)
    D_append(dotacion*dif)
    D_append(aporte_salud_e*dif)
    D_append(aporte_pension_e*dif)
    
    D_append(cesantias_prima*dif)
    D_append(intereses_cesantias*dif)
    D_append(vacaciones*dif)
    D_append(cesantias_prima*dif)
    D_append(aporte_arl*dif)
    D_append(compensacion*dif)
    
    C_append(cesantias_prima*dif)
    C_append(intereses_cesantias*dif)
    C_append(vacaciones*dif)
    C_append(cesantias_prima*dif)
    C_append(aporte_arl*dif)
    C_append(compensacion*dif)
    
    C_append((aporte_salud_e+aporte_salud_t)*dif)
    C_append((aporte_pension_e+aporte_pension_t)*dif)
    
    # Inicio del otro mes
    C_append((neto_pagar+dotacion)*(1-dif))
    if factor==False:
        D_append(aux_transporte*(1-dif))
    D_append(salario*(1-dif))
    D_append(dotacion*(1-dif))
    D_append(aporte_salud_e*(1-dif))
    D_append(aporte_pension_e*(1-dif))
    
    D_append(cesantias_prima*(1-dif))
    D_append(intereses_cesantias*(1-dif))
    D_append(vacaciones*(1-dif))
    D_append(cesantias_prima*(1-dif))
    D_append(aporte_arl*(1-dif))
    D_append(compensacion*(1-dif))
    
    C_append(cesantias_prima*(1-dif))
    C_append(intereses_cesantias*(1-dif))
    C_append(vacaciones*(1-dif))
    C_append(cesantias_prima*(1-dif))
    C_append(aporte_arl*(1-dif))
    C_append(compensacion*(1-dif))
    C_append((aporte_salud_e+aporte_salud_t)*(1-dif))
    C_append((aporte_pension_e+aporte_pension_t)*(1-dif))
    
    # Pago
    D_append(neto_pagar+dotacion)
    D_append(aportes_nomina)
    C_append(neto_pagar+dotacion+aportes_nomina)
    
    return [debito,credito]    
    
    
    
    
    
    