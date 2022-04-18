"""Programa para calcular la potencia x a la y"""




from tkinter import Y


print("----------------------------------------------")
print("---------------POTENCIA: x ^ y----------------")
print("----------------------------------------------")

# input

X= input(" Digite el valor de x: ")
X= int(X)
Y= input(" Digite el valor de y: ")
Y= int(Y)

# Procesing
z = X**Y

# Output
print(str(X) + " elevado a la " + str(Y) + " es igual a " + str(z))


