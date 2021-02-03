import guizero
import string
import numpy as np
import matplotlib.pyplot as plt



# apriamo il file in lettura
f = open("dati.txt", 'r')

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe



from guizero import App, Text, TextBox, PushButton, Picture

def tasto0():
    for riga in f:
        valori = str(f.readline())  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y
        output.append(int(valori[0]))
        output.append(int(valori[1]))
    f.close()  # chiudiamo il file

def tasto1():
    print ("X: ",coordX)
    print ("Y: ",coordY)
    coordX.sort()
    coordY.sort()
    print("liste ordinate:")
    print ("X: ",coordX)
    print ("Y: ",coordY)
    print(type(coordX))
    print(type(coordY))
    output.append(coordX)
    output.append(coordY)


def tasto2():
    plt.scatter(coordX,coordY)
    plt.plot(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()
    plt.savefig("grafico.png")
    picture = Picture(app, image="grafico.png")
    output.append(picture)

app = App(title='interfaccia-grafico')

grafico_text = Text(app, text='Grafico', font = 'arial', size=40)

whatever = TextBox(app, width=50, multiline=True, height=2)
whatever.value='Interfaccia grafico'

output = TextBox(app, width=80, height=10, multiline=True)

push1 =PushButton(app, text='definire le coordinate', command=tasto0)

push2 =PushButton(app, text='coordinate', command=tasto1)

push3 = PushButton(app, text='grafico', command=tasto2)

app.bg="#000000"

grafico_text.text_color ="#FFFFFF"

whatever.bg="#FFFFFF"

push1.bg="#E52B50"

push2.bg="#CC9966"

push3.bg="#5E86C1"

output.bg="#008f39"

app.display()
