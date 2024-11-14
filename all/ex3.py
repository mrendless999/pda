import math
import random

# Taking input from the user and converting it to a float for mathematical operations
x = float(input("Enter a number: "))

print("\nNumerical Operations using math:")
print("Square root:", math.sqrt(x))           # Square root of x
print("e^2:", math.exp(2))                    # e^2
print("Natural log of 10:", math.log(10))     # Natural log of 10
print("Sin(π/2):", math.sin(math.pi / 2))     # Sin of π/2, which is 1.0
print("Factorial of 5:", math.factorial(5))   # Factorial of 5, which is 120
print("Floor of 3.9:", math.floor(3.9))       # Floor value of 3.9, which is 3
print("Ceil of 3.1:", math.ceil(3.1))         # Ceil value of 3.1, which is 4

print("\nNumerical Operations using random number functions:")
print("Random float between 0 and 1:", random.random())  # Random float between 0 and 1
print("Random integer between 1 and 100:", random.randint(1, 100))  # Random integer between 1 and 100
print("Random float between 1 and 10:", random.uniform(1, 10))      # Random float between 1 and 10

items = ['apple', 'banana', 'cherry']
print("Randomly selected item from the list:", random.choice(items))  # Randomly select an item from the list
random.shuffle(items)  # Shuffle the list in place
print("Shuffled list:", items)
