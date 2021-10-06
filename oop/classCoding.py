class serieTvNetflix:

    # Attributi di Classe
    numeroSerieTv = 616

    #Metodo costruttore
    def __init__(self, titolo, puntate, anno, stagioni, luogo):

        # Attributi di Istanza
        self.titolo = titolo
        self.puntate = puntate
        self.anno = anno
        self.stagioni = stagioni
        self.luogo = luogo
       
    #Metodo di tipo Get
    def scheda(self):
        return f'\nScheda "{self.titolo}"\n puntate: {self.puntate}\n Anno: {self.anno}\n stagioni: {self.stagioni}\n luogo: {self.luogo}'
   
serie1=serieTvNetflix("Squid Game",10,2021,1,"Corea del Sud")

serie2=serieTvNetflix("Stranger Things",25,2016,3,"Usa")

serie3=serieTvNetflix("Dark",26,2017,3,"Germania")

print("Il tipo di variabile costruita è: ")
print(serie1)
print(serie2)
print(serie3)

print("\nLa singola scheda è: ")
print (serie1.scheda())
print (serie2.scheda())
print (serie3.scheda())
