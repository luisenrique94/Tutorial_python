a = int(input("proporciona un valor:"))
valorMinimo=0
valorMaximo=5
dentroRango=(a >= valorMinimo and a <= valorMaximo)
if(dentroRango):
    print("Dentro de rango")
else:
    print("fuera de rango")