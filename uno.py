print("HOLA MUNDO!")

for i in [1, 2, 3, 4]:
    print(i, end=", ") # prints: 1, 2, 3, 4,

for i in [1, 3, 5, 7, 9]:
    x = i**2 - (i-1)*(i+1)
    print(x, end=", ") # prints 1, 1, 1, 1, 1, 