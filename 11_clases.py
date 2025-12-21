### CLASES ### 
# LAS CLASES NOS SIRVE PARA DEFINIR CIERTO AMBITO, EL CODIGO QUE ESTE DENTRO DE ESE AMBITO VA A TENER CIERTAS CARACTERISTICAS. 
# LO DEFINIMOS COMO: 
#class Person:
 #   pass           #El pass nos sirve para que no nos tire error, y dejar para escribir codigo dsp 

# EJEMPLO N°1

#class Celular:
 #   def __init__(self,marca,modelo):
  #      self.marca= marca
   #     self.modelo= modelo

#mi_celu = Celular("Samsung", "S23")
#tu_celu = Celular("Apple", "Iphone 15")

#print(f"mi celu es un {tu_celu.marca}" )


##### EJEMPLO N°2

#class Producto:
#    def __init__(self, Nombre, Precio):
#        self.Nombre = Nombre
#        self.Precio = Precio
        
#    def aplicar_descuento(self, porcentaje):
#        descuento = self.Precio * (porcentaje / 100)
#        self.Precio = self.Precio - descuento
#        print(f"Nuevo precio de {self.Nombre}: ${self.Precio}")
        
#Remera = Producto("Remera taylor", 100)
#Remera.aplicar_descuento(10)

### EJEMPLO N°3

class Personaje:
    def __init__(self, nombre, vida):
        self.name = nombre
        self.vida = vida
    
    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            print(f"💀 {self.name} ha sido derrotado")
        else:
            print(f" {self.name} ahora tiene {self.vida} de vida")

guerrero = Personaje("suduky",100)
guerrero.recibir_daño(40)
guerrero.recibir_daño(70)