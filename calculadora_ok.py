from tkinter import *
from tkinter import messagebox

ventana = Tk()
ventana.title("Calculadora de Alice")
ventana.config(
    bd=15,
    bg="#ecb9ed"
)
marco = Frame(ventana).grid()
#---------------pantalla-----------------------

numero_pantalla = StringVar()
pantalla = Entry(marco, textvariable=numero_pantalla, bg="black", fg="#7df5db", justify="right"). grid(row=0, column=0, columnspan=4, padx=5, pady=5)

#--------------- marcacion teclado -----------------------

operacion = ""
resultado = 0
nuevo_numero = False
tipo_operacion = ""
 
def valorBoton(valor):
    global operacion
    if operacion != "":
        numero_pantalla.set(valor)
        operacion = ""
    else:
        numero_pantalla.set(numero_pantalla.get()+valor)
        
#--------------- borrado -----------------------
   
def borrar():
    global operacion
    global resultado
    global tipo_operacion
    
    numero_pantalla.set("")
    tipo_operacion = ""
    operacion = ""
    resultado = 0
    
#--------------- operaciones -----------------------
    
def sumar():
    global operacion
    global resultado
    global tipo_operacion
    operacion = "suma"
    resultado += float(numero_pantalla.get())
    numero_pantalla.set(resultado)
    tipo_operacion = "sumado"
    
def resta():
    global operacion
    global resultado
    global tipo_operacion
    
    if resultado == 0:
        resultado = float(numero_pantalla.get())
        operacion = "resta"
    else:
        resultado -= float(numero_pantalla.get())
        operacion = "resta"
    numero_pantalla.set(resultado)
    tipo_operacion = "restado"
    
def Mult():
    global operacion
    global resultado
    global tipo_operacion
    
    if resultado == 0:
        resultado = float(numero_pantalla.get())
        operacion = "multiplica"
    else:
        resultado = resultado * float(numero_pantalla.get())
        operacion = "multiplica"
    numero_pantalla.set(resultado)
    tipo_operacion = "multiplicado"

    
def Div():
    global operacion
    global resultado
    global tipo_operacion
    
    if resultado == 0:
        resultado = float(numero_pantalla.get())
        operacion = "divide"
    else:
        resultado = resultado / float(numero_pantalla.get())
        operacion = "divide"
    numero_pantalla.set(resultado)
    tipo_operacion = "dividido"
    
def Total():
    global operacion
    global resultado
    global tipo_operacion
    
    if tipo_operacion == "sumado":
        operacion = "suma"
        resultado += float(numero_pantalla.get())
        numero_pantalla.set(resultado)
        
    elif tipo_operacion == "restado":
        resultado -= float(numero_pantalla.get())
        operacion = "resta"
        numero_pantalla.set(resultado)
        
    elif tipo_operacion == "multiplicado":
        resultado = resultado * float(numero_pantalla.get())
        operacion = "multiplica"
        numero_pantalla.set(resultado)
        
    elif tipo_operacion == "dividido":
        resultado = resultado / float(numero_pantalla.get())
        operacion = "divide"
        numero_pantalla.set(resultado)

    operacion = "total"
    tipo_operacion = ""



#--------------- primera linea de botones -----------------------

boton7 = Button(marco, text="7", width=3, bg= "#7df5db", command = lambda: valorBoton("7"))
boton7.grid(row=1, column=0, padx=5, pady=5)
boton8 = Button(marco, text="8", width=3, bg= "#7df5db", command = lambda: valorBoton("8"))
boton8.grid(row=1, column=1, padx=5, pady=5)
boton9 = Button(marco, text="9", width=3, bg= "#7df5db", command = lambda: valorBoton("9"))
boton9.grid(row=1, column=2, padx=5, pady=5)
botonDiv = Button(marco, text="÷", width=3, bg= "#7df5db", command= lambda: Div())
botonDiv.grid(row=1, column=3, padx=5, pady=5)

#--------------- segunda linea de botones -----------------------

boton4 = Button(marco, text="4", width=3, bg= "#7df5db", command = lambda: valorBoton("4"))
boton4.grid(row=2, column=0, padx=5, pady=5)
boton5 = Button(marco, text="5", width=3, bg= "#7df5db", command = lambda: valorBoton("5"))
boton5.grid(row=2, column=1, padx=5, pady=5)
boton6 = Button(marco, text="6", width=3, bg= "#7df5db", command = lambda: valorBoton("6"))
boton6.grid(row=2, column=2, padx=5, pady=5)
botonMult = Button(marco, text="x", width=3, bg= "#7df5db", command= lambda: Mult())
botonMult.grid(row=2, column=3, padx=5, pady=5)

#--------------- tercera linea de botones -----------------------

boton1 = Button(marco, text="1", width=3, bg= "#7df5db", command = lambda: valorBoton("1"))
boton1.grid(row=3, column=0, padx=5, pady=5)
boton2 = Button(marco, text="2", width=3, bg= "#7df5db", command = lambda: valorBoton("2"))
boton2.grid(row=3, column=1, padx=5, pady=5)
boton3 = Button(marco, text="3", width=3, bg= "#7df5db", command = lambda: valorBoton("3"))
boton3.grid(row=3, column=2, padx=5, pady=5)
botonRest = Button(marco, text="-", width=3, bg= "#7df5db", command= lambda: resta())
botonRest.grid(row=3, column=3, padx=5, pady=5)

#--------------- cuarta linea de botones -----------------------

boton0 = Button(marco, text="0", width=3, bg= "#7df5db", command = lambda: valorBoton("0"))
boton0.grid(row=4, column=0, padx=5, pady=5)
botonComa = Button(marco, text=",", width=3, bg= "#7df5db")
botonComa.grid(row=4, column=1, padx=5, pady=5)
botonIgual = Button(marco, text="=", width=3, bg= "#7df5db", command= lambda:Total())
botonIgual.grid(row=4, column=2, padx=5, pady=5)
botonSuma = Button(marco, text="+", width=3, bg= "#7df5db", command= lambda:sumar())
botonSuma.grid(row=4, column=3, padx=5, pady=5)


boton_borrado = Button(marco, text="<<<", width=3, bg= "#7df5db", command=borrar)
boton_borrado.grid(row=5, column=2, columnspan=2, padx=5, pady=5, sticky=EW)

ventana.mainloop()

