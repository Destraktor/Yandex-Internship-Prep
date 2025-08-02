# task1
print([i**2 for i in range(1,19) if i%2 == 1])

# task2
letters = ['a','b','c']
numbers = [1,2,3]

directory = dict(zip(letters, numbers))

print(directory)

# task3
from itertools import permutations

print(list(permutations("123")))