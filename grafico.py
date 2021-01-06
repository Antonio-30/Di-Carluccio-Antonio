# infludiamo questo modulo per creare numeri casuali
from random import randint

# per accedere ad un file devo assegnare
# ad un oggetto il file da aprire, in lettura o scrittura

# associo ad f il file, indico con "w" il tipo di operazione
# così lo aprirà in scrittura (write)

f = open("dati.txt", 'w')

# definiamo una variabile stringa da riempire con i dati che poi scriverò

# inizializzo la stringa
dati = ""

# il primo ciclo serve a creare le singole righe
for riga in range(100):

    # il secondo ciclo serve a compulare la singola riga
    for elemento in range(1):

        # aggiungo il numero casuale e inserisco uno spazio in coda
        dati = dati + str(randint(1,100)) + "," + str(randint(1,100))
    
    # aggiungo un terminatore di riga, così il secondo rigo va a capo
    dati = dati + "\n"

# avremmmo potuto creare una lista di righe:
# lines = [
#...     'prima riga del file\n',
#...     'seconda riga del file\n',
#...     'terza riga del file\n',
#... ]

print(dati)

# scrivo la stringa nel file
f.write(dati)

# chdiuamo sempre il file
f.close()

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

for riga in f:
    valori = str(f.readline())  # converto in stringa la riga
    Nval = len(valori)          # conto il numero di caratteri
    valori = valori.strip('\n') # elimino i lterminatore di riga
    valori = valori.split(',')  # separo la stringa in due numeri
    valori = list(valori)       # converto in lista
    print(valori)
    coordX.append(int(valori[0])) # aggiungo la coordinata X
    coordY.append(int(valori[1])) # aggiungo la coordinata Y

f.close()  # chiudiamo il file

print ("X: ",coordX)
print ("Y: ",coordY)

# ordiniamo le liste
coordX.sort()
coordY.sort()

print("liste ordinate:") 
print ("X: ",coordX)
print ("Y: ",coordY)

# stampo il tipo di dati delle coordinate
print(type(coordX))
print(type(coordY))

# ora sono pronte per essere usate anche nei grafici
plt.scatter(coordX,coordY)
plt.plot(coordX,coordY)
plt.ylabel('some numbers')
plt.show()
