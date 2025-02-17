from tkinter import *
import os

print(os.listdir())  # Muestra los archivos en el directorio actual

#Creacion de la ventana raiz y su logo
ventana_Principal = Tk()
ventana_Principal.geometry("289x537")
icono = PhotoImage(file='tamapp_logo.png')
ventana_Principal.iconphoto(True,icono)
ventana_Principal.title("Tamapp")

#Titulo principal de la aplicacion
titulo_Principal = Label(ventana_Principal,text="Tamapp")
titulo_Principal.grid(row=0,column=1)

#Funciones
def ventana_Registro():
    ventana = Toplevel(ventana_Principal)
    mensaje_Ventana_Registro = Label(ventana,text="Ventana de registro de productos")
    mensaje_Ventana_Registro.pack()
    

#Alineacion de los botones
boton_Tamales = Button(ventana_Principal,text="Tamales").grid(row=1,column=0)
boton_Pan = Button(ventana_Principal,text="Pan", command=ventana_Registro).grid(row=2,column=0)
boton_Donas = Button(ventana_Principal,text="Donas").grid(row=3,column=0)
boton_ChampurradoGde = Button(ventana_Principal,text="Champurrado Gde").grid(row=4,column=0)
boton_ChampurradoChi = Button(ventana_Principal,text="Champurrado Chi").grid(row=5,column=0)



#Loop grafico
ventana_Principal.mainloop()
"""
cuenta_total = 0
class Producto():
    
    cantidad = 0
    producto_ID = 0
    def __init__(self,item_ID, cantidad):
        self.producto_ID = item_ID
        self.cantidad = cantidad

    def Calcular_Cuenta(self):
        global cuenta_total
        precio = 0
        if self.producto_ID == 1:
            #Tamales
            precio = 17
        elif self.producto_ID  == 2:
            #Pan dulce
            precio = 12
        elif self.producto_ID  == 3:
            #Donas
            precio = 14
        elif self.producto_ID  == 4:
            #Champurrado grande
            precio = 90
        elif self.producto_ID  == 5:
            #Champurrado chico
            precio = 45
        else:
            print("Producto no reconocido, porfavor vuelva a intentarlo")
            return
            
        cuenta_total += self.cantidad * precio
        return





#inicio del codigo "principal"
print("---------------Tamapp-----------------")
print("Contamos con los siguientes productos:")
print("1)Tamales---------------------$17 (c/u)")
print("2)Pan dulce-------------------$12 (c/u)")
print("3)Donas-----------------------$14 (c/u)")
print("4)Champurrado grande (1 lt)---$90")
print("5)Champurrado chico (1/2 lt)--$45")

pregunta = True
while pregunta == True:
    productoId = int(input("Que producto desea llevar?: "))
    cantidad = int(input("Cuantos desea llevar?: "))

    item1 = Producto(productoId,cantidad)
    item1.Calcular_Cuenta()
    if int(input("¿Desea llevar algo más? 1) Sí  2) No ")) != 1:
        pregunta = False
        print("La cuenta total es de:", cuenta_total)
        cuenta_total = 0

"""