#Programa para invertir un numero de 4 digitos Ej. si ingresa 1234 devuelve 4321

print("-------------------------------------")
print("---invertir un numero de 4 digitos---")
print("-------------------------------------")

# input
n = int(input("digite el valor de n: "))

# processing
d1 = ((n%10)*1000)
pe = (n//10)
d2 = ((pe%10)*100)
pe = (pe//10)
d3 = ((pe%10)*10)
d4 = (pe//10)
ni = (d1+d2+d3+d4)

# output
print("------------------------------------")
print("---------RESULTADOS-----------------")
print("------------------------------------")
print(" RESULTADO INVERSO:" + str(ni))
