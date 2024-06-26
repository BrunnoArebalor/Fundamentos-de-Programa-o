# Questão 1
import random

def shuffle(arr):
    n = len(arr)

    i = random.randint(0, n-1)
    j = random.randint(0, n-1)
    while i == j:
        j = random.randint(0, n-1)

    arr[i], arr[j] = arr[j], arr[i]
    return arr

array = ['a', 'b', 'c', 'd', 'e']
print("Array original:", array)
shuffled_array = shuffle(array.copy())
print("Array após troca:", shuffled_array)

