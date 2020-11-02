# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 05:13:38 2020

@author: Carlos Rubio
"""

#Definición de la clase Cuenta con sus atributos

class Cuenta:
    
    def __init__(self):
        self.Subtotal = 0
        self.Iva = 0
        self.Total = 0
        self.Retefuente = 0
        self.A_pagar = 0
        self.Efectivo = 0
        self.Por_Pagar = 0
 
 #Para cuando se adicione una transacción a la cuenta       
 
    def __add__(self,monto,contado):
        self.Subtotal = self.Subtotal + monto
        self.Iva = self.Subtotal * 0.19
        self.Total = self.Subtotal + self.Iva
        self.Retefuente = self.Total * 0.025
        self.A_pagar = self.Total - self.Retefuente
        self.Efectivo = self.A_pagar * (contado/100)
        self.Por_Pagar = self.A_pagar * ((100-contado)/100)
            
#Creación de las cuentas más importantes

Compras_Administrativas = Cuenta()
Compras_Comercialización = Cuenta()
Compras_Producción = Cuenta()
Inventario_Materias_Primas = Cuenta()
Inventario_Productos_Terminados = Cuenta()

#Creación de la clase Saldo para cuando se realice una contabilidad más detallada
#de los inventarios

class Saldo:
    
    def __init__(self):
        self.costo = 0
        self.cantidad = 0
        self.valor = 0

#Para cuando se adicione una transacción a la cuenta 

    def sumar(self,cantidad,precio):
        self.cantidad = self.cantidad + cantidad
        self.valor = self.valor + (precio * cantidad)
        self.costo = self.valor / self.cantidad
          
#Diccionario de la vida útil de las propiedades

vida_util = {"Vehiculos":5,"Edificios":20,"Muebles y enseres":10,"Equipo de cómputo":3,
             "Maquinaria y equipo":10}

#Creación de la clase Propiedad junto con el método para calcular su
#respectiva depreciación.

class Propiedad:
    
    def __init__(self,categoria,valor,meses):
        self.valor_inicial = valor
        self.depreciacion = self.valor_inicial / (12*vida_util[categoria])
        self.acumulada = meses * self.depreciacion
        self.valor_final = self.valor_inicial - self.acumulada
        
        

        

    
        
    
        
