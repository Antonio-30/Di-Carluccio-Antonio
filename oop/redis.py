import redis
from random import *

r = redis.StrictRedis(host='10.255.237.211', port=6379, password='1357642rVi0', db=0)

f = open("FileGioco.txt", "w") # apre il file in scrittura

D = dict(key1=10, key2=20, key3=30) # dizionario
r.keys() # inizializzo la lista delle chiavi del DB

for k, v in D.items(): #ciclo legge valori dizionario
    r.set(k, v) # scrive nel database: r.set('chiave, "valore')
    f.write(k+","+str(v)+"\n") # scrive nel file, poichè accetta solo stringhe si utilizza str() per il value
f.close() # chiude il file

valueDB = r.get('key2'); print(valueDB) # legge e visualizza un valore del database

f = open("FileGioco.txt", "r") # apre il file in lettura
print(f.read()) # legge e visualizza tutto il contenuto del file (f.readline() per leggere una riga alla volta)
