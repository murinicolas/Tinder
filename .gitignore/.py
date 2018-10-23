from datos_prueba import dicDatos
from datos_prueba import dicBusq
min = "qwertyuiopasdfghjklñzxcvbnm"
may="QWERTYUIOPASDFGHJKLÑZXCVBNM"
num="1234567890"
gb="_"

def menuPrincipal():
    OpcionesMenuPrincipal = input("""
    (1) CARGAR UN GRUPO DE PERSONAS PREDETERMINADO
    (2) CREAR CUENTA NUEVA
    (3) (opcional) EDITAR INFORMACION DE UNA PERSONA
    (4) INGRESAR AL SISTEMA
    Escriba el numero de opcion deseada: 
    """)

    if OpcionesMenuPrincipal=="1":
        print("hola")
    #cuando cargo el grupo de persona predeterminado este se va a actualizar con "usuariosDeEstructura"
    #llama a la funcion "datos_prueba.base_de_datos_de_prueba()",
    # print(datos_prueba.base_de_datos_de_prueba())	#va a imprimir el diccionario entero, para probar vió.
    elif OpcionesMenuPrincipal == '2':
        crearUsuario()
        filtrarBusquedas()
    #llama una func, la cual sirve para cargar datos, y esto aladirlos al diccionario principal, osea a usuariosDeEstructura
    elif OpcionesMenuPrincipal=='3':
        print("as")
        #llama a una funcion para que sirve para editar la info de una persona
    elif OpcionesMenuPrincipal=='4':
        ingresarSistema()
    else:
        print("Por favor, ingrese una de las opciones")
        menuPrincipal()	#vuelve al menu principal
    return OpcionesMenuPrincipal

def ingresarSistema():
    pseu=str(input("Ingrese su nombre de usuario:"))
    if pseu in dicDatos.keys():
        contraseña=(input("Ingrese su contraseña:"))
        if contraseña in dicDatos[pseu]:
            print("Bienvenide",dicDatos.values()[0])

def filtrarBusquedas():
    pseu = str(input("Vuelva a ingresar su nombre de usuario:"))
    sexoInteres=str(input("Ingrese el/los sexo/s de interes (M, F o A):"))
    sexoInt = definirSexoInt(sexoInteres)
    edadMinima=input("Ingrese la edad mínima del rango de búsqueda:")
    edadMaxima=input("Ingrese la edad máxima del rango de búsqueda:")
    crearRango(edadMinima,edadMaxima)
    dicBusq[pseu]=[sexoInt,[rangoEdad]]

def crearUsuario():
    pseu = str(input("Ingrese nombre de usuario: "))
    validarPseudonimo(pseu)
    contraseña = str(input("Ingrese contraseña: "))
    validarContraseña(contraseña)
    nombre = str(input("Ingrese su/s nombre/s: "))
    apellido = str(input("Ingrese su/s apellido/s: "))
    sexo = str(input("Sexo (M, F o I):"))
    edad = int(input("Ingrese su edad: "))
    validarEdad(edad)
    intereses=str(input("Ingrese separados por espacios y guiones hobbies, intereses, etc. Ej.: 'green-day gatos viajar museos-de-arte"))
    interesesEnListado(intereses)
    dicDatos[pseu]=[nombre,apellido,contraseña,sexo,edad,ubicacion,intereses]
    filtrarBusquedas()
def validarPseudonimo(pseudonimo):
    #revisa que el pseudonimo cumpla las condiciones
    if any(letra.isupper() for letra in pseudonimo)==True:
        print("Usuario inválido, por favor ingrese un usuario que contenga únicamente minúsculas, números y guión bajo.")
        pseudonimo = str(input("Ingrese un pseudonimo nuevo: "))
        validarPseudonimo(pseudonimo)
    elif (any(letra.isdigit() for letra in pseudonimo)==True) or (any(letra=="_" for letra in pseudonimo))==True:
        return True
    else:
        print("Usuario inválido, por favor ingrese un usuario que contenga únicamente minúsculas, números y guión bajo.")
        pseudonimo = str(input("Ingrese un pseudonimo nuevo: "))
        validarPseudonimo(pseudonimo)


    '''for letras in pseudonimo:
        if letras not in (num or min or gb):
            print(letras, "Usuario inválido")
            break'''
def validarContraseña(contraseña):
    #revisa que la contraseña cumpla las condiciones
    for letras in contraseña:
        if letras not in (min or num or may):
            print("Contraseña incorrecta, debe contener al menos una minúscula, una masyucula, un número y 5 caracteres")
            contraseñaNueva=str(input("Ingrese otra contraseña: "))
            validarContraseña(contraseñaNueva)
        else:
            print("Contraseña aceptada")
def validarEdad(edad):
    if edad<18:
        print("Debe tener por lo menos 18 años para registrarse")
        menuPrincipal()
    if edad>99:
        print("Debe tener menos de 99 años para registrarse")
        menuPrincipal()
def interesesEnListado(intereses):
    interesesLista = intereses.split
def crearRango(edadMin,edadMax):
    for x in range(edadMin,edadMax+1):
        rangoEdad=[x]
        return rangoEdad
def definirSexoIn(sexoInteres):
    if sexoInteres=="M":
        sexoInt = "M"
    elif sexoInteres=="F":
        sexoInt = "F"
    else:
        sexoInt=["M","F"]
    return sexoInt


print(menuPrincipal())
