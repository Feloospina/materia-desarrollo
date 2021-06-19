""" Manejo de estructuras básicas de programación

        Introduccion a la programacion

             Grupo: 301304_5
             
    Luis Felipe Castrillon Ospina
"""   

#Problema seleccionado # 4

"""En el curso de filosofia, se desea saber cuál es el promedio del grupo, 
cuántos aprobaron el curso y cuántos reprobaron. Se debe solicitar la 
cantidad de estudiantes que se registrarán y la nota definitiva por 
estudiante en un rango entre 0 y 5.")"""

#Definicion de varibales

lista = []
suma = 0
promedio = 0


#inicio de proceso, evaluando el ingreo de datos
while True:
    try:
        cantidad_notas = int(input(f"¿cuantos alumnos va registrar ? "))
        break
    except ValueError:
        print("----------------------------------------------")
        print("Esta ingresando texto, debe ingresar un numero")
        print("----------------------------------------------")
# inicio del bucle ingresando Una cantidad n
for i in range(cantidad_notas):
    while True: 
        try:
            nota = float(input(f"ingrese la nota final de cada estudiante {i + 1}: "))
            if(nota > 5 or nota < 0):
                print("----------------------------------")
                print("Su nota final debe ser entre 0 y 5")
                print("----------------------------------")
            else:    
                lista.append(nota)
                break
        except ValueError:
            print("------------------------------------------------------------------------------")
            print("Esta ingresando texto, debe ingresar un numero. Por favor intentalo nuevamente")
            print("------------------------------------------------------------------------------")
#comparacion de datos y comprobacion de que los mismos cumplan con los parametros
    suma = suma + lista[i]
#operacion para calcular el promedio del grupo
promedio = (suma / len(lista))
   
# salida de datos e impresion de datos en la pantalla
print("----------------------------------------------")
print(f"El grupo obtuvo las siguientes notas: {lista}")
print("----------------------------------------------")
print("-------------------------------------")
print(f"El promedio del grupo es: {promedio}")
print("-------------------------------------")
print("-------------------------------------------")
print(f"La nota Minima del grupo es : {min(lista)}")
print("-------------------------------------------")
print("-------------------------------------------")
print(f"La nota Maxima del grupo es : {max(lista)}")
print("-------------------------------------------")
lista.clear()