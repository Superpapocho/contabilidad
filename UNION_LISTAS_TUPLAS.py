# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 20:02:15 2020

@author: Windows
"""

x1 =["asd","asd","asd"]
x2 =["qwe","qwe","qwe"]  
x3 =["zxc","zxc","zxc"]
x4 =["tyu","tyu","tyu"]
x5 =["958","tyu","tyu"] 

y = [x1,x2,x3,x4,x5]
z=[]
for i in range(len(x1)):
    w = []
    for j in y:
        w.append(j[i])
    z.append(w)    
print(z)
