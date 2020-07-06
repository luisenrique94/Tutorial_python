print("Proporcione los siguientes datos del libro")
nombre=input("Proporcione el nombre:")
id=int(input("Proporcione el ID: "))
precio=float(input("Proporcione el precio:"))
envioGratuito=input("Indica si el envio es gratuito (true/false)")
if envioGratuito=="true":
    envioGratuito=True
elif envioGratuito == "False":
    envioGratuito=False
else:
    envioGratuito= "valor incorrecto, debe ser true/false"

print("Nombre",nombre)
print("Id",id)
print("Precio:",precio)
print("Envio Gratuito:", envioGratuito)
#prueba de git 
#prueba de git remoto 