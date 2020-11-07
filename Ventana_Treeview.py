# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:32:30 2020

@author: Windows
"""

from tkinter import *
import pandas as pd
from tkinter import ttk,filedialog
import amortizacion1

root = Tk()
root.title('Contabilidad')
root.geometry("1100x800")

wrapper1 = LabelFrame(root, text="Cuentas T")
wrapper2 = LabelFrame(root, text="Añadir datos")
wrapper3 = LabelFrame(root, text="Funciones contables")

wrapper1.pack(fill="both", expand="yes", padx= 20, pady = 10)
wrapper2.pack(fill="both", expand="yes", padx= 20, pady = 10)
wrapper3.pack(fill="both", expand="yes", padx= 20, pady = 10)

# IMPORTANT LIST
lista_transacciones = []
"""
Add style
"""
style = ttk.Style()
# Pick a theme
style.theme_use('clam')

# Configure treeview colors
style.configure("Treeview",
    background="white",
    foreground="blue",
    rowheight=30,
    fieldbackground="white"
    )
# Change selected color
style.map('Treeview',
    background=[('selected','green')])

"""
Create Treeview Frame
"""

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
    
     
def clear_tree():
    my_tree.delete(*my_tree.get_children())        
        
#Create frame
tree_frame=Frame(wrapper1)
tree_frame.pack(pady=5)

#Scrollbar to the frame
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

# Create Treeview - selectmode("browse","none","extended")
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
# Configure Scrollbar
tree_scroll.config(command=my_tree.yview)

# =============================================================================
# # Create striped row tags
# my_tree.tag_configure('oddrow', background="white")
# my_tree.tag_configure('evenrow', background="lightblue")
# =============================================================================

"""
Functions
"""
# Add record 
def add_record():
    my_tree.insert(parent='', index='end', text="Child",values=[fecha_box.get(),cuenta_box.get(),
                                        naturaleza_box.get(),debito_box.get(), credito_box.get()])
    
    # Clear the boxes
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    
# Remove one selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
# Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
# Remove many
def remove_many():
    for i in my_tree.selection():
        my_tree.delete(i)
        
# Select record
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
# Save updated record
def update_record():
    # Grab index number
    selected = my_tree.focus()
    #Save new data
    my_tree.item(selected,text="",values=(fecha_box.get(),cuenta_box.get(),
                                naturaleza_box.get(),debito_box.get(), credito_box.get()))
    # Clear entry boxes
    fecha_box.delete(0,END)
    cuenta_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)

# Create Binding Click function
def clicker(e):
    select_record()

# Move Row up and down
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

# Funciones contables
def amortizacion():
    amortizacion1.ventana_amortizacion()
    for i in range(len(z)):
        my_tree.insert(parent='', index='end', text="Child",values=z[1])
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
fecha_box.grid(row=0,column=1, padx=5, pady=3)
cuenta_box = Entry(wrapper2)
cuenta_box.grid(row=1,column=1, padx=5, pady=3)
naturaleza_box = Entry(wrapper2)
naturaleza_box.grid(row=2,column=1, padx=5, pady=3)
debito_box = Entry(wrapper2)
debito_box.grid(row=3,column=1, padx=5, pady=3)
credito_box = Entry(wrapper2)
credito_box.grid(row=4,column=1, padx=5, pady=3)

# Buttons
add_record = Button(wrapper2, text = "Add new",command=add_record)
add_record.grid(row=5,column=0,padx=5, pady=3)

update_button = Button(wrapper2,text="Update",command=update_record)
update_button.grid(row=5,column=1,padx=5, pady=3)

delete_record = Button(wrapper2, text = "Delete",command=remove_one)
delete_record.grid(row=5,column=2,padx=5, pady=3)

# Buttons Funciones contables
amortizacion = Button(wrapper3, text = "Amortización",command=amortizacion)
amortizacion.grid(row=5,column=2,padx=5, pady=3)
""" 
Add a menu 
"""
my_menu = Menu(root)
root.config(menu=my_menu)

# Add menu dropdown
# Number 1
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Archivo", menu=file_menu)
file_menu.add_command(label="Open",command=file_open)

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
#my_tree.bind("<ButtonRelease-1>", clicker)

root.mainloop()

