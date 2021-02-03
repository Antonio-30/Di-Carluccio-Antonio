#lavoro svolto da:
#Antonio Di Carluccio
#Lorenzo Di Gennaro
#Andrea Gurrado
#Renato Montella

#scrivi file
from random import randint

f = open("dati.txt", 'w')

dati = ""

for riga in range(100):

    for elemento in range(1):

        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
   
    dati = dati + "\n"

print(dati)

f.write(dati)

f.close()

#interfaccia
import guizero
import string
import numpy as np
import matplotlib.pyplot as plt

f = open("dati.txt", 'r')

coordX = []
coordY = []

from guizero import *

def tasto():
    for riga in f:
        valori = str(riga)
        valori = valori.strip('\n')
        valori = valori.split(',')
        valori = list(valori)
        print(valori)
        coordX.append(int(valori[0]))
        coordY.append(int(valori[1]))

    f.close()  

    print ("X: ",coordX)
    print ("Y: ",coordY)

    coordX.sort()
    coordY.sort()
    print("liste ordinate:")
    print ("X: ",coordX)
    print ("Y: ",coordY)
    print(type(coordX))
    print(type(coordY))

    plt.scatter(coordX,coordY)
    plt.plot(coordX,coordY)
    plt.grid()
    plt.ylabel('some numbers')
    plt.savefig("grafico.png")
    picture = Picture(app, image="grafico.png")
   

app = App(title='interfaccia-grafico', width=2000, height=1000, bg="#5F9EA0")

grafico_text = Text(app, text='Grafico', font = 'arial', size=40)

testo = Text(app, text="inserisci il nome del file:", size=15)

file = TextBox(app, width=100)

push3 = PushButton(app, text='grafico', command=tasto)

grafico_text.text_color ="#D8BFD8"

push3.bg="#FFDEAD"

app.display()
