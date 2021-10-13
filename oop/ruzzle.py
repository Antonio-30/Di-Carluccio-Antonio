class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        try:
            self.__stringa=str(self.__stringa)

        except ValueError:
            print("errore, inserisci una parola)")
       
    def combUtil(self):
        f = open("C:/Users/Antonio/Desktop/coding/4E/words.italian.txt, 'r')
        for riga in f:

           p=f.readline()

           if self.__stringa in p:
               print("è una parola italiana")
           #else:
               #print("non è una parola italiana")

casa=calcComb("casa")
casa.combUtil()
