#LOS CONDICIONALES NOS DICEN, SI LA CONDICION ES TRUE SE CUMPLE, SI LA CONDICION ES FALSA NO SE EJECUTA Y PASA A LA SIGUIENTE.#

edad_texto = input("Cuantos tenes años tenes?")
edad = int(edad_texto) 

if edad >= 18:                                                #Ejemplo de condicional + Input
    print("Bienvenido")
else:
    print("No podes pasar")
    
print("gracias por venir")

#################################

temperatura = 35

if temperatura > 30:
    print("Hace calor")                           #EJEMPLO DE CONDICIONALES IF,ELIF, ELSE.
elif temperatura >15: 
    print("Esta agradable")#
else:
    print("Hace frio")#

####################
                                                          

edad = 15
tiene_licencia=True                                           ##EJEMPLO IF + CONDICIONAL AND

if edad >= 18 and tiene_licencia ==True:
    print("Podes manejar")
else:
    print("No podes manejar")
 
 #-----------------------------------------------
                                                                  
 
alarma_encendida = True
                                                                
if not alarma_encendida:                               ##EJEMPLO DE NOT + condicional
     print("PASA")
else:
    print("Cuidao")

#-------------------------------------
                                                                    

es_estudiante = False
es_jubilado =  True
                                                                
if es_estudiante or es_jubilado:                                  # #EJEMPLO DE OR + Condicional
    print("Tenes 50 de descuento")
else:
    print("Pagas todo")