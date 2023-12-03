""" Librerias para realizar los graficos """
import numpy as np
import matplotlib.pyplot as plt
""" Librerias para medir el tiempo de ejecucion """
import random
import time

""" Bucket Sort Implementacion """
""" Se implementará con un array como contenedor de buckets,
 para los buckets se usará listas enlazadas y
 para ordenar cada bucket se utilizará Bubble Sort"""
class NodoDoble:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

    def __str__(self):
        return self.valor

class ListaDobleEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0

    def agregar_al_principio(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.contador += 1
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
            self.contador += 1

    def agregar_al_final(self, valor):
        nuevo_nodo = NodoDoble(valor)
        if self.cola is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
            self.contador += 1
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
            self.contador += 1

    def eliminar_al_principio(self):
        if self.cabeza is None:
            return

        if self.cabeza == self.cola:
            retornar = self.cabeza
            self.cabeza = None
            self.cola = None
            self.contador -= 1
            return retornar
        else:
            retornar = self.cabeza
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
            self.contador -= 1
            return retornar

    def eliminar_al_final(self):
        if self.cola is None:
            return

        if self.cabeza == self.cola:
            retornar = self.cabeza
            self.cabeza = None
            self.cola = None
            self.contador -= 1
            return retornar
        else:
            retornar = self.cola
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.contador -= 1
            return retornar

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" <-> ")
            actual = actual.anterior
        print("None")

    def insertion_sort(self): #
        if self.contador == 0:
            return
        saver = self.cabeza
        actual = self.cabeza
        previo = actual.anterior
        while saver:
            if previo:
                if actual.valor <= self.cola.valor:
                    self.cola = actual
                while previo and previo.valor < actual.valor:

                    actual.anterior = previo.anterior
                    if actual.anterior:
                        actual.anterior.siguiente = actual
                    previo.siguiente = actual.siguiente
                    if previo.siguiente:
                        previo.siguiente.anterior = previo
                    actual.siguiente = previo
                    previo.anterior = actual


                    previo = actual.anterior
                    if not previo:
                        self.cabeza = actual

            saver = saver.siguiente
            if saver:
                actual = saver
                previo = actual.anterior


class BucketSort:
    def __init__(self):
        self.numeroBuckets = None
        self.buckets = []
        self.globalMax = None
        self.globalMin = None
        self.rango = None
        self.bucketRango = None

    def ordenar(self, array):
        if len(array) <= 1: # caso edge
            return

        self.numeroBuckets = len(array) // 2  # tamaño promedio eficiente
        self.buckets = [None] * self.numeroBuckets # arreglar!
        self.globalMax = max(array)  # rango minimo # o(n)
        self.globalMin = min(array)  # rango maximo # o(n)
        self.rango = self.globalMax - self.globalMin  # rango final
        self.bucketRango = self.rango / self.numeroBuckets # rango para funcion hash

        for i in range(self.numeroBuckets): # Crear Buckets: tiempo y espacio O(n/2)
            self.buckets[i] = ListaDobleEnlazada()

        for i in array: # insercion: tiempo O(n) y espacio O(k*n)
            indiceBucket = self.funcionHash(i, self.bucketRango, self.numeroBuckets)
            self.insertar(i, indiceBucket)

        for i in self.buckets: #ordenar: tiempo O(n^2/k) == O(k^2/k)
            i.insertion_sort()

        lista_ordenada = []

        for i in self.buckets:
            rango = i.contador
            for j in range(rango):
                lista_ordenada.append(i.eliminar_al_final().valor)
        #regresar valores originales
        self.numeroBuckets = None
        self.buckets = []
        self.globalMax = None
        self.globalMin = None
        self.rango = None
        self.bucketRango = None
        return lista_ordenada


    #def insertar_ordenado(self, valor, indice):
    #    self.buckets[indice].insertar_ordenadamente(valor)

    def insertar(self, valor, indice):
        self.buckets[indice].agregar_al_final(valor)

    def funcionHash(self, num, valorhash, numerodebuckets):
        indice = num // valorhash #indice de insercion
        if indice >= numerodebuckets:
            indice = numerodebuckets - 1
        return int(indice)

    def ordenar_peor_caso(self, array):
        bucket = ListaDobleEnlazada()

        for valor in array:
            bucket.agregar_al_final(valor)

        bucket.insertion_sort()

        resultado = []

        for i in range(len(array)):
            resultado.append(bucket.eliminar_al_final())

        return resultado

""" Bucket Sort Implementacion fin"""


""" --------------------------------------------------------- """

"""
Analisis de complejidad temporal:
Mejor Caso:
    En el mejor caso, la complejidad temporal de Bucket Sort podría aproximarse a O(n + k), 
    donde "n" es el número total de elementos y "k" es el número de buckets. 
    Esto se debe a que, en el mejor caso, cada bucket se ordena eficientemente con 
    Insertion Sort debido a la distribución uniforme, y luego se combinan para obtener 
    la salida final.

    Distribución Balanceada:
    Los elementos están distribuidos de manera que los buckets tengan una carga equilibrada. 
    Aunque no sean exactamente iguales, evitar extremos como un bucket con muchos más 
    elementos que los demás.
    
    Pequeño Número de Elementos por Bucket:
    Los buckets contienen un número moderado de elementos. 
    Si un bucket contiene muy pocos o demasiados elementos, puede afectar el 
    rendimiento del algoritmo.

Peor Caso:
    El peor caso ocurre cuando todos los elementos de la lista de entrada 
    terminan en un solo bucket. 
    En esta situación, la distribución de los elementos en los buckets no es equitativa, 
    y el algoritmo de Insertion Sort tendrá que ordenar un conjunto completo de 
    elementos en lugar de distribuir la carga entre varios buckets. 
    Esto lleva a un rendimiento subóptimo y resulta en un peor caso para la 
    complejidad de tiempo.
    
    En este escenario, el rendimiento del algoritmo se degrada y se asemeja al 
    rendimiento del algoritmo de ordenación cuadrática cuando se trabaja 
    con un solo conjunto grande de datos.
    
    La complejidad de tiempo en el peor caso para Bucket Sort con 
    Insertion Sort es influenciada principalmente por el algoritmo de 
    ordenación utilizado dentro de los buckets. En este caso, se acerca a O(n^2)
    donde n es el número total de elementos.

Caso Promedio:
    En general, si asumimos que la distribución de elementos es aleatoria y uniforme 
    entre los buckets, y si la estrategia de asignación de elementos es eficiente, 
    el caso promedio puede aproximarse a un rendimiento más cercano al mejor 
    caso O(n+(n^2)/k) == O(n+k) donde n es el número total de elementos y k es el número de buckets.

Complejidad espacio propio:
En mejor caso: O(n+k)
En peor caso: O(n)
En caso promedio: O(n+k)
"""

"""
Aplicacion de benchmarking promedio:
Se crearan 10 arrays con datos aletarios entre 1 y 10000.
el tamaño de estos va aumentando segun la formula t = 5000 * i^2
siendo "i" un iterador que aumenta de 1 en 1 y empeiza en 1
y luego se aplicara Bucket Sort a estos
"""

bucketsort = BucketSort()
aleatorios = random.Random()

"""Eplicacion basica inicio"""


#lista1 = [12, 9, 24, 4, 19, 21, 14, 6, 2, 16]
#print(lista1)
#lista1 = bucketsort.ordenar(lista1)
#print()
#print(lista1)

"""Eplicacion basica fin"""

"""Implementacion caso promedio"""
tiempo_axis_y = []
tamanio_axis_x = []
lista2 = []

for n in range(1,11):
    datosbase = 5000
    tamanio = datosbase * pow(n,2)
    for i in range(5): #llenar la lista
        lista2 = [aleatorios.randint(1,10000) for _ in range(tamanio)]
    inicio_tiempo = time.time()
    lista2 = bucketsort.ordenar(lista2)
    fin_tiempo = time.time()
    tiempo_transcurrido = fin_tiempo - inicio_tiempo
    tiempo_axis_y.append(tiempo_transcurrido)
    tamanio_axis_x.append(len(lista2))
    print(f"Loop: {n} || Datos: {tamanio} || Tiempo de ejecución: {tiempo_transcurrido:.10f} segundos")
    lista2 = []
    print()

plt.scatter(tamanio_axis_x, tiempo_axis_y, s= 200)
plt.xlabel("Tamaño de entrada")
plt.xlabel("Tiempo")
plt.title("Grafico de ejecucion BucketSort")

plt.show()


"""
Implementacion peor y mejor de los casos
"""

#array_sizes = [10, 100, 1000, 5000]
#best_case_times = []
#worst_case_times = []
#
#for size in array_sizes:
#    #arr_best = list(range(size))
#    #arr_worst = list(range(size, 0, -1))
#    arr_best = []
#    arr_worst = []
#
#    for i in range(len(array_sizes)):
#        arr_best = [aleatorios.randint(1,1000) for _ in range(array_sizes[i])] #arreglar
#        arr_worst = [aleatorios.randint(1, 1000) for _ in range(array_sizes[i])]
#
#    # Mejor de los casos
#    start_time = time.time()
#    arr_best = bucketsort.ordenar(arr_best)
#    end_time = time.time()
#    best_case_times.append(end_time - start_time)
#
#    # El peor de los casos
#    start_time = time.time()
#    arr_worst = bucketsort.ordenar_peor_caso(arr_worst)
#    end_time = time.time()
#    worst_case_times.append(end_time - start_time)
#
#plt.plot(array_sizes, best_case_times, label='Mejor de los casos')
#plt.plot(array_sizes, worst_case_times, label='El peor de los casos')
#plt.xlabel('Tamaño del array')
#plt.ylabel('Tiempo (segundos)')
#plt.title('Bucket Sort el mejor y peor caso')
#plt.legend()
#plt.show()
#