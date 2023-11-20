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
class Nodo:
    def __init__(self, valor) -> None:
        self.valor = valor
        self.siguiente = None

    def __str__(self):
        return str(self.valor)

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.contador = 0
    def insertar_inicio(self, dato) -> None:
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.contador += 1

    def insertar_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza == None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.contador += 1

    def insertar_dentro(self, dato, posicion):
        nuevo_nodo = Nodo(dato)
        actual = self.cabeza
        indice = 0
        while actual != None:
            if indice == posicion:
                anterior = actual
                siguiente = actual.siguiente
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = siguiente
                return
            indice += 1
            actual = actual.siguiente
        self.contador += 1

    def eliminar_primero(self):
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            valor = self.cabeza.valor
            self.cabeza = None
            self.cola = None
            self.contador -= 1
            return valor
        else:
            valor = self.cabeza.valor
            segundo = self.cabeza.siguiente
            self.cabeza.siguiente = None
            self.cabeza = segundo
            self.contador -= 1
            return valor


    def eliminar_final(self):
        actual = self.cabeza
        if self.cabeza == None:
            raise Exception("Lista enlazada vacia")
        if self.cabeza == self.cola:
            valor = self.cabeza.valor
            self.cabeza = None
            self.cola = None
            self.contador -= 1
            return valor
        else:
            while actual != None:
                if actual.siguiente == self.cola:
                    break
                actual = actual.siguiente
            valor = self.cola.valor
            actual.siguiente = None
            self.cola = actual
            self.contador -= 1
            return valor



    def eliminar_dentro(self, dato):
        actual = self.cabeza
        anterior = None
        while actual != None:
            if actual.siguiente.valor == dato:
                anterior = actual
                actual = actual.siguiente
                break
            actual = actual.siguiente
        anterior.siguiente = actual.siguiente
        self.contador -= 1

    def buscar(self, valor):
        actual = self.cabeza
        while actual != None:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        actual = self.cabeza
        while actual != None:
            print(actual.valor, end=" - ")
            actual = actual.siguiente
        print("None")

    def bubble_sort(self):
        if not self.cabeza:
            return

        while True:
            swapped = False
            actual = self.cabeza
            previo = None

            while actual.siguiente:
                siguiente = actual.siguiente
                if actual.valor > siguiente.valor:
                    # Realiza el intercambio de nodos
                    if previo:
                        previo.siguiente = siguiente
                    else:
                        self.cabeza = siguiente

                    actual.siguiente = siguiente.siguiente
                    siguiente.siguiente = actual
                    if self.cola.valor <= actual.valor:
                        self.cola = actual
                    swapped = True
                elif actual.valor <= siguiente.valor:
                    self.cola = siguiente
                    
                previo = actual
                actual = siguiente

            if not swapped:
                break

    def insertar_ordenadamente(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = self.cabeza
            self.contador += 1

        elif self.cabeza == self.cola:
            if valor <= self.cabeza.valor:
                nuevo_nodo.siguiente = self.cola
                self.cabeza = nuevo_nodo
                self.contador += 1
            else:
                self.cabeza.siguiente = nuevo_nodo
                self.cola = nuevo_nodo
                self.contador += 1
        else:
            if valor <= self.cabeza.valor:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
                self.contador += 1
                return
            actual = self.cabeza
            while actual.siguiente and valor > actual.siguiente.valor:
                actual = actual.siguiente

            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            if valor >= self.cola.valor:
                self.cola = nuevo_nodo
            self.contador += 1

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
            self.buckets[i] = ListaEnlazada()

        for i in array:
            indiceBucket = self.funcionHash(i, self.bucketRango, self.numeroBuckets)
            self.insertar(i, indiceBucket)

        for i in self.buckets:
            i.bubble_sort()

        lista_ordenada = []

        for i in self.buckets:
            rango = i.contador
            for j in range(rango):
                lista_ordenada.append(i.eliminar_primero())
        self.buckets = []
        return lista_ordenada


    def insertar_ordenado(self, valor, indice):
        self.buckets[indice].insertar_ordenadamente(valor)

    def insertar(self, valor, indice):
        self.buckets[indice].insertar_final(valor)

    def funcionHash(self, num, valorhash, numerodebuckets):
        indice = num // valorhash #indice de insercion
        if indice >= numerodebuckets:
            indice = numerodebuckets - 1
        return int(indice)

""" Bucket Sort Implementacion fin"""

bucketsort = BucketSort()

aleatorios = random.Random()

tiempo_axis_y = []
tamanio_axis_x = []
lista2 = []

for n in range(1,11):
    datosbase = 5000
    tamanio = datosbase * pow(n,2)
    for i in range(tamanio): #llenar la lista
        lista2.append(aleatorios.randint(1,100000))

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
print(x_log_n_values)
#plt.scatter(x_values, x_log_n_values, s= 200, label="n * log(n)")

plt.scatter(tamanio_axis_x, tiempo_axis_y, s= 200, edgecolors="red")
plt.xlabel("Tamaño de entrada")
plt.xlabel("Tiempo")
plt.title("Grafico de ejecucion BucketSort")
plt.legend()

plt.show()
