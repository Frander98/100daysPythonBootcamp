from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=500, height=500)
#Change the icon in the window
#iconphoto(False, PhotoImage(file='path'))

#Labels
label = Label(text="This is old text")
label.config(text="This is new text")
label.pack()

#Buttons
def action():
    print("Do something")

#calls action() when pressed
button = Button(text="Click Me", command=action)
button.pack()

#Entries
entry = Entry(width=30)
#Add some text to begin with
entry.insert(END, string="Some text to begin with.")
#Gets text in entry
print(entry.get())
entry.pack()

#Text
text = Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# Layout managers object.pack() --> Ordena los objetos en una distribución lógica, es poco flexible para posisciones
# precisas. object.place(x=x, y=y) --> Es el más preciso de todos, recibe las coordenadas exactas de "x" y de "y".
# object.grid(column=column, row=row) --> Divide la ventana en filas y columnas y dispone los elementos de acuerdo al
# ...número de columnas que uno disponga, las posiciones son relativas entre los elementos.
# metodo columnspan: Se usa para expandir un elemento mas de una columna, ejemplo:
# object.grid(column=column, row=row, columnspan=2) En este ejemplo, el objeto se ocupa 2 columnas del layout
#Para una mejor explicacion de columnspan ver: https://replit.com/@Frander/grid-columnspan-demo#main.py

# padding : es una manera de agregar margenes externos a los elementos con respecto a la ventana (Ejemplo 1), también se puede
# agregar margenes a un elemento especifico (Ejemplo 2).
# Ejemplo 1: window.config(padx=x, pady=y)
# Ejemplo 2: object.config(padx=x, pady=y)

#Canvas
#Canvas es un lienzo que nos permite dibujar en 2D diferentes objetos al delimitar un área especifica de la ventana para ello.
#Crear un canvas:
#Canvas(width=ancho, height=alto)
#Agregar una imagen al canvas: 
#imagen = PhotoImage(file="ruta_de_la_iamgen")
#canvas.create_image(100, 100, image=imagen) , las coordenadas indican la posicion en que queremos ubicar la imagen.
#Agregar texto a el canvas:
#canvas.create_text(113, 135, text="00:00", font=(FONT_NAME, 31, "bold"), fill="white"), las coordenadas indican la posicion en que queremos ubicar el texto.


#Articulo de interes para repasar este tema:
#https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/
window.mainloop()

