import guizero
import string
import numpy as np
import matplotlib.pyplot as plt

f = open("dati.txt", 'r')

coordX = []
coordY = []

from guizero import *

def tasto0():
    for riga in f:
        valori = str(f.readline())  
        Nval = len(valori)          
        valori = valori.strip('\n')
        valori = valori.split(',')  
        valori = list(valori)      
        print(valori)
        coordX.append(int(valori[0]))
        coordY.append(int(valori[1]))
        output.append(valori)
    f.close()  

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
    plt.grid()
    plt.ylabel('some numbers')
    plt.show()
    plt.savefig("grafico")
    picture = Picture(app, image="grafico")
   

app = App(title='interfaccia-grafico', width=2000, height=1000)

grafico_text = Text(app, text='Grafico', font = 'arial', size=40)

testo = Text(app, text="inserisci il nome del file:", size=15)

whatever = TextBox(app, width=50, multiline=True, height=2)

output = TextBox(app, width=80, height=20, multiline=True)

push1 =PushButton(app, text='definire le coordinate', command=tasto0)

push2 =PushButton(app, text='coordinate', command=tasto1)

push3 = PushButton(app, text='grafico', command=tasto2)

app.bg="#5F9EA0"

grafico_text.text_color ="#FFFFFF"

whatever.bg="#FFFFFF"

push1.bg="#E52B50"

push2.bg="#CC9966"

push3.bg="#5E86C1"

output.bg="#008f39"

app.display()
