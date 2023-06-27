""" Escribir un programa que pregunte al usuario:
a) su nombre, y luego lo salude.
b) dos números, y luego muestre el producto.""" 

name = input("Escriba su nombre:")
print("Hola "+ name)
print(f"Hola {name}")

print("")

n1=int(input("Escriba un numero:"))
n2=int(input("Escriba otro numero:"))
producto= n1 * n2


print(f" {n1} * {n2} = {producto}")


