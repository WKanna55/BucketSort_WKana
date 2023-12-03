"""
def bucket_sort(arr):
    # Find the maximum and minimum values in the array
    max_val = max(arr) # o(n)
    min_val = min(arr) # o(n)

    # Calculate the range of each bucket
    bucket_range = (max_val - min_val) / len(arr)

    # Create empty buckets
    buckets = [[] for _ in range(len(arr))]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # Sort each bucket (using a simple sorting algorithm, like insertion sort)
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])

    # Concatenate the sorted buckets to get the final sorted array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array

# Example usage:
arr = [3.2, 1.8, 0.5, 2.5, 1.3, 3.7]
sorted_arr = bucket_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)
"""

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
        buckets[i] = buckets[i].sort()

    sorted_array = []
    for bucket in buckets:
        sorted_array = sorted_array + bucket

    return sorted_array


arreglo = [3, 5, 2, 8, 1]
sorted_arr = bucket_sort(arreglo)
print("Original array:", arreglo)
print("Sorted array:", sorted_arr)



