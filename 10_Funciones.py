# LAS FUNCIONES: NOS SIRVEN PARA ASIGNARLE TAREAS Y NO TENER QUE ESTAR ESCRIBIENDO MIL VECES EL CODIGO
# LAS DEFINIMOS CON "def" + saludar (): -----> def, nombre, parentesis y : 
# LA EJECUTAMOS POR SU NOMBRE: saludar ()

#def calcular_iva(precio):
#    impuesto = precio * 0.21
#    total = precio + impuesto
#    print("El precio con IVA es:", total)
    
#calcular_iva(50)

###########################

def validar(dato_ingresado, dato_guardado):
    return dato_ingresado == dato_guardado

usuario_guardado = "Lucas"
contraseña_guardada = "Superlogico"

while True:
    input_usuario = input("Ingrese Usuario:  ")
    if validar(input_usuario, usuario_guardado):
        print("✅ Usuario correcto")
        break
    else:
        print("❌ El usuario no existe")
        
while True:
    input_contraseña = input("Ingrese contraseña:  ")
    if validar(input_contraseña,contraseña_guardada):
        print("🔓 Acceso Total. ¡Bienvenido al sistema Full Stack!")
        break
    else:
        print("⚠️ Contraseña incorrecta, intente de nuevo.")