"""
    ELABORADO POR YADIR VEGA ESPINOZA
    ESTUDIANTE: MATEMÁTICAS E INGENIERÍA EN COMPUTACIÓN EN TECNOLÓGICO DE COSTA RICA
    CORREO: yadir.sve@gmail.com
    Celular: +506 86711794

    Cualquier sugerencia o corrección será bienvenida.
    ¡Espero sea de gran ayuda!


    Descripción: Este programa permite multiplicar matrices donde una es
                 de nxp y la otra pxm, la cantidad de filas y columnas
                 las define el usuario y las entradas de la matriz son
                 números reales aleatorios donde los extremos del intervalo
                 los define el usuario.
"""


#Librerías
import random


#Funciones
def crearMatrizAleatoria(n,p,a,b):
    """
        Recibe: 4 parametros, 2 que corresponden a la cantidad
                de filas y columnas que desea para crear una
                matriz y los otros dos son los extremos del
                intervalo del cual se tomarán los valores para
                llenar la matriz aleatoriamente.
                
        Proceso: crea una matriz de n filas y p columnas con valores
                 aleatorios.

        Salida: una matriz.
    """
                    
    matriz = []
    for i in range(n):
        matriz.append([])
        for j in range(p):
            matriz[i].append(random.randint(a,b))
    return matriz


def valida_producto_matricial(A,B):
    """
        Recibe: 2 matrices
                
        Proceso: verifica que la cantidad de columnas de la primer matriz sean  iguales a la cantidad de filas de la segunda matriz:
                 (Condición de producto matricial)

        Salida: valor booleano, True si es posible multiplicar y False en caso de que no.
    """
    filas = len(B)
    columnas = len(A[0])
    if filas == columnas:
        return True
    else:
        return False

def multiplicar_matrices(A,B):
    """
        Recibe: 2 matrices
                
        Proceso: multiplica las 2 matrices ingresadas

        Salida: una matriz.
    """
    filas_resultado = len(A)
    columnas_resultado = len(B[0])

    if valida_producto_matricial(A,B) == True:
        resultado = crearMatrizAleatoria(filas_resultado,columnas_resultado,0,0)
        for i in range(filas_resultado):
            for j in range(columnas_resultado):
                for k in range(len(B)):
                    resultado[i][j] += A[i][k] * B[k][j]
        return resultado

    else:
        return "\n---------------------------------------\nLas matrices ingresadas no cumplen con\nlas condiciones de la multiplicación\nmatricial\n---------------------------------------\n"
   
               
    

def imprimir_matriz_bonita(matriz,letra):
    """
        Recibe: 1 matriz
                
        Proceso: imprime de forma elegante una matriz

        Salida: una cadena de texto.
    """
    if type(matriz)==list:
        mostrar = letra + " ="
        for i in range(len(matriz)):
            mostrar += "\t\t" + str(matriz[i]) + "\n"
    
        return mostrar
    else:
        return matriz
            



# ------------------------------------------ Ejemplo -------------------------------------------------#
try:
    print("\nPrograma que multiplica 2 matrices (A x B)\n\n")

    #Dimensiones de la matriz A
    filas1 = int(input("Ingrese la cantidad de filas para la matriz A: "))
    columnas1 = int(input("Ingrese la cantidad de columnas para la matriz A: "))


    #Dimensiones de la matriz B
    filas2 = int(input("Ingrese la cantidad de filas para la matriz B: "))
    columnas2 = int(input("Ingrese la cantidad de columnas para la matriz B: "))

    #Intervalo para llenar las matrices
    a = int (input ("El inicio del rango de sus números es: "))
    b = int (input ("El final del rango de sus números es: "))

    # Se crea y llena matriz A
    A = crearMatrizAleatoria(filas1,columnas1,a,b)

    # Se crea y llena matriz B
    B = crearMatrizAleatoria(filas2,columnas2,a,b)

    # Se multiplican las matrices y se guarda en resultado
    resultado = multiplicar_matrices(A,B)

    # Salto de linea para que se vea mejor
    print("\n\n")

    # Imprimo bonito la matriz A 
    print(imprimir_matriz_bonita(A,"A"))

    # Imprimo bonito la matriz B
    print(imprimir_matriz_bonita(B,"B"))

    # Imprimo bonito el resultado
    print(imprimir_matriz_bonita(resultado,"A X B"))

except Exception as e:
    print("\n\n---------------------------------------\nNo es posible realizar la operación\n---------------------------------------\n")


# -------------------------------------- FIN DEL PROGRAMA -------------------------------------------#


