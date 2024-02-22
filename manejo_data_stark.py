from data_stark import*

# Desafío #00:

# A. Analizar detenidamente el set de datos
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
# C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a
# la altura del mismo
# D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
# F. Recorrer la lista y determinar la altura promedio de los superhéroes
# (PROMEDIO)
# G. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (MÁXIMO, MÍNIMO)
# H. Calcular e informar cual es el superhéroe más y menos pesado.
# I. Ordenar el código implementando una función para cada uno de los valores
# informados.
# J. Construir un menú que permita elegir qué dato obtener

# Desafío #01:
# Agregar al código elaborado para cumplir el desafío #00 los siguientes puntos,
# utilizando un menú que permita acceder a cada uno de los puntos por separado.
# A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género M
# B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
# género F
# C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
# D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
# E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
# F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
# G. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género M
# H. Recorrer la lista y determinar la altura promedio de los superhéroes de
# género F
# I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
# indicadores anteriores (ítems C a F)
# J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
# K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
# L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
# no tener, Inicializarlo con ‘No Tiene’).
# M. Listar todos los superhéroes agrupados por color de ojos.
# N. Listar todos los superhéroes agrupados por color de pelo.
# O. Listar todos los superhéroes agrupados por tipo de inteligencia


def analisis_datos(lista, clave_nombre, clave_identidad, clave_empresa, clave_altura, clave_peso, clave_genero, clave_color_ojos, clave_color_pelo, clave_fuerza, clave_inteligencia):
    print("     Nombre         |           Identidad           |    Empresa    |       Altura       |        Peso        | Género |       Color de ojos      | Color de pelo | Fuerza | Inteligencia")
    print("--" * 94)  # Línea separadora

    for superheroe in lista:
        nombre = superheroe[clave_nombre]
        identidad = superheroe[clave_identidad]
        empresa = superheroe[clave_empresa]
        altura = superheroe[clave_altura]
        peso = superheroe[clave_peso]
        genero = superheroe[clave_genero]
        color_ojos = superheroe[clave_color_ojos]
        color_pelo = superheroe[clave_color_pelo]
        fuerza = superheroe[clave_fuerza]
        inteligencia = superheroe[clave_inteligencia]

        # Formatear los datos en una línea
        linea_titulos = f"{nombre:<19} | {identidad:<29} | {empresa:<12} | {altura:<18} | {peso:<18} | {genero:<6} | {color_ojos:<24} | {color_pelo:<13} | {fuerza:<6} | {inteligencia}"
        print(linea_titulos)

def imprimir_nombres(lista, clave_nombre):
    contador = 0
    for superheroes in lista:
        nombre = superheroes[clave_nombre]
        contador += 1
        print (f"{contador}). Nombre: {nombre}")

def imprimir_nombre_altura(lista, clave_nombre, clave_altura):
    
    contador = 0
    print("Los superheroes son: \n")
    for superheroe in lista:
        nombre = superheroe[clave_nombre]
        altura = superheroe[clave_altura]
        contador += 1
        (print (f"{contador}). Nombre: {nombre}; altura: {float(altura):.2f}"))
    return

def determinar_mas_alto(lista, clave_nombre, clave_altura):
    mas_alto = ""
    altura_max = 0
    for superheroe in lista:
        altura = float(superheroe[clave_altura])
        if altura > altura_max:
            altura_max = altura
            mas_alto = superheroe[clave_nombre]
    return mas_alto

def determinar_mas_bajo(lista, clave_nombre, clave_altura):
    mas_bajo = ""
    altura_min = float("inf")
    for superheroe in lista:
        altura = float(superheroe[clave_altura])
        if altura < altura_min:
            altura_min = altura
            mas_bajo = superheroe[clave_nombre]
    return mas_bajo

def altura_promedio(lista, clave_altura):
    acu_alturas = 0
    for superheroes in lista:
        acu_alturas += float(superheroes[clave_altura])
    
    promedio_alturas = acu_alturas/len(lista)
    return promedio_alturas
    
def nombre_mas_alto_mas_bajo(lista, clave_nombre, clave_altura):
    mas_alto = determinar_mas_alto(lista, clave_nombre, clave_altura)
    mas_bajo = determinar_mas_bajo(lista, clave_nombre, clave_altura)
    print(f"Los superheroes son: \n El mas bajo es: {mas_bajo}\n El mas alto es: {mas_alto}")

def mas_y_menos_pesados(lista, clave_nombre, clave_peso):
    mas_pesado = ""
    peso_max = 0
    for superheroes in lista:
        peso = float(superheroes[clave_peso])
        if peso > peso_max:
            peso_max = peso
            mas_pesado = superheroes[clave_nombre]
    
    menos_pesado = ""
    peso_min = float("inf")
    for superheroe in lista:
        peso = float(superheroe[clave_peso])
        if peso < peso_min:
            peso_min = peso
            menos_pesado = superheroe[clave_nombre]

    print(f"El superheroe mas pesado es: {mas_pesado} y su peso es: {peso_max:.2f}\nEl superheroe menos pesado es: {menos_pesado} y su peso es: {peso_min:.2f}")

def imprimir_heroes_masculinos(lista, clave_nombre, clave_genero):
    superheroes_M = []
    contador_superheroes = 0
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "M":
            nombre = superheroe[clave_nombre]
            superheroes_M.append(nombre)
    print("Los superheroes del genero masculino son: \n")
    for superheroe in superheroes_M:
        contador_superheroes += 1
        print(f"Los superheroes del genero masculino son: /n {contador_superheroes}) {superheroe}")

def imprimir_heroe_femenino(lista, clave_nombre, clave_genero):
    superheroes_F = []
    contador_superheroes = 0
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "F":
            nombre = superheroe[clave_nombre]
            superheroes_F.append(nombre)
    print("Los superheroes del genero femenino son: \n")
    for superheroe in superheroes_F:
        contador_superheroes += 1
        print(f"{contador_superheroes}) {superheroe}")

def superheroe_mas_alto_M(lista, clave_nombre, clave_altura, clave_genero):
    superheroes_M = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "M":
            nombre = superheroe[clave_nombre]
            altura = superheroe[clave_altura]
            superheroes_M.append({"nombre" : nombre, "altura" : altura})

    mas_alto_masculino = determinar_mas_alto(superheroes_M, "nombre", "altura")
    
    return mas_alto_masculino

def superheroe_mas_alto_F(lista, clave_nombre, clave_altura, clave_genero):
    superheroes_F = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "F":
            nombre = superheroe[clave_nombre]
            altura = superheroe[clave_altura]
            superheroes_F.append({"nombre" : nombre, "altura" : altura})

    mas_alto_femenino = determinar_mas_alto(superheroes_F, "nombre", "altura")
    return mas_alto_femenino

def superheroe_mas_bajo_M(lista, clave_nombre, clave_altura, clave_genero):
    superheroes_M = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "M":
            nombre = superheroe[clave_nombre]
            altura = superheroe[clave_altura]
            superheroes_M.append({"nombre" : nombre, "altura" : altura})

    mas_bajo_masculino = determinar_mas_bajo(superheroes_M, "nombre", "altura")
    
    print(f"El superheroe mas bajo del genero masculino es: \n {mas_bajo_masculino}")

def superheroe_mas_bajo_F(lista, clave_nombre, clave_altura, clave_genero):
    superheroes_F = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "F":
            nombre = superheroe[clave_nombre]
            altura = superheroe[clave_altura]
            superheroes_F.append({"nombre" : nombre, "altura" : altura})

    mas_bajo_femenino = determinar_mas_bajo(superheroes_F, "nombre", "altura")
    
    return mas_bajo_femenino

def altura_promedio_genero_M(lista, clave_genero, clave_altura):
    superheroes_M = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "M":
            altura = superheroe[clave_altura]
            superheroes_M.append({"genero" : genero, "altura" : altura})
    
    return altura_promedio(superheroes_M, "altura")

def altura_promedio_genero_F(lista, clave_genero, clave_altura):
    superheroes_F = []
    for superheroe in lista:
        genero = superheroe[clave_genero]
        if genero == "F":
            altura = superheroe[clave_altura]
            superheroes_F.append({"genero" : genero, "altura" : altura})
    
    return altura_promedio(superheroes_F, "altura")

def mostrar_superheroe_mas_alto_masculino_y_mas_bajo_femenino(lista, clave_nombre, clave_genero, clave_altura):
    
    print("El superheroe masculino mas alto es: " + superheroe_mas_alto_M(lista, "nombre", "altura", "genero")) 
    print("El superheroe mas bajo femenino es: " + superheroe_mas_bajo_F(lista, "nombre", "altura", "genero"))
    
def determinar_superheroes_por_color_de_ojos(lista, clave_nombre, clave_color_ojos):
    
    conteo_colores_ojos = {}
    for superheroe in lista:
        color_ojos = superheroe[clave_color_ojos]
        nombre = superheroe[clave_nombre]
        
        if color_ojos not in conteo_colores_ojos:
            conteo_colores_ojos[color_ojos] = {"count": 1, "nombres": [nombre]}
        else:
            conteo_colores_ojos[color_ojos]["count"] += 1
            conteo_colores_ojos[color_ojos]["nombres"].append(nombre)
    
    return conteo_colores_ojos

def determinar_superheroes_por_color_de_pelo(lista, clave_nombre, clave_color_pelo):
        
    conteo_colores_pelo = {}
    for superheroe in lista:
        color_pelo = superheroe[clave_color_pelo]
        nombre = superheroe[clave_nombre]

        if color_pelo not in conteo_colores_pelo:
            conteo_colores_pelo[color_pelo] = 1
        else:
            conteo_colores_pelo[color_pelo] += 1
            conteo_colores_pelo[color_pelo]["nombres"].append(nombre)

    return conteo_colores_pelo

def determinar_superheroes_por_tipo_de_inteligencia(lista, clave_nombre, clave_inteligencia):
    conteo_tipo_inteligencia = {}
    
    for superheroe in lista:
        tipo_inteligencia = superheroe[clave_inteligencia]
        nombre = superheroe[clave_nombre]
        
        if tipo_inteligencia == "":
            tipo_inteligencia = "No tiene"
        
        if tipo_inteligencia not in conteo_tipo_inteligencia:
            conteo_tipo_inteligencia[tipo_inteligencia] = {"count": 1, "nombres": [nombre]}
        else:
            conteo_tipo_inteligencia[tipo_inteligencia]["count"] += 1
            conteo_tipo_inteligencia[tipo_inteligencia]["nombres"].append(nombre)
    
    return conteo_tipo_inteligencia

def mostrar_superheroes_por_color_de_ojos(lista, clave_nombre, clave_color_ojos):

    conteo_colores_ojos = determinar_superheroes_por_color_de_ojos(lista, clave_nombre, clave_color_ojos)
    for color, data in conteo_colores_ojos.items():
        count = data["count"]
        nombres = data["nombres"]
        
        print(f" \n Color de ojos: {color}")
        print(f"Número de superhéroes con este color de ojos: {count}")
        print("Nombres de superhéroes:")
        
        for nombre in nombres:
            print(f"  - {nombre}")

def mostrar_superheroes_por_color_de_pelo(lista, clave_nombre, clave_color_pelo):
    
    conteo_colores_pelo = determinar_superheroes_por_color_de_pelo(lista, clave_nombre, clave_color_pelo)
    for color_de_pelo, data in conteo_colores_pelo.items():
        count = data["count"]
        nombres = data["nombres"]
        
        print(f" \n Color de pelo: {color_de_pelo}")
        print(f"Número de superhéroes con este color de pelo: {count}")
        print("Nombres de superhéroes:")
        
        for nombre in nombres:
            print(f"  - {nombre}")

def mostrar_superheroes_por_tipo_de_inteligencia(lista, clave_nombre, clave_inteligencia):
    
    conteo_tipo_inteligencia= determinar_superheroes_por_tipo_de_inteligencia(lista, clave_nombre, clave_inteligencia)
    for inteligencia, data in conteo_tipo_inteligencia.items():
        count = data["count"]
        nombres = data["nombres"]
        
        print(f" \n Tipo de inteligencia: {inteligencia}")
        print(f"Número de superhéroes con este tipo de inteligencia: {count}")
        print("Nombres de superhéroes:")
        
        for nombre in nombres:
            print(f"  - {nombre}")



def obtener_opcion():
    match opcion:
        case "A":
            analisis_datos(lista_personajes)
        case "B":
            imprimir_nombres(lista_personajes, "nombre")
        case "C":
            imprimir_nombre_altura(lista_personajes, "nombre", "altura")
        case "D":
            print(determinar_mas_alto(lista_personajes, "nombre", "altura"))
        case "E":
            print(determinar_mas_bajo(lista_personajes, "nombre", "altura"))
        case "F":
            altura_promedio(lista_personajes, "altura")
        case "G":
            nombre_mas_alto_mas_bajo(lista_personajes, "nombre", "altura")
        case "H":
            mas_y_menos_pesados(lista_personajes, "nombre", "peso")
        case "I":
            imprimir_heroes_masculinos(lista_personajes, "nombre", "genero")
        case "J":
            imprimir_heroe_femenino(lista_personajes, "nombre", "genero")
        case "K":
            superheroe_mas_alto_M(lista_personajes, "nombre", "altura", "genero")
        case "L":
            superheroe_mas_alto_F(lista_personajes, "nombre", "altura", "genero")
        case "M":
            superheroe_mas_bajo_M(lista_personajes, "nombre", "altura", "genero")
        case "N":
            superheroe_mas_bajo_F(lista_personajes, "nombre", "altura", "genero")
        case "Ñ":
            altura_promedio_genero_M(lista_personajes, "genero", "altura")
        case "O":
            altura_promedio_genero_F(lista_personajes, "genero", "altura")
        case "P":
            mostrar_superheroe_mas_alto_masculino_y_mas_bajo_femenino(lista_personajes, "nombre", "altura", "genero")
        case "Q":
            determinar_superheroes_por_color_de_ojos(lista_personajes, "nombre", "color_ojos")
        case "R":
            determinar_superheroes_por_color_de_pelo(lista_personajes, "nombre", "color_pelo")
        case "S":
            print(determinar_superheroes_por_tipo_de_inteligencia(lista_personajes, "nombre", "inteligencia"))
        case "T":
            mostrar_superheroes_por_color_de_ojos(lista_personajes, "nombre", "color_ojos")
        case "U":
            mostrar_superheroes_por_color_de_pelo(lista_personajes, "nombre", "color_pelo")
        case "V":
            mostrar_superheroes_por_tipo_de_inteligencia(lista_personajes, "nombre", "inteligencia")
        case _:
            print("Opcion invalida")

continuar = True
while continuar:
    print("\n *****----Menu de Opciones----****\n")
    print("A) Mostrar para analizar el set de datos")
    print("B) Imprimir los nombres de los superheroes")
    print("C) Imprimir nombre y altura de los superheroes")
    print("D) Determinar y mostrar cual es el superheroe mas alto")
    print("E) Determinar y mostrar cual es el superheroe mas bajo")
    print("F) Determinar y mostrar la altura promedio entre los superheroes")
    print("G) Determinar y mostrar los nombres del superheroe mas alto y del mas bajo")
    print("H) Determinar y mostrar los nombres del superheroe mas pesado y del menos pesado")
    print("I) Imprimir los nombres de los superheroes de genero masculino")
    print("J) Imprimir los nombres de los superheroes de genero femenino")
    print("K) Imprimir cual es el superheroe mas alto del genero masculino")
    print("L) Imprimir cual es el superheroe mas alto del genero femenino")
    print("M) Imprimir cual es el superheroe mas bajo del genero masculino")
    print("N) Imprimir cual es el superheroe mas bajo del genero femenino")
    print("Ñ) Determinar y mostrar la altura promedio de los superheroes del genero masculino")
    print("O) Determinar y mostrar la altura promedio de los superheroes del genero femenino")
    print("P) Imprimir el nombre del superheroe mas alto del genero masculino y el mas bajo del genero femenino")
    print("Q) Determinar cuantos superheroes tienen cada tipo de color de ojos")
    print("R) Determinar cuantos superheroes tienen cada tipo de color de pelo")
    print("S) Determinar cuantos superheroes tienen cada tipo de inteligencia")
    print("T) Mostar todos los superhéroes agrupados por color de ojos")
    print("U) Mostar todos los superhéroes agrupados por color de pelo")
    print("V) Mostar todos los superhéroes agrupados por tipo de inteligencia")
    opcion = input("\nSeleccione una opcion(A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V): ").upper()
    opcion = obtener_opcion()
    while True:
        continuar = input("Desea continuar (s/n): ").lower()
        if continuar == "s":
            opcion = input("\nSeleccione la opcion de la informacion que desea ahora: ").upper()
            opcion = obtener_opcion()
        elif continuar == "n":
            continuar = False
            print("Ha salido del programa")
            break
        else:
            print("Ha ingresado un dato invalido")
            


