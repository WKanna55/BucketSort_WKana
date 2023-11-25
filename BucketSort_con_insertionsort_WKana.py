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

    def insertion_sort(self):
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
        self.numeroBuckets = len(array) // 2  # tamaño promedio eficiente
        self.buckets = [None] * self.numeroBuckets
        self.globalMax = max(array)  # rango minimo
        self.globalMin = min(array)  # rango maximo
        self.rango = self.globalMax - self.globalMin  # rango final
        self.bucketRango = self.rango / self.numeroBuckets # rango para funcion hash

        for i in range(self.numeroBuckets):
            self.buckets[i] = ListaDobleEnlazada()

        for i in array:
            indiceBucket = self.funcionHash(i, self.bucketRango, self.numeroBuckets)
            self.insertar(i, indiceBucket)

        for i in self.buckets:
            i.insertion_sort()

        lista_ordenada = []

        for i in self.buckets:
            rango = i.contador
            for j in range(rango):
                lista_ordenada.append(i.eliminar_al_final())
        self.buckets = []
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

""" Bucket Sort Implementacion fin"""

bucketsort = BucketSort()
""" --------------------------------------------------------- """
aleatorios = random.Random()

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

x_values = tamanio_axis_x
x_log_n_values = [val * np.log(val) for val in x_values]
#print(x_log_n_values)
#plt.scatter(x_values, x_log_n_values, s= 200, label="n * log(n)")

plt.scatter(tamanio_axis_x, tiempo_axis_y, s= 200)
plt.xlabel("Tamaño de entrada")
plt.xlabel("Tiempo")
plt.title("Grafico de ejecucion BucketSort")

plt.show()

""" --------------------------------------------------------- """

#linkedList = ListaDobleEnlazada()
#
#linkedList.agregar_al_final(3)
#linkedList.agregar_al_final(1)
#linkedList.agregar_al_final(2)
#linkedList.agregar_al_final(15)
#linkedList.agregar_al_final(6)
#linkedList.agregar_al_final(20)
#linkedList.agregar_al_final(9)
#linkedList.agregar_al_final(1)
#linkedList.agregar_al_final(16)
#linkedList.agregar_al_final(16)
#
#linkedList.imprimir_adelante()
#
#linkedList.insertion_sort()
#
#linkedList.imprimir_adelante()