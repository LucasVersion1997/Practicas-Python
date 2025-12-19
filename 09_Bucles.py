### BUCLES / LOOPS ###
#Ejemplo N°1 de bucle - "for"

#clientes = ["Lucas", "Taylor", "Alison", "Swift"]
#for nombre in clientes:
#    print("Analizando datos de:", nombre)

#########

contraseña_real = "python123"

while True:
    contraseña_introducida = input("Introducir contraseña:")
    
    if contraseña_introducida == contraseña_real:
        print("Welcome")
        break
    
    else: 
        print("Error, Contraseña incorrecta")