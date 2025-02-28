print('Bienvenido a "Promedio pro" por EduTech Solutions.')

suma = 0
contador = 0
promedio = 0

while contador < 5:
    calificacion = float(input(f"Ingrese la calificación n° {contador + 1}: "))
    if (calificacion < 0):
        print("Tu calificación no puede ser menor a 0.")
    elif (calificacion > 100):
        print("Tu calificación no puede ser mayor a 100.")
    elif (calificacion % 1 != 0):
        print("Tu calificación debe ser un número entero.")
    else:
        contador = contador + 1
        suma = calificacion + suma

promedio = suma/5
print(f"Tu promedio es {promedio}")

if promedio >= 60:
    print("Aprobaste el curso.")
elif promedio < 40:
    print("Reprobaste el curso.")
else:
    print("Quedaste en recuperación.")

print("Gracias por usar nuestros servicios.")
