#imprimir solo las letras a
for letra in "holanda":
    if letra=="a":
        print(letra)
        break
else:
    print("Fin ciclo for")
print("continua el programa")
#imprimir solo numeros pares
for i in range(6):
    if i%2 !=0:
        continue
    print(i)