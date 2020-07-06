calificacion=int(input("Integre la calificacion del alumno del 1 al 10: "))
nota=None


if calificacion>=9 and calificacion<=10:

    nota="A"

elif calificacion>=8 and calificacion<9:

    nota="B"

elif calificacion>=7 and calificacion<8:

    nota="C"

elif calificacion>=6 and calificacion<7:

    nota="D"

elif calificacion>=0 and calificacion<6:

    nota="F"

else:

    calificacion="Error"

print("La calificación es: ", nota)