# EXEPCIONES!!
# NOS SIRVEN COMO ESCUDO PARA QUE EL PROGRAMA NO SE CAIGA CUANDO EL USUARIO GENERA UN ERROR

class Auto:
    def __init__(self, marca, modelo, combustible):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        
    def conducir(self,distancia):
        self.combustible -= distancia
        if self.combustible <= 0:
           self.combustible = 0
           print("Te quedaste sin nafta")
        else:
            print(F"Recorriste {distancia}km. Te quedan {self.combustible} L de combustible")
    
    def cargar_nafta(self,cantidad):
        self.combustible += cantidad
        print(F"Cargaste {cantidad}L")
    
    
Golsito = Auto("Volkswagen", "gol", 100)

while True:
    try:
        km = int(input("Cuantos km queres conducir? o sino 0 para apagar: "))
        if km == 0:
            print("Apagando el motor")
            break
        Golsito.conducir(km)
        
    except ValueError:
        print("❌ ERROR: Porfavor coloca un numero")