import random
import time
import numpy as np
import matplotlib.pyplot as plt
def bucket_sort(array):
    num_buckets = (len(array)//2)
    max_val = max(array)  # o(n)
    min_val = min(array)  # o(n)

    bucketRango = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in array: # insertar los numeros de entrada en los buckets || O(n)
        indiceHash = int((num / bucketRango).__floor__())
        if indiceHash >= len(buckets):
            indiceHash = len(buckets) - 1
        buckets[indiceHash].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array = sorted_array + bucket

    return sorted_array

def bucket_sort_peor(array):
    num_buckets = (len(array) // 2)
    max_val = max(array)  # o(n)
    min_val = min(array)  # o(n)

    bucketRango = (max_val - min_val) / num_buckets

    buckets = [[] for _ in range(num_buckets)]

    for num in array:  # insertar los numeros de entrada en los buckets || O(n)
        buckets[0].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array = sorted_array + bucket

    return sorted_array

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
lista = []

for n in range(1,6):
    datosbase = 5000
    tamanio = datosbase * pow(n,2)
    for i in range(5): #llenar la lista
        lista = [aleatorios.randint(1, 10000) for _ in range(tamanio)]
    inicio_tiempo = time.time()
    lista = bucket_sort(lista)
    fin_tiempo = time.time()
    tiempo_transcurrido = fin_tiempo - inicio_tiempo
    tiempo_axis_y.append(tiempo_transcurrido)
    tamanio_axis_x.append(len(lista))
    print(f"Loop: {n} || Datos: {tamanio} || Tiempo de ejecución: {tiempo_transcurrido:.10f} segundos")
    lista = []
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
#    arr_best = list(range(size))
#    arr_worst = list(range(size, 0, -1))
#
#    # Mejor de los casos
#    start_time = time.time()
#    arr_best = bucket_sort(arr_best)
#    end_time = time.time()
#    best_case_times.append(end_time - start_time)
#
#    # El peor de los casos
#    start_time = time.time()
#    arr_worst = bucket_sort_peor(arr_worst)
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