""" Librerias para realizar los graficos """
import pandas as pd
import matplotlib.pyplot as plt

""" Librerias para medir el tiempo de ejecucion """
import random
import time

""" Bucket Sort Implementacion """
""" Se implementará con un array como contenedor de buckets,
 para los buckets se usará listas enlazadas y
 para ordenar cada bucket se utilizará Quick Sort"""


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


    def quick_sort(self):
        if self.contador <= 1:
            return self
        lista_menor = ListaEnlazada()
        lista_mayor = ListaEnlazada()

        pivote = self.cabeza
        actual = pivote.siguiente
        while actual:
            if actual.valor > pivote.valor:
                lista_mayor.insertar_final(actual.valor)
            elif actual.valor <= pivote.valor:
                lista_menor.insertar_final(actual.valor)
            actual = actual.siguiente

        lista_resultado = self.concatenar_quick_sort(
            lista_menor.quick_sort(), pivote, lista_mayor.quick_sort())
        self.cabeza = lista_resultado.cabeza
        self.cola = lista_resultado.cola
        return self

    def concatenar_quick_sort(self, ll_menor, pivote, ll_mayor):
        lista_resultado = ListaEnlazada()

        if ll_menor.contador == 0 and ll_mayor.contador == 0:
            lista_resultado.insertar_final(pivote.valor)
            return lista_resultado

        elif ll_menor.contador == 0:
            lista_resultado.insertar_final(pivote.valor)
            if ll_mayor.contador == 0:
                return lista_resultado
            else:
                actual = ll_mayor.cabeza
                while actual:
                    lista_resultado.insertar_final(actual.valor)
                    actual = actual.siguiente
                return lista_resultado
        else:
            actual = ll_menor.cabeza
            while actual:
                lista_resultado.insertar_final(actual.valor)
                actual = actual.siguiente

            lista_resultado.insertar_final(pivote.valor)

            if ll_mayor.contador == 0:
                return lista_resultado
            else:
                actual = ll_mayor.cabeza
                while actual:
                    lista_resultado.insertar_final(actual.valor)
                    actual = actual.siguiente
                return lista_resultado

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
        self.bucketRango = self.rango / self.numeroBuckets  # rango para funcion hash
        for i in range(self.numeroBuckets):
            self.buckets[i] = ListaEnlazada()

        for i in array:
            indiceBucket = self.funcionHash(i, self.bucketRango, self.numeroBuckets)
            self.insertar(i, indiceBucket)

        for i in self.buckets:
            i.quick_sort()

        lista_ordenada = []

        for i in self.buckets:
            rango = i.contador
            for j in range(rango):
                lista_ordenada.append(i.eliminar_primero())
        self.buckets = []
        return lista_ordenada

    #def insertar_ordenado(self, valor, indice):
    #    self.buckets[indice].insertar_ordenadamente(valor)

    def insertar(self, valor, indice):
        self.buckets[indice].insertar_final(valor)

    def funcionHash(self, num, valorhash, numerodebuckets):
        indice = num // valorhash  # indice de insercion
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


plt.scatter(tamanio_axis_x, tiempo_axis_y, s= 200)
plt.xlabel("Tamaño de entrada")
plt.xlabel("Tiempo")
plt.title("Grafico de ejecucion BucketSort")
plt.show()
