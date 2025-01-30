from tkinter import *
from tkinter import ttk

class venta():
    nombre = ""
    producto_Id = 0
    cantidad = 0
    precio = 0
    costo_Final = 0

    def __init__(self,producto_Id,cantidad):
        self.producto_Id = producto_Id
        self.cantidad = cantidad

    def cuenta_Final(self,costo):
        self.costo_Final = self.costo_Final + costo
        
    def imprimir_Cuenta_Final(self):
        print("La cuenta final es de: $",self.costo_Final)

    def levantar_Pedido(self):
        
        costo= 0
        if self.producto_Id == 1:
            self.nombre = "Tamales"
            self.precio = 17
        if self.producto_Id == 2:
            self.nombre = "Pan dulce"
            self.precio = 12
        if self.producto_Id == 3:
            self.nombre = "Donas"
            self.precio = 14
        if self.producto_Id == 4:
            self.nombre = "Champurrado grande"
            self.precio = 90
        if self.producto_Id == 5:
            self.nombre = "Champurrado chico"
            self.precio = 45

        costo = self.precio * self.cantidad
        self.cuenta_Final(costo)
        #print("Lleva:",self.cantidad,"de",self.nombre,"el monto a pagar es:",costo)
        
        

#inicio del codigo "principal"
print("---------------Tamapp-----------------")
print("Contamos con los siguientes productos:")
print("1)Tamales---------------------$17 (c/u)")
print("2)Pan dulce-------------------$12 (c/u)")
print("3)Donas-----------------------$14 (c/u)")
print("4)Champurrado grande (1 lt)---$90")
print("5)Champurrado chico (1/2 lt)--$45")

pregunta = "s" #Variable para while

while pregunta == "s":
    productoId = int(input("Que producto desea llevar?: "))
    cantidad = int(input("Cuantos desea llevar?: "))
    ventaVariable = venta(productoId,cantidad)
    ventaVariable.levantar_Pedido()
    itera = int(input("Desea llevar algo mas? 1)Si 2)No"))
    if  itera == 1:
        ventaVariable.levantar_Pedido()
    else: 
        ventaVariable.imprimir_Cuenta_Final()
        pregunta = "x"

    






""""
tamales = Productos("Tamales", 17,12)
tamales.datos()
tamales.calc_Costo()
 

root = Tk()
root.title("Tamapp")

frame1 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame1.grid(column=0, row=0, sticky= (N, W, E, S))

frame2 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame2.grid(column=0, row=1, sticky= (N, W, E, S))

frame3 = ttk.Frame(root,width=300, height=200, padding="20 20 20 20")
frame3.grid(column=0, row=2, sticky= (N, W, E, S))


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.mainloop()

"""