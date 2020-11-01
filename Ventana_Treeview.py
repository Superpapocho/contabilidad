# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 11:32:30 2020

@author: Windows
"""

from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Contabilidad')
root.geometry("1000x800")

# Add style
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

# Create Treeview Frame
tree_frame=Frame(root)
tree_frame.pack(pady=5)
#Scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT,fill=Y)

# Create Treeview - selectmode("browse","none","extended")
my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
# Pack to the screen
my_tree.pack(pady=10)

#Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)

# Define our columns
my_tree['columns'] = ("Fecha","Descripcion","Naturaleza","Debito","Credito")

# Format our columns
my_tree.column("#0",width=0, stretch=NO)
my_tree.column("Fecha",anchor=W, width=100)
my_tree.column("Descripcion",anchor=CENTER, width=160)
my_tree.column("Naturaleza",anchor=W, width=160)
my_tree.column("Debito",anchor=W, width=140)
my_tree.column("Credito",anchor=W, width=140)

# Create Headings
my_tree.heading("#0",text="Label",anchor=W)
my_tree.heading("Fecha", text="Fecha", anchor=W)
my_tree.heading("Descripcion", text="Descripcion",anchor=CENTER)
my_tree.heading("Naturaleza",text="Naturaleza",anchor=W)
my_tree.heading("Debito", text="Débito", anchor=W)
my_tree.heading("Credito", text="Crédito", anchor=W)

# Add data
data = [
        (35,"Venta","Ingreso","50000",""),
        (52,"Compra","Activo","70000",""),
        (13,"Capital suscrito","Patrimonio","90000",""),
        (36,"Cuentas por cobrar","Pasivo","","52400"),
        (76,"Arrendamiento","Gasto","","100000"),
        (35,"Venta","Ingreso","50000",""),
        (52,"Compra","Activo","70000",""),
        ]


# Create striped row tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

global count
count = 0
for i in range(6):
    for record in data:
        if count%2==1:
            my_tree.insert(parent='', index='end', iid=count, text="",values=record,tags=('oddrow')) #Se insertara la tupla de las funciones contables
        else:
            my_tree.insert(parent='', index='end', iid=count, text="",values=record,tags=('evenrow'))
        count += 1

# =============================================================================
# # Add child
# my_tree.insert(parent='', index='end', iid=2, text="Child",values=(33,"Carlitos","Pasivo","5000",""))
# my_tree.move('2', '0', '0')
# =============================================================================

# Create treeview frame
add_frame = Frame(root)
add_frame.pack(pady=0)

# Labels
fl = Label(add_frame, text="Fecha")
fl.grid(row=0,column=0)
desl = Label(add_frame, text="Descripción")
desl.grid(row=0,column=1)
nl = Label(add_frame, text="Naturaleza")
nl.grid(row=0,column=2)
debl = Label(add_frame, text="Débito")
debl.grid(row=0,column=3)
cl = Label(add_frame, text="Crédito")
cl.grid(row=0,column=4)

# Entry boxes
fecha_box = Entry(add_frame)
fecha_box.grid(row=1,column=0)
descripcion_box = Entry(add_frame)
descripcion_box.grid(row=1,column=1)
naturaleza_box = Entry(add_frame)
naturaleza_box.grid(row=1,column=2)
debito_box = Entry(add_frame)
debito_box.grid(row=1,column=3)
credito_box = Entry(add_frame)
credito_box.grid(row=1,column=4)

#Add record function
def add_record():
    global count
    if count%2==1:
        my_tree.insert(parent='', index='end', iid=count, text="Child",values=(fecha_box.get(),descripcion_box.get(),
                                                        naturaleza_box.get(),debito_box.get(), credito_box.get()),tags=('oddrow'))
    else:
        my_tree.insert(parent='', index='end', iid=count, text="Child",values=(fecha_box.get(),descripcion_box.get(),
                                                        naturaleza_box.get(),debito_box.get(), credito_box.get()),tags=('evenrow'))
    count += 1
    # Clear the boxes
    fecha_box.delete(0,END)
    descripcion_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)

# Remove all records
def remove_all():
    for record in my_tree.get_children():
        my_tree.delete(record)
# Remove one selected
def remove_one():
    x = my_tree.selection()[0]
    my_tree.delete(x)
# Remove many
def remove_many():
    for i in my_tree.selection():
        my_tree.delete(i)
# Select record
def select_record():
    # Clear entry boxes
    fecha_box.delete(0,END)
    descripcion_box.delete(0,END)
    naturaleza_box.delete(0,END)
    debito_box.delete(0,END)
    credito_box.delete(0,END)
    # Grab index number
    selected = my_tree.focus()
    # Grab record values (or an specific column)
    values = my_tree.item(selected, 'values')

    fecha_box.insert(0, values[0])
    descripcion_box.insert(0,values[1])
    naturaleza_box.insert(0,values[2])
    debito_box.insert(0,values[3])
    credito_box.insert(0,values[4])
# Save updated record
def update_record():
    # Grab index number
    selected = my_tree.focus()
    #Save new data
    my_tree.item(selected,text="",values=(fecha_box.get(),descripcion_box.get(),
                                naturaleza_box.get(),debito_box.get(), credito_box.get()))
    # Clear entry boxes
    fecha_box.delete(0,END)
    descripcion_box.delete(0,END)
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
    ind=len(my_tree.get_children())
    print(len(my_tree.get_children()))
    limit(rows,ind,"down")

# Buttons - Funciones contables a través de command
move_up= Button(root,text="Move Up",command=up)
move_up.pack(pady=10)

move_down= Button(root,text="Move Down",command=down)
move_down.pack(pady=10)

select_button = Button(root,text="Select Record",command=select_record)
select_button.pack(pady=10)

update_button = Button(root,text="Save record",command=update_record)
update_button.pack(pady=10)

add_record = Button(root, text = "Add record",command=add_record)
add_record.pack(pady=10)

# Remove all
remove_all = Button(root,text="Remove all", command=remove_all)
remove_all.pack(pady=10)

# Remove one
remove_one = Button(root,text="Remove one",command=remove_one)
remove_one.pack(pady=10)
# Remove selected
remove_many = Button(root,text="Remove selected", command=remove_many)
remove_many.pack(pady=10)
# Bindings
# my_tree.bind("<Double-1>", clicker)
my_tree.bind("<ButtonRelease-1>", clicker)

root.mainloop()
