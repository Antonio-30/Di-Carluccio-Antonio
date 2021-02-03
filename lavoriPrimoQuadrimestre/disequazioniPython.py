a = int(input("quanto vale a"))

b = int(input("quanto vale b"))

c = int(input("quanto vale c"))

import math

delta = pow(b,2)-4*a*c

if delta < 0:

    print("non ci sono soluzioni")

elif delta > 0:
    print(str("ci sono 2 suluzioni reali"))
    print(int((-b)-(math.sqrt(delta))) / (2*a))
    print(int((-b)+(math.sqrt(delta))) / (2*a))      
