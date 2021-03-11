from random import *
a = [[randint(1,100) for x in range(3)],
    [randint(1,100) for x in range(3)],
    [randint(1,100) for x in range(3)]]
print (a[0])
print (a[1])
print (a[2])

domanda=int(input("Quale riga vuoi visualizzare: "))

print(a[domanda])
