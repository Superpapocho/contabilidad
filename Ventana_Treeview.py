# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:32:30 2020
@author: Windows
"""

from tkinter import *
import pandas as pd
from tkinter import ttk,filedialog
from datetime import datetime
import Cambio_de_fecha
import cuenta
import naturaleza
import credito

root = Tk()
root.title('Contabilidad')
root.geometry("1100x1100")

wrapper1 = LabelFrame(root, text="Cuentas T")
wrapper2 = LabelFrame(root, text="Añadir datos")
wrapper3 = LabelFrame(root, text="Funciones contables")

wrapper1.pack(fill="both", expand="yes", padx= 20, pady = 10)
wrapper2.pack(fill="both", expand="yes", padx= 20, pady = 10)
wrapper3.pack(fill="both", expand="yes", padx= 20, pady = 10)

""" 
Add style 
"""
style = ttk.Style()
# Pick a theme
style.theme_use('default')

# Configure treeview colors
style.configure("Treeview",
    background="white",
    foreground="blue",
    rowheight=30,
    fieldbackground="white"
    )
# Change selected color
style.map('Treeview',
    background=[('selected','#009999')])

style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11)) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 13,'bold')) # Modify the font of the headings
style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
"""
Create Treeview Frame
"""     
#Create frame
tree_frame=Frame(wrapper1)
tree_frame.pack(pady=5)

#Scrollbar to the frame
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

# Create Treeview - selectmode("browse","none","extended")
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, style="mystyle.Treeview")

my_tree["columns"] = ("Fecha", "Cuenta","Naturaleza" ,"Debito", "Credito")
my_tree.column("#0",width=0)
my_tree.column("Fecha",width=200)
my_tree.column("Cuenta",width=200)
my_tree.column("Naturaleza",width=200)
my_tree.column("Debito",width=200)
my_tree.column("Credito",width=200)

#Headings

my_tree.heading("#0",text="")
my_tree.heading("Fecha",text="Fecha")
my_tree.heading("Cuenta",text="Cuenta")
my_tree.heading("Naturaleza",text="Naturaleza")
my_tree.heading("Debito",text="Debito")
my_tree.heading("Credito",text="Credito")
# Configure Scrollbar
tree_scroll.config(command=my_tree.yview)

my_tree.pack()

# Open new file
def file_open():
    filename=filedialog.askopenfilename(
        initialdir="D:/Windows/Desktop/Proyecto/contabilidad-main",
        title = "Abrir un archivo excel",
        filetype=(("xlsx files","*.xlsx"),("All files","*.*"))
        )
    if filename:
        try:
            filename = r"{}".format(filename)
            df = pd.read_excel(filename)
        except ValueError:
            my_label.config(text="File could not be opened. Try again")
        except FileNotFoundError:
            my_label.config(text="File could not be found. Try again")
    
    # Limpiar la base que se encuentre en el documento
    clear_tree()
    
    #Set up new treeview
    my_tree["column"]=list(df.columns)
    my_tree["show"]="headings"
    # Loop column list for headers
    for column in my_tree["column"]:
        my_tree.heading(column,text=column)
    
    #Put data in treeview
    df_rows = df.to_numpy().tolist()
    for row in df_rows:
        my_tree.insert("","end",values=row)
    
    # Pack the treeview finally
    my_tree.pack()
    
    # Recalcula Débito y Crédito
    add()

# Save current file
def save_open():
    filename = filedialog.asksaveasfilename(title="Select file",filetypes=[("Excel file", "*.xlsx")])
    if filename:
        column_a_list = []
        column_b_list = []
        column_c_list = []
        column_d_list = []
        column_e_list = []

        for child in my_tree.get_children():
            column_a_list.append(my_tree.item(child)["values"][0])   
            column_b_list.append(my_tree.item(child)["values"][1])  
            column_c_list.append(my_tree.item(child)["values"][2])  
            column_d_list.append(my_tree.item(child)["values"][3])  
            column_e_list.append(my_tree.item(child)["values"][4])  
        
        full_treeview_data_dict = {'Fecha': column_a_list, 'Cuenta': column_b_list, 'Naturaleza': column_c_list, 'Débito': column_d_list,'Crédito': column_e_list}

        treeview_df = pd.DataFrame.from_dict(full_treeview_data_dict)
        
        str(filename).replace("xlsx","")
        filename = "{0}.xlsx".format(filename)
        treeview_df.to_excel(str(filename))
        
def clear_tree():
    my_tree.delete(*my_tree.get_children()) 
"""
Contabilización del crédito y débito total
"""
x = "Débito: 0"
y = "Débito: 0"
lbl_D = Label(wrapper2,text=x)
lbl_D.grid(row=0,column=4)
lbl_C = Label(wrapper2,text=y)
lbl_C.grid(row=1,column=4)

def add():
    total_D = 0.0
    total_C = 0.0
    	
    for child in my_tree.get_children():
        total_D += float(my_tree.item(child, 'values')[3])
        total_C += float(my_tree.item(child, 'values')[4])
    
    x = StringVar()    
    x.set("Débito: "+str(total_D))
    lbl_D.config(textvariable=x)
    y = StringVar()
    y.set("Crédito: "+str(total_C))
    lbl_C.config(textvariable=y)

# Definición de variables globales para la función venta_acciones
acciones = 0
precio_par = 0
def definir_preciopar(y):
    global precio_par
    precio_par = y

def definir_acciones(x):
    global acciones
    acciones = x


"""
Funciones de manejo de tabla
"""
# Add record 
def add_record():
    # En caso de recibir vacio convierte a 0
    if debito_box.get()=="":
        x = 0
    else:
        x = debito_box.get()
    
    if credito_box.get()=="":
        y = 0
    else:
        y = credito_box.get()
    
    # Insertar al treeview
    my_tree.insert(parent='', index='end', text="Child",values=[fecha_box.get(),cuenta_box.get(),
                                        naturaleza_box.get(),x, y])
    
    # Limpiar las cajas
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    # Recalcula Débito y Crédito
    add()
    
# Modificar un registro
def update_record():
    # Obtener el número del indice
    selected = my_tree.focus()
    # Guardar los nuevos datos
    my_tree.item(selected,text="",values=(fecha_box.get(),cuenta_box.get(),
                                naturaleza_box.get(),debito_box.get(), credito_box.get()))
    # Limpiar las cajas
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    # Recalcula Débito y Crédito
    add()

# Limpiar las cajas
def clear_boxes():
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    # Recalcula Débito y Crédito
    add()

# Remover uno de los seleccionados
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
    # Recalcula Débito y Crédito
    add()

# Remover todos
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
    # Recalcula Débito y Crédito
    add()

# Remover los seleccionados
def remove_many():
    for i in my_tree.selection():
        my_tree.delete(i)
    # Recalcula Débito y Crédito
    add()
        
# Seleccionar registro
def select_record():
    # Clear entry boxes
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    # Grab index number
    selected = my_tree.focus()
    # Grab record values (or an specific column)
    values = my_tree.item(selected, 'values')

    fecha_box.insert(0, values[0])
    cuenta_box.insert(0,values[1])
    naturaleza_box.insert(0,values[2])
    debito_box.insert(0,values[3])
    credito_box.insert(0,values[4])
    
# Función de doble clic para seleccionar fila
def clicker(e):
    select_record()

# Mover filas para arriba y abajo
def limit(rows,ind,up_down):
    if up_down=="up":
        for row in rows:
            if my_tree.index(row)>ind:
                my_tree.move(row, my_tree.parent(row),my_tree.index(row)-1)
            elif my_tree.index(row)==ind:
                ind += 1
    elif up_down=="down":
        for row in reversed(rows):
            if my_tree.index(row)<ind:
                my_tree.move(row, my_tree.parent(row),my_tree.index(row)+1)
            elif my_tree.index(row)==ind:
                ind -= 1

def up():
    rows = my_tree.selection()
    ind = 0
    limit(rows,ind,"up")

def down():
    rows = my_tree.selection()
    ind=len(my_tree.get_children())-1
    limit(rows,ind,"down")

""" 
Add a menu 
"""
my_menu = Menu(root)
root.config(menu=my_menu)

# Add menu dropdown
# Number 1
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Abrir",command=file_open)
file_menu.add_command(label="Guardar",command=save_open)

my_label = Label(root, text='')
my_label.pack(pady=20)

# Number 2
selection_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Editar", menu=selection_menu)
selection_menu.add_command(label="Seleccionar (Doble click)",command=select_record)
selection_menu.add_command(label="Eliminar uno",command=remove_one)
selection_menu.add_command(label="Eliminar seleccionados",command=remove_many)
selection_menu.add_command(label="Eliminar todos",command=remove_all)

my_label = Label(root, text='')
my_label.pack(pady=20)

#Number 3
move_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Mover", menu=move_menu)
move_menu.add_command(label="Mover para arriba", command=up)
move_menu.add_command(label="Mover para abajo", command=down)

# Bindings
my_tree.bind("<Double-1>", clicker)

""" 
Create boxes frame 
"""
# Labels
fl = Label(wrapper2, text="Fecha")
fl.grid(row=0,column=0, padx=5, pady=3)
desl = Label(wrapper2, text="Cuenta")
desl.grid(row=1,column=0, padx=5, pady=3)
nl = Label(wrapper2, text="Naturaleza")
nl.grid(row=2,column=0, padx=5, pady=3)
debl = Label(wrapper2, text="Débito")
debl.grid(row=3,column=0, padx=5, pady=3)
cl = Label(wrapper2, text="Crédito")
cl.grid(row=4,column=0, padx=5, pady=3)

# Entry boxes
fecha_box = Entry(wrapper2)
fecha_box.grid(row=0,column=1, padx=5, pady=3, columnspan=3,ipadx=60)
cuenta_box = Entry(wrapper2)
cuenta_box.grid(row=1,column=1, padx=5, pady=3, columnspan=3,ipadx=60)
naturaleza_box = Entry(wrapper2)
naturaleza_box.grid(row=2,column=1, padx=5, pady=3, columnspan=3,ipadx=60)
debito_box = Entry(wrapper2)
debito_box.grid(row=3,column=1, padx=5, pady=3, columnspan=3,ipadx=60)
credito_box = Entry(wrapper2)
credito_box.grid(row=4,column=1, padx=5, pady=3, columnspan=3,ipadx=60)

# Buttons
add_record = Button(wrapper2, text = "Agregar Nuevo",command=add_record)
add_record.grid(row=5,column=0,padx=5, pady=8)

update_button = Button(wrapper2,text="Modificar",command=update_record)
update_button.grid(row=5,column=1,padx=5, pady=8)

delete_record = Button(wrapper2, text = "Borrar registro",command=remove_one)
delete_record.grid(row=5,column=2,padx=5, pady=8)

clear_boxes = Button(wrapper2,text = "Vaciar",command=clear_boxes)
clear_boxes.grid(row=5,column=3,padx=5,pady=8)

"""
Funciones contables
"""
def Amortizacion():
    ventana_amortizacion()
    
def Sociedades():
    ventana_sociedades()

def venta_acciones():
    ventana_acciones(acciones,precio_par)

def nomina():
    ventana_nomina()
    
def Compra_admin():
    ventana_compra_admin()
    
def Compra_produc():
    ventana_compra_prod()
    
def Venta_mercancias():
    ventana_ventas()
    
def Depreciacion():
    ventana_depreciacion()

"""
Buttons Funciones contables
"""
Amortizacion = Button(wrapper3, text = "Amortización",command=Amortizacion)
Amortizacion.grid(row=1,column=1,padx=5, pady=3)

Sociedades = Button(wrapper3, text = "Creación de sociedades",command=Sociedades)
Sociedades.grid(row=1,column=2,padx=5, pady=3)

Venta_acciones = Button(wrapper3, text = "Venta de acciones",command=venta_acciones)
Venta_acciones.grid(row=1,column=3,padx=5, pady=3)

Nomina = Button(wrapper3, text = "Nomina",command=nomina)
Nomina.grid(row=1,column=4,padx=5, pady=3)

compra_admin = Button(wrapper3, text = "Compras admin.",command=Compra_admin)
compra_admin.grid(row=1,column=4,padx=5, pady=3)

compra_produc = Button(wrapper3, text = "Compras produc.",command=Compra_produc)
compra_produc.grid(row=1,column=5,padx=5, pady=3)

venta_mercancias =  Button(wrapper3, text = "Venta de mercancías",command=Venta_mercancias)
venta_mercancias.grid(row=1,column=6,padx=5, pady=3)

depreciacion = Button(wrapper3, text = "Depreciación", command = Depreciacion)
depreciacion.grid(row=1,column=7,padx=5,pady=3)

"""
Amortización
"""
def datos_amortizacion():
    # Obtener la información de las boxes
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    plazo = int(plazo_box.get())
    monto = int(monto_box.get())
    tasa = float(tasa_box.get())
    tipo = tipo_box.get()
    
    # Definir intereses diarios
    diferencia = 30 - int(fecha_dt.day)
    tasa_causar = (tasa/30)*diferencia
    tasa_pagar = tasa - tasa_causar
    
    if tipo_box.get()=="Bullet":
        monto_causar = monto * (tasa_causar/100)
        monto_pagar =  monto * (tasa_pagar/100)
        cuota = monto * tasa
        
        # Fecha
        x1 = Cambio_de_fecha.fechas_amortizacion_bullet(fecha_dt,plazo)
        # Cuenta
        x2 = cuenta.cuenta_amortizacion_bullet(plazo)
        # Naturaleza
        x3 = naturaleza.naturaleza_amortizacion_bullet(plazo)
        # Crédito y Debito
        comodin = credito.credito_amortizacion_bullet(plazo,monto,monto_causar,monto_pagar,cuota)
        x4 = comodin[0]
        x5 = comodin[1]

    elif tipo_box.get()=="Cuota fija":
        cuota_fija = ((tasa/100)*((1+(tasa/100))**plazo)*monto)/(((1+(tasa/100))**plazo)-1)
        
        # Fecha
        x1 = Cambio_de_fecha.fechas_amortizacion_cf_cc(fecha_dt,plazo)
        # Cuenta
        x2 = cuenta.cuenta_amortizacion_cf_cc(plazo)
        # Naturaleza
        x3 = cuenta.naturaleza_amortizacion_cf_cc(plazo)
        # Crédito y Debito
        comodin = credito.credito_amortizacion_cfija(plazo,monto,cuota_fija,tasa/100,diferencia)
        x4 = comodin[0]
        x5 = comodin[1]
        
    elif tipo_box.get()=="Capital Constante":        
        # Fecha
        x1 = Cambio_de_fecha.fechas_amortizacion_cf_cc(fecha_dt,plazo)
        # Cuenta
        x2 = cuenta.cuenta_amortizacion_cf_cc(plazo)
        # Naturaleza
        x3 = cuenta.naturaleza_amortizacion_cf_cc(plazo)
        # Crédito y Debito
        comodin = credito.credito_amortizacion_cc(plazo,monto,tasa/100,diferencia)
        x4 = comodin[0]
        x5 = comodin[1]
    
    # Unión de las listas
    y = [x1,x2,x3,x4,x5]
    z=[]
    
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    plazo_box.delete(0,END)
    monto_box.delete(0,END)
    tasa_box.delete(0,END)
    tipo_box.delete(0,END)
    
    close_window(newAmort)
    add()
    print("Juan")
    
def ventana_amortizacion(): 

    # Toplevel object which will be treated as a new window 
    newAmort = Toplevel() 
    newAmort.title("Amortización")  
    newAmort.geometry("500x500") 
    
    fl = Label(newAmort, text="Fecha",width=20,anchor=W)
    fl.grid(row=0,column=0, padx=5, pady=3)
    plazo = Label(newAmort, text="Plazo",width=20,anchor=W)
    plazo.grid(row=1,column=0, padx=5, pady=3)
    monto = Label(newAmort, text="Monto",width=20,anchor=W)
    monto.grid(row=2,column=0, padx=5, pady=3)
    tasa = Label(newAmort, text="Tasa mensual",width=20,anchor=W)
    tasa.grid(row=3,column=0, padx=5, pady=3)
    tipo = Label(newAmort, text="Tipo",width=20,anchor=W)
    tipo.grid(row=4,column=0, padx=5, pady=3)

    # Entry boxes
    global fecha_box
    fecha_box = Entry(newAmort)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    global plazo_box
    plazo_box = Entry(newAmort)
    plazo_box.grid(row=1,column=1, padx=5, pady=3)
    global monto_box
    monto_box = Entry(newAmort)
    monto_box.grid(row=2,column=1, padx=5, pady=3)
    global tasa_box
    tasa_box = Entry(newAmort)
    tasa_box.grid(row=3,column=1, padx=5, pady=3)
    global tipo_box
    options = ("Bullet","Cuota fija","Capital Constante")
    tipo_box = ttk.Combobox(newAmort, values = options)
    tipo_box.grid(row=4,column= 1)
    
    amortizacion = Button(newAmort, text = "Agregar datos",command=datos_amortizacion)
    amortizacion.grid(row=5,column=2,padx=5, pady=3)

"""
Sociedades
"""

def datos_limitada(Ltda):
    # Obtener la información de las boxes
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    if efectivo_box.get()!="":
        efectivo = int(efectivo_box.get())
    else:
        efectivo = 0
    if ppe_box.get()!="":
        ppe = int(ppe_box.get())
    else:
        ppe = 0
    
    if (ppe!=0 and efectivo==0) or (ppe==0 and efectivo!=0): 
        # Fecha
        x1 = Cambio_de_fecha.fechas_sociedad_limitada(fecha_dt,False)
        # Cuenta
        x2 = cuenta.cuenta_sociedad_limitada(efectivo,ppe,False)
        # Naturaleza
        x3 = naturaleza.naturaleza_sociedad_limitada(False)
        # Credito y Debito
        comodin = credito.credito_sociedad_limitada(efectivo,ppe,False)
        x4 = comodin[0]
        x5 = comodin[1]
    elif (ppe==0 and efectivo==0):
        # Cierra la ventana en caso de que no reciba un dato
        ventana_sociedades(my_tree)
        close_window(Ltda)
    else:
        x1 = Cambio_de_fecha.fechas_sociedad_limitada(fecha_dt,True)
        x2 = cuenta.cuenta_sociedad_limitada(efectivo,ppe,True)
        x3 = naturaleza.naturaleza_sociedad_limitada(True)
        comodin = credito.credito_sociedad_limitada(efectivo,ppe,True)
        x4 = comodin[0]
        x5 = comodin[1]
    
    # Unión de las listas
    y = [x1,x2,x3,x4,x5]
    z=[]
    
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    efectivo_box.delete(0,END)
    ppe_box.delete(0,END)
    
    close_window(Ltda)
    add()
    
def datos_anonima(Sa):
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    capital = int(capital_box.get())
    accion = int(acciones_box.get())

    precio_par = capital/accion
    definir_acciones(accion)
    definir_preciopar(precio_par)
    
    # Fecha
    x1 = Cambio_de_fecha.fechas_sociedad_anonima(fecha_dt)
    # Cuenta
    x2 = cuenta.cuenta_sociedad_anonima()
    # Naturaleza
    x3 = naturaleza.naturaleza_sociedad_anonima()
    # Credito y Debito
    comodin = credito.credito_sociedad_anonima(capital)
    x4 = comodin[0]
    x5 = comodin[1]

    # Unión de las listas
    y = [x1,x2,x3,x4,x5]
    z=[]
    
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    capital_box.delete(0,END)
    acciones_box.delete(0,END)
    
    close_window(Sa)
    add()
  
def ventana_sociedades():
    # Toplevel object which will be treated as a new window 
    newSociedades = Toplevel() 
    newSociedades.title("Creación de Sociedades")  
    newSociedades.geometry("200x200") 
    
    # Button boxes
    sl_button = Button(newSociedades, text = "Sociedad Limitada",command=lambda: ltda(newSociedades))
    sl_button.place(relx=0.5,rely=0.3,anchor=CENTER)
    sa_button = Button(newSociedades, text = "Sociedad Anónima",command=lambda: sociedad_anonima(newSociedades))
    sa_button.place(relx=0.5,rely=0.6,anchor=CENTER)
     
def close_window(x):
    x.destroy()

def ltda(newSociedades):
    # Cerrar ventana anterior
    close_window(newSociedades)
    
    # Toplevel object which will be treated as a new window 
    Ltda = Toplevel() 
    Ltda.title("Creación de Sociedades")  
    Ltda.geometry("500x500") 
    
    fl = Label(Ltda, text="Fecha",width=20,anchor=W)
    fl.grid(row=0,column=0, padx=5, pady=3)
    efectivo = Label(Ltda, text="Efectivo",width=20,anchor=W)
    efectivo.grid(row=1,column=0, padx=5, pady=3)
    ppe = Label(Ltda, text="PP&E",width=20,anchor=W)
    ppe.grid(row=2,column=0, padx=5, pady=3)

    # Entry boxes
    global fecha_box
    fecha_box = Entry(Ltda)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    global efectivo_box
    efectivo_box = Entry(Ltda)
    efectivo_box.grid(row=1,column=1, padx=5, pady=3)
    global ppe_box
    ppe_box = Entry(Ltda)
    ppe_box.grid(row=2,column=1, padx=5, pady=3)
    
    limitada = Button(Ltda, text = "Agregar datos",command=lambda: datos_limitada(Ltda))
    limitada.grid(row=3,column=2,padx=5, pady=3)
    
def sociedad_anonima(newSociedades):
    # Cerrar ventana anterior
    close_window(newSociedades)
    
    # Toplevel object which will be treated as a new window 
    Sa = Toplevel() 
    Sa.title("Creación de Sociedades")  
    Sa.geometry("500x500") 
    
    fl = Label(Sa, text="Fecha",width=20,anchor=W)
    fl.grid(row=0,column=0, padx=5, pady=3)
    C_autorizado = Label(Sa, text="Capital autorizado",width=20,anchor=W)
    C_autorizado.grid(row=1,column=0, padx=5, pady=3)
    acciones = Label(Sa, text="Número de acciones",width=20,anchor=W)
    acciones.grid(row=2,column=0, padx=5, pady=3)

    # Entry boxes
    global fecha_box
    fecha_box = Entry(Sa)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    global capital_box
    capital_box = Entry(Sa)
    capital_box.grid(row=1,column=1, padx=5, pady=3)
    global acciones_box
    acciones_box = Entry(Sa)
    acciones_box.grid(row=2,column=1, padx=5, pady=3)
    
    anonima = Button(Sa, text = "Agregar datos",command=lambda: datos_anonima(Sa))
    anonima.grid(row=3,column=2,padx=5, pady=3)
    
""" 
Venta de acciones 
"""

def datos_venta_acciones(newAcciones,accion,precio_par):
    
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    socio = socio_box.get()
    cantidad = float(cantidad_box.get())
    precio = float(precio_box.get())
    
    if precio <= 0:
        # Toplevel object which will be treated as a new window 
        Errorcantidad = Toplevel() 
        Errorcantidad.title("Acciones")  
        Errorcantidad.geometry("250x100")
        advertencia = Label(newAcciones, text="Error: El precio señalado \nno es valido",width=50,anchor=W)
        advertencia.grid(row=0,column=0, padx=40, pady=7, columnspan=2)
        close_window(newAcciones)
        return 0
    # Restricciones sobre la cantidad de acciones que se pueden vender
    if cantidad > accion or cantidad < 0:
        # Toplevel object which will be treated as a new window 
        Errorcantidad = Toplevel() 
        Errorcantidad.title("Acciones")  
        Errorcantidad.geometry("250x100")
        advertencia = Label(Errorcantidad, text="Error: El número de acciones a \nadquirir no es valido",width=50,anchor=W)
        advertencia.grid(row=0,column=0, padx=40, pady=7, columnspan=2)
        close_window(newAcciones)
        return 0
    
    # Identifica si el precio puesto por el usuario es mayor, menor o igual
    # al valor nominal de una acción
    precio_abajo = precio_par-0.1
    precio_arriba = precio_par+0.1
    factor = "igual"
    diferencia = 0

    if precio > precio_arriba:
        factor = "mayor"
        diferencia = precio - precio_par 
    elif precio < precio_abajo:
        factor = "menor"
        diferencia = precio_par - precio

    #Actualizar acciones disponibles para la venta
    temporal = accion - cantidad
    definir_acciones(temporal)
    
    # Fecha
    x1 = Cambio_de_fecha.fechas_venta_acciones(fecha_dt,factor)
    # Cuenta
    x2 = cuenta.cuenta_venta_acciones(socio,factor)
    # Naturaleza
    x3 = naturaleza.naturaleza_venta_acciones(factor)
    # Credito y Debito
    comodin = credito.credito_venta_acciones(cantidad, precio_par, precio, factor, diferencia)
    x4 = comodin[0]
    x5 = comodin[1]

    # Unión de las listas
    y = [x1,x2,x3,x4,x5]
    z=[]
    
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    socio_box.delete(0,END)
    cantidad_box.delete(0,END)
    precio_box.delete(0,END)
    
    close_window(newAcciones)
    add()

def ventana_acciones(accion,precio_par): 
    if accion == 0 or precio_par==0:
        # Toplevel object which will be treated as a new window 
        newAcciones = Toplevel() 
        newAcciones.title("Acciones")  
        newAcciones.geometry("250x100")
        advertencia = Label(newAcciones, text="Error: Aún no se ha creado \nuna Sociedad Anonima",width=50,anchor=W)
        advertencia.grid(row=0,column=0, padx=40, pady=7, columnspan=2)
    else:
        # Toplevel object which will be treated as a new window 
        newAcciones = Toplevel() 
        newAcciones.title("Acciones")  
        newAcciones.geometry("600x500")
        
        # Labels
        acciones_venta = Label(newAcciones, text="Acciones disponibles para la venta "+str(accion),width=50,anchor=CENTER)
        acciones_venta.grid(row=0,column=0, padx=5, pady=7, columnspan=2)
        precio_nominal = Label(newAcciones, text="Precio a la par "+str(round(precio_par,2)),width=50,anchor=CENTER)
        precio_nominal.grid(row=1,column=0, padx=5, pady=7, columnspan=2)
        fl = Label(newAcciones, text="Fecha",width=20,anchor=W)
        fl.grid(row=2,column=0, padx=5, pady=3)
        socio = Label(newAcciones, text="Nombre del socio",width=20,anchor=W)
        socio.grid(row=3,column=0, padx=5, pady=3)
        cantidad = Label(newAcciones, text="Número de acciones",width=20,anchor=W)
        cantidad.grid(row=4,column=0, padx=5, pady=3)
        precio = Label(newAcciones, text="Precio de adquisición",width=20,anchor=W)
        precio.grid(row=5,column=0, padx=5, pady=3)
    
        # Fecha box
        global fecha_box
        fecha_box = Entry(newAcciones)
        fecha_box.grid(row=2,column=1, padx=5, pady=3)
        # Socio box
        global socio_box
        socio_box = Entry(newAcciones)
        socio_box.grid(row=3,column=1, padx=5, pady=3)
        # Cantidad box
        global cantidad_box
        cantidad_box = Entry(newAcciones)
        cantidad_box.grid(row=4,column=1, padx=5, pady=3)
        # Precio box
        global precio_box
        precio_box = Entry(newAcciones)
        precio_box.grid(row=5,column=1, padx=5, pady=3)
    
        venta_acciones = Button(newAcciones, text = "Agregar datos",command=lambda: datos_venta_acciones(newAcciones,accion,precio_par))
        venta_acciones.grid(row=6,column=2,padx=5, pady=3)

"""
Nomina
"""

def datos_nomina(newNomina):
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    trabajador = float(trabajador_box.get())
    salario = float(salario_box.get())
    dotacion = float(dotacion_box.get())
    arl = arl_box.get()
    
    if arl == "Clase I":
        arl = 0.00522
    elif arl =="Clase II":
        arl = 0.01044
    elif arl =="Clase III":
        arl = 0.02436
    elif arl =="Clase IV":
        arl = 0.0435
    elif arl =="Clase V":
        arl = 0.0696
    
    factor = False
    if salario >= 1755606:
        factor = True
    
    if trabajador <= 0  or dotacion <= 0:
        # Toplevel object which will be treated as a new window 
        Errorcantidad = Toplevel() 
        Errorcantidad.title("Error nomina")  
        Errorcantidad.geometry("250x100")
        advertencia = Label(newAcciones, text="Error: Los datos señalados en trabajador \n o en dotacion no son validos",width=50,anchor=W)
        advertencia.grid(row=0,column=0, padx=40, pady=7, columnspan=2)
        close_window(newAcciones)
        return 0
    
    # Restricciones sobre la cantidad de acciones que se pueden vender
    if salario <= 0:
        # Toplevel object which will be treated as a new window 
        Errorcantidad = Toplevel() 
        Errorcantidad.title("Acciones")  
        Errorcantidad.geometry("250x100")
        advertencia = Label(Errorcantidad, text="Error: El salario \nno es valido",width=50,anchor=W)
        advertencia.grid(row=0,column=0, padx=40, pady=7, columnspan=2)
        close_window(newAcciones)
        return 0
    
    # Fecha
    x1 = Cambio_de_fecha.fechas_nomina(fecha_dt,factor)
    # Cuenta
    x2 = cuenta.cuenta_nomina(factor)
    # Naturaleza
    x3 = naturaleza.naturaleza_nomina(factor)
    # Credito y Debito
    comodin = credito.credito_nomina(fecha_dt, trabajador, salario, dotacion, arl,factor)
    x4 = comodin[0]
    x5 = comodin[1]

    # Unión de las listas
    y = [x1,x2,x3,x4,x5]
    z=[]
    
    for i in range(len(x1)):
        w = []
        for j in y:
            w.append(j[i])
        z.append(w)    
    
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    trabajador_box.delete(0,END)
    salario_box.delete(0,END)
    dotacion_box.delete(0,END)
    arl_box.delete(0,END)
    
    close_window(newNomina)
    add()

def ventana_nomina():
    # Toplevel object which will be treated as a new window 
    newNomina = Toplevel() 
    newNomina.title("Nomina")  
    newNomina.geometry("600x500")
    
    # Labels
    fl = Label(newNomina, text="Fecha",width=20,anchor=W)
    fl.grid(row=2,column=0, padx=5, pady=3)
    trabajador = Label(newNomina, text="Número de trabajadores",width=20,anchor=W)
    trabajador.grid(row=3,column=0, padx=5, pady=3)
    salario = Label(newNomina, text="Salario",width=20,anchor=W)
    salario.grid(row=4,column=0, padx=5, pady=3)
    dotacion = Label(newNomina, text="Dotación",width=20,anchor=W)
    dotacion.grid(row=5,column=0, padx=5, pady=3)
    arl = Label(newNomina, text="Tipo Arl",width=20,anchor=W)
    arl.grid(row=6,column=0, padx=5, pady=3)
    


    # Fecha box
    global fecha_box
    fecha_box = Entry(newNomina)
    fecha_box.grid(row=2,column=1, padx=5, pady=3)
    # Socio box
    global trabajador_box
    trabajador_box = Entry(newNomina)
    trabajador_box.grid(row=3,column=1, padx=5, pady=3)
    # Cantidad box
    global salario_box
    salario_box = Entry(newNomina)
    salario_box.grid(row=4,column=1, padx=5, pady=3)
    # Precio box
    global dotacion_box
    dotacion_box = Entry(newNomina)
    dotacion_box.grid(row=5,column=1, padx=5, pady=3)
    global arl_box
    options = ("Clase I","Clase II","Clase III","Clase IV","Clase V")
    arl_box = ttk.Combobox(newNomina, values = options)
    arl_box.grid(row=6,column= 1)
    

    boton_nomina = Button(newNomina, text = "Agregar datos",command=lambda: datos_nomina(newNomina))
    boton_nomina.grid(row=7,column=2,padx=5, pady=3)

class Producto:
    
    def __init__(self):
        self.cantidad = 0 
        self.precio = 0
        self.valor = 0
        
    def sumar(self,cantidad,precio):
        self.cantidad = self.cantidad + cantidad
        self.valor = self.valor + (precio * cantidad)
        self.precio = self.valor / self.cantidad
        
Sillas = Producto()
Mesas = Producto()

"""
Compras Administrativas
"""

def datos_compra_admin(NewCompraAdmin):
    
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    Fecha = Cambio_de_fecha.fecha_compra(fecha_dt)

    cantidad = float(cantidad_box.get())
    precio = float(precio_box.get())
    contado = float(contado_box.get())
    
    Naturaleza = naturaleza.naturaleza_compra_admin()
    Cuenta = cuenta.cuenta_compra_admin()
    
    if contado < 100:
        Fecha.insert(3,fecha_dt)
        Naturaleza.insert(3,"Pasivo")
        Cuenta.insert(3,"Cuentas comerciales por pagar")
    
    iva = iva_box.get()
    if iva == 1:
        Credito = []
        Credito = credito.credito_compra_sin_iva(cantidad,precio,contado)
    elif iva == 2:
        Credito = []
        Credito = credito.credito_compra_iva_incluido(cantidad,precio,contado)
        
    Datos = [Fecha,Naturaleza,Cuenta,Credito[0],Credito[1]]
    
    z = []
    
    for i in range(len(Fecha)):
        w = []
        for j in Datos:
            w.append(j[i])
        z.append(w)    

    for i in range(len(z)):
        my_tree.insert(parent="",index='end', text="Child",values=z[i])

    # Clear the boxes
    fecha_box.delete(0,END)
    cantidad_box.delete(0,END)
    precio_box.delete(0,END)
    contado_box.delete(0,END)
    iva_box.set(None)
    
    close_window(NewCompraAdmin)
    add()  

def ventana_compra_admin():
    
    global NewCompraAdmin
    NewCompraAdmin = Toplevel() 
    NewCompraAdmin.title("Compras Administrativas")  
    NewCompraAdmin.geometry("500x500")
    
    #El usuario ingresa la fecha, la cantidad de unidades compradas, el precio de compra y el porcentaje a pagar de contado.
    
    fecha = Label(NewCompraAdmin, text="Fecha",width=20,anchor=W)
    fecha.grid(row=0,column=0, padx=5, pady=3)
    cantidad = Label(NewCompraAdmin, text="Cantidad",width=20,anchor=W)
    cantidad.grid(row=1,column=0, padx=5, pady=3)
    precio = Label(NewCompraAdmin, text="Precio",width=20,anchor=W)
    precio.grid(row=2,column=0, padx=5, pady=3)
    contado = Label(NewCompraAdmin, text="Pago de contado (%)",width=20,anchor=W)
    contado.grid(row=3,column=0, padx=5, pady=3)

    # Entry boxes
    global fecha_box
    fecha_box = Entry(NewCompraAdmin)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    global cantidad_box
    cantidad_box = Entry(NewCompraAdmin)
    cantidad_box.grid(row=1,column=1, padx=5, pady=3)
    global precio_box
    precio_box = Entry(NewCompraAdmin)
    precio_box.grid(row=2,column=1, padx=5, pady=3)
    global contado_box
    contado_box = Entry(NewCompraAdmin)
    contado_box.grid(row=3,column=1,padx=5,pady=3)
    
    #El usuario puede escoger entre dos opciones: sin IVA y con IVA incluido
    global iva_box
    iva_box = IntVar()
    global sin_iva
    sin_iva = ttk.Radiobutton(NewCompraAdmin,variable = iva_box,text = "Sin IVA",value=1)
    sin_iva.grid(row=4,column=0)
    global con_iva
    con_iva = ttk.Radiobutton(NewCompraAdmin,variable = iva_box,text = "IVA incluido",value=2)
    con_iva.grid(row=4,column=1) 
          
    compra_admin = Button(NewCompraAdmin, text = "Agregar datos",command=lambda: datos_compra_admin(NewCompraAdmin))  
    compra_admin.grid(row=5,column=1,padx=5, pady=3)
    
"""
Datos Comercialización
"""
    
def datos_compra_prod(NewCompraProd):
    
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    Fecha = Cambio_de_fecha.fecha_compra(fecha_dt)

    cantidad = float(cantidad_box.get())
    precio = float(precio_box.get())
    contado = float(contado_box.get())
    
    if mercancia_box.get() == "Sillas":
        Sillas.sumar(cantidad,precio)
    elif mercancia_box.get() == "Mesas":
        Mesas.sumar(cantidad,precio)
    
    Naturaleza = naturaleza.naturaleza_compra_prod()
    Cuenta = cuenta.cuenta_compra_prod()
    texto = "Inventarios" + " (" + mercancia_box.get() + ")"
    Cuenta.insert(1,texto)
    
    if contado < 100:
        Fecha.insert(3,fecha_dt)
        Naturaleza.insert(3,"Pasivo")
        Cuenta.insert(3,"Cuentas comerciales por pagar")
    
    iva = iva_box.get()
    if iva == 1:
        Credito = credito.credito_compra_sin_iva(cantidad,precio,contado)
        
    elif iva == 2:
        Credito = credito.credito_compra_iva_incluido(cantidad,precio,contado)
        
    Datos = [Fecha,Naturaleza,Cuenta,Credito[0],Credito[1]]
        
    z = []
    
    for i in range(len(Fecha)):
        w = []
        for j in Datos:
            w.append(j[i])
        z.append(w)    
        
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[i])
        
    # Clear the boxes
    fecha_box.delete(0,END)
    mercancia_box.delete(0,END)
    cantidad_box.delete(0,END)
    precio_box.delete(0,END)
    contado_box.delete(0,END)
    iva_box.set(None)
    
    close_window(NewCompraProd)
    add()

def ventana_compra_prod(): 

    # Toplevel object which will be treated as a new window 
    global NewCompraProd
    NewCompraProd = Toplevel() 
    NewCompraProd.title("Compras Comercialización")  
    NewCompraProd.geometry("500x500") 
    
     #El usuario ingresa la fecha, la cantidad de unidades compradas, el precio de compra y el porcentaje a pagar de contado.
    
    fecha = Label(NewCompraProd, text="Fecha",width=20,anchor=W)
    fecha.grid(row=0,column=0, padx=5, pady=3)
    mercancia = Label(NewCompraProd, text="Mercancía",width=20,anchor=W)
    mercancia.grid(row=1,column=0,padx=5,pady=3)
    cantidad = Label(NewCompraProd, text="Cantidad",width=20,anchor=W)
    cantidad.grid(row=2,column=0, padx=5, pady=3)
    precio = Label(NewCompraProd, text="Precio",width=20,anchor=W)
    precio.grid(row=3,column=0, padx=5, pady=3)
    contado = Label(NewCompraProd, text="Pago de contado (%)",width=20,anchor=W)
    contado.grid(row=4,column=0, padx=5, pady=3)

   # Entry boxes
    global fecha_box
    fecha_box = Entry(NewCompraProd)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    
    #El usuario escoge qué clase de producto compró
    global mercancia_box
    mercancias = ("Sillas","Mesas")
    mercancia_box = ttk.Combobox(NewCompraProd, values = mercancias)
    mercancia_box.grid(row=1,column= 1)
    global cantidad_box
    cantidad_box = Entry(NewCompraProd)
    cantidad_box.grid(row=2,column=1, padx=5, pady=3)
    global precio_box
    precio_box = Entry(NewCompraProd)
    precio_box.grid(row=3,column=1, padx=5, pady=3)
    global contado_box
    contado_box = Entry(NewCompraProd)
    contado_box.grid(row=4,column=1,padx=5,pady=3)
    
    #El usuario puede escoger entre dos opciones: sin IVA y con IVA incluido
    global iva_box
    iva_box = IntVar()
    sin_iva = ttk.Radiobutton(NewCompraProd,variable = iva_box,text = "Sin IVA",value=1)
    sin_iva.grid(row=5,column=0)
    con_iva = ttk.Radiobutton(NewCompraProd,variable = iva_box,text = "IVA incluido",value=2)
    con_iva.grid(row=5,column=2)   
    
    compra_prod = Button(NewCompraProd, text = "Agregar datos",command= lambda:datos_compra_prod(NewCompraProd))
    compra_prod.grid(row=6,column=1,padx=5, pady=3)
    
"""
Venta de mercancías
"""

def datos_venta(NewVenta):
    
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    Fecha = Cambio_de_fecha.fecha_venta(fecha_dt)
    
    cantidad = float(cantidad_box.get())
    p_venta = float(precio_box.get())
    contado = float(contado_box.get())
    
    Naturaleza = naturaleza.naturaleza_venta()
    Cuenta = cuenta.cuenta_venta()
    texto = "Inventarios (" + mercancia_box.get() + ")"
    Cuenta.insert(0,texto)
    
    if contado < 100:
        Fecha.insert(3,fecha_dt)
        Naturaleza.insert(3,"Activo")
        Cuenta.insert(3,"Cuentas comerciales por cobrar")
        
    if mercancia_box.get() == "Sillas":
        p_compra = Sillas.precio
    elif mercancia_box.get() == "Mesas":
        p_compra = Mesas.precio
    
    metodo = metodo_box.get()
    if metodo == 0:
        Credito = credito.credito_venta_sin_iva(cantidad,p_venta,p_compra,contado)
    elif metodo == 1:
        Credito = credito.credito_venta_iva_incluido(cantidad,p_venta,p_compra,contado)
    elif metodo == 2:
        Credito = credito.credito_venta_margen(cantidad,margen,p_compra,contado)
        
    Datos = [Fecha,Naturaleza,Cuenta,Credito[0],Credito[1]]
    z = []
    
    for i in range(len(Fecha)):
        w = []
        for j in Datos:
            w.append(j[i])
        z.append(w) 
        
    for i in range(len(z)):
        my_tree.insert(parent="",index='end', text="Child",values=z[i])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    mercancia_box.delete(0,END)
    cantidad_box.delete(0,END)
    precio_box.delete(0,END)
    contado_box.delete(0,END)
    metodo_box.set(None)
    
    close_window(NewVenta)
    add()

def ventana_ventas():
    
    global NewVenta
    NewVenta = Toplevel() 
    NewVenta.title("Ventas")  
    NewVenta.geometry("500x500")
    
     #El usuario ingresa la fecha, la cantidad de unidades vendidas, el precio de venta y el porcentaje a cobrar de contado.
    fecha = Label(NewVenta, text="Fecha",width=20,anchor=W)
    fecha.grid(row=0,column=0, padx=5, pady=3)
    mercancia = Label(NewVenta, text="Mercancías",width=20,anchor=W)
    mercancia.grid(row=1,column=0, padx=5, pady=3)
    cantidad = Label(NewVenta, text="Cantidad",width=20,anchor=W)
    cantidad.grid(row=2,column=0, padx=5, pady=3)
    metodo = Label(NewVenta, text="Método",width=20,anchor=W)
    metodo.grid(row=3,column=0, padx=5, pady=3)
    precio = Label(NewVenta,text="Precio / margen",width=20,anchor=W)
    precio.grid(row=6,column=0, padx=5, pady=3)
    contado = Label(NewVenta, text="Pago de contado (%)", width=20, anchor=W)
    contado.grid(row=7,column=0, padx=5, pady=3)

    # Entry boxes        
    
    global fecha_box
    fecha_box = Entry(NewVenta)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    
    #El usuario escoge qué clase de producto vendió
    global mercancia_box
    mercancias = ("Sillas","Mesas")
    mercancia_box = ttk.Combobox(NewVenta, values = mercancias)
    mercancia_box.grid(row=1,column= 1)
    global cantidad_box
    cantidad_box = Entry(NewVenta)
    cantidad_box.grid(row=2,column=1, padx=5, pady=3)
    
    #El usuario puede escoger entre tres opciones para elegir su precio: sin IVA, con IVA incluido o aquel que brinde un margen de utilidad específico.
    global metodo_box
    metodo_box = IntVar()
    sin_iva = ttk.Radiobutton(NewVenta,variable = metodo_box,text = "Por precio de venta (sin IVA)",value=0)
    sin_iva.grid(row=3,column=1)
    con_iva = ttk.Radiobutton(NewVenta,variable = metodo_box,text = "Por precio de venta (IVA incluido)",value=1)
    con_iva.grid(row=4,column=1)
    margen = ttk.Radiobutton(NewVenta,variable = metodo_box, text = "Por margen de utilidad", value=2)
    margen.grid(row=5,column=1)
    global precio_box
    precio_box = Entry(NewVenta)
    precio_box.grid(row=6,column=1, padx=5, pady=3)
    global contado_box
    contado_box = Entry(NewVenta)
    contado_box.grid(row=7,column=1,padx=5,pady=3)
    
    venta = Button(NewVenta, text = "Agregar datos",command= lambda:datos_venta(NewVenta))
    venta.grid(row=8,column=1,padx=5, pady=3)
    
"""
Depreciación
"""
    
def datos_depreciacion(NewDeprecio):
    
    fecha = fecha_box.get()
    fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
    valor = int(valor_box.get())
    meses = int(meses_box.get())
    
    Fecha = Cambio_de_fecha.fecha_depreciacion(fecha_dt,meses)
    Naturaleza = naturaleza.naturaleza_depreciacion(meses)
    Cuenta = cuenta.cuenta_depreciacion(meses)
    
    if metodo_box.get() == "Línea recta":
        Credito = credito.credito_linea_recta(tipo_box.get(),valor,meses)
    elif metodo_box.get() == "Suma creciente":
        Credito = credito.credito_suma_creciente(tipo_box.get(),valor,meses)
    elif metodo_box.get() == "Suma decreciente":
        Credito = credito.credito_suma_decreciente(tipo_box.get(),valor,meses)
        
    Datos = [Fecha,Naturaleza,Cuenta,Credito[0],Credito[1]]
    z = []
    
    for i in range(len(Fecha)):
        w = []
        for j in Datos:
            w.append(j[i])
        z.append(w)    
        
    for i in range(len(z)):
        my_tree.insert(parent="",index='end', text="Child",values=z[i])
        
    # Clear the boxes
    fecha_box.delete(0,END)
    tipo_box.delete(0,END)
    valor_box.delete(0,END)
    meses_box.delete(0,END)
    metodo_box.delete(0,END) 
    
    close_window(NewDeprecio)
    add()

def ventana_depreciacion():
    
    NewDeprecio = Toplevel() 
    NewDeprecio.title("Depreciación")  
    NewDeprecio.geometry("500x500")
    
    #El usuario ingresa la fecha de la compra de un equipo, el valor de la compra
 ,  #y los meses para los cuales quiere hallar la depreciación.
    fecha = Label(NewDeprecio, text="Fecha",width=20,anchor=W)
    fecha.grid(row=0,column=0, padx=5, pady=3)
    tipo = Label(NewDeprecio, text="Tipo",width=20,anchor=W)
    tipo.grid(row=1,column=0, padx=5, pady=3)
    valor = Label(NewDeprecio, text="Valor histórico",width=20,anchor=W)
    valor.grid(row=2,column=0, padx=5, pady=3)
    meses = Label(NewDeprecio, text="Meses",width=20,anchor=W)
    meses.grid(row=3,column=0, padx=5, pady=3)
    metodo = Label(NewDeprecio, text="Método", width=20, anchor=W)
    metodo.grid(row=4,column=0, padx=5, pady=3)
    
    # Entry boxes
    global fecha_box
    fecha_box = Entry(NewDeprecio)
    fecha_box.grid(row=0,column=1, padx=5, pady=3)
    
    #El usuario escoge la categoría a la cual pertenece el equipo.
    global tipo_box
    options1 = ("Vehiculos","Edificios","Muebles y enseres","Equipo de cómputo",
             "Maquinaria y equipo")
    tipo_box = ttk.Combobox(NewDeprecio, values = options1)
    tipo_box.grid(row=1,column= 1)
    global valor_box
    valor_box = Entry(NewDeprecio)
    valor_box.grid(row=2,column=1, padx=5, pady=3)
    global meses_box
    meses_box = Entry(NewDeprecio)
    meses_box.grid(row=3,column=1, padx=5, pady=3)
    
    #El usuario elige el método contable para calcular la depreciación.
    global metodo_box 
    options2 = ("Línea recta","Suma creciente","Suma decreciente")
    metodo_box = ttk.Combobox(NewDeprecio, values = options2)
    metodo_box.grid(row=4,column=1)
        
    depreciacion = Button(NewDeprecio, text = "Agregar datos",command= lambda:datos_depreciacion(NewDeprecio))
    depreciacion.grid(row=5,column=1,padx=5, pady=3)

"""
Cerrar ventana    
"""    

root.mainloop()


