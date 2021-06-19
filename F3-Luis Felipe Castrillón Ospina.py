''' Aplicación de clases y métodos 

    Introduccion a la programacion
    
         Grupo: 301304_5
              
    Luis Felipe Castrillon Ospina
'''

# problema seleccionado #3

''' Un instituto de idiomas ofrece cursos de inglés, francés y mandarín. 
Necesita un programa que le permita al estudiante elegir uno de los 3 
cursos que desee estudiar. La aplicación mostrará después de cada 
registro la cantidad de estudiantes que tiene cada curso. '''


# documentacion de el scrip desarrollado


# datetime
'''nos permite manipular las clases de fecha y hora'''

# pickle
'''pickle pódemos serializar y de esta forma podemos almacenar los datos en un documento
en este caso en concretro almacenaremos en un .txt y .bin para posterior poder cargarlos
tambien en nuesta scrip'''

# Tkinter
''' nos va permitir craftear lo que es nuestra interfaz fracia, con este modulo podemos pasar
de consola a una inferfazas grafica, que nos dara mejor control al momento de ingresar datos,
el modulo ya lo trae por defecto python'''

# scrolledtext
''' este Widget nos va permitir manejar todo lo que es multilineas de texto dentro de nustro
aplicativo, es decir diversas o multiples cadenas de texto'''

# io
''' nos va permitir importar datos, a nuestro scrip de forma estructurada, el uso que le daremos
para importar y hacer uso de open(file) de esta forma podemos abrir un documento en nuestro scrip'''

# importacion de modulos y uso de Widget




from datetime import datetime
from pickle import dump
from pickle import load
from tkinter import *
from tkinter import messagebox
import tkinter.scrolledtext as scrolledtext
import io
class Estudiante():

    def __init__(self, nombre_est, apellido_est):
        self.nombre = nombre_est
        self.apellido = apellido_est

# definicion de la clases y sus atributos:CursoIdioma


class CursoIdioma():

    def __init__(self):
        self.listaCurso = []

    def ingresar(self, nodoEstudiante):         # Ingreso estudiante n a un curso n
        self.listaCurso.append(nodoEstudiante)

    # Retorna un string con los estudiantes en diversas lineas
    def lista_para_imprimir(self):
        cadena = ""

        for i in self.listaCurso:
            cadena = cadena + \
                "Nombres: {} Apellidos: {}\n".format(i.nombre, i.apellido)

        return cadena

    def calcularCant(self):  # Retorna la cantidad de alumnos n en un curso n
        return len(self.listaCurso)

# definicion de la clases y sus atributos:CursoIdioma


class TodosLosCursos():
    def __init__(self):
        self.ingles = CursoIdioma()
        self.frances = CursoIdioma()
        self.mandarin = CursoIdioma()

# definicion de la funcion: agrega_nuevo_alumno


def agrega_nuevo_alumno():  # es llamada por el boton "Agregar nuevo"
    obj_curso = curso

    nombre = entrada_nomb.get()
    apellido = entrada_apell.get()
    valor_radio = val_radio.get()  # 1 = Ingles  2 = Frances  3 = Mandarin

    if nombre == "":
        print(messagebox.showinfo(
            message="No ingreso un nombre", title="Notificacion"))
    else:
        if apellido == "":
            print(messagebox.showinfo(
                message="No ingreso un apellido", title="Notificacion"))
        else:
            if valor_radio == 0:
                print(messagebox.showinfo(
                    message="Curso no seleccionado", title="Notificacion"))
            else:
                # agrega el estudiante
                alumno_nuevo = Estudiante(nombre, apellido)

                if valor_radio == 1:
                    obj_curso.ingles.ingresar(alumno_nuevo)
                    # actualiza la etiqueta de cantidad
                    var_etiq_ing.set(obj_curso.ingles.calcularCant())
                    radio_ingles.deselect()
                else:
                    if valor_radio == 2:
                        obj_curso.frances.ingresar(alumno_nuevo)
                        var_etiq_fran.set(obj_curso.frances.calcularCant())
                        radio_frances.deselect()
                    else:
                        if valor_radio == 3:
                            obj_curso.mandarin.ingresar(alumno_nuevo)
                            var_etiq_mand.set(
                                obj_curso.mandarin.calcularCant())
                            radio_mandarin.deselect()

                print(messagebox.showinfo(
                    message="Ingreso exitoso", title="Notificacion"))
                texto_nombre.set("")
                texto_apellido.set("")
                val_radio.set(0)


'''Cuando se apreta el boton "Total alumnos"
imprime toda la informacion de los cursos con sus alumnos en la caja de texto texto_impresion'''


def imprimir_listado():
    obj_curso = curso

    c_i = obj_curso.ingles.calcularCant()
    c_f = obj_curso.frances.calcularCant()
    c_m = obj_curso.mandarin.calcularCant()

    txt = "En total hay {} estudiantes inscritos :\n".format(c_i+c_f+c_m)
    if c_i > 0:
        txt = txt + \
            "El curso de ingles tiene {} alumnos :\n".format(
                c_i)
        txt = txt+obj_curso.ingles.lista_para_imprimir()+"\n"
    if c_f > 0:
        txt = txt + \
            "El curso de Frances tiene {} alumnos :\n".format(
                c_f)
        txt = txt+obj_curso.frances.lista_para_imprimir()+"\n"
    if c_m > 0:
        txt = txt + \
            "El curso de Mandarin Tiene {} alumnos :\n".format(
                c_m)
        txt = txt+obj_curso.mandarin.lista_para_imprimir()+"\n"

    texto_impresion.delete("2.0", "end")
    texto_impresion.insert(END, txt)

    '''Muestra un archivo de texto, y
    se habre el fichero en modo "append" añadiendo fecha y hora al header de cada nuevo registro'''
    archivo_txt = open(ruta_fichero_texto, 'a')
    # header de cada registro, tambien sirve de separador
    tx = '##################################### \n'
    tx = tx+'Registro añadido el ' + \
        str(now.date()) + "\n" + 'a las ' + \
        str(now.time()) + "\n\n" + txt + "\n\n"

    archivo_txt.write(tx)
    archivo_txt.close()
    del(archivo_txt)


def habrir_fichero():
    try:
        fichero_binario = open(ruta_fichero_binario, "rb")
        bol = messagebox.askyesno(
            message="se sobreescribiran, los datos \n ¿Desea continuar?", title="Notificacion")

        if bol:

            obj_curso = load(fichero_binario)
            global curso  # Me permite modificar una variable global desde una funcion
            curso = obj_curso

# permite actualizar las cantidades de alumnos en las etiquetas
            var_etiq_ing.set(obj_curso.ingles.calcularCant())
            var_etiq_fran.set(obj_curso.frances.calcularCant())
            var_etiq_mand.set(obj_curso.mandarin.calcularCant())

            fichero_binario.close()
            del(fichero_binario)

            print(messagebox.showinfo(
                message="Fichero cargado", title="Notificacion"))

    except FileNotFoundError:
        messagebox.showinfo(
            message="todavia no ha guardado un fichero", title="Notificacion")


# Permite el guardado en archivo binario
def guardar_fichero(obj_curso):

    fichero_binario = open(ruta_fichero_binario, "wb")
    dump(obj_curso, fichero_binario)

    fichero_binario.close()
    del(fichero_binario)

    print(messagebox.showinfo(message="Fichero guardado", title="Notificacion"))


# inicializacion de variables
root = Tk()
root.title("Instituto de idiomas")
root.geometry("510x400")
# me permite manejar un ancho fijo o redimensionarse a n valor
root.resizable(0, 0)


texto_nombre = StringVar()
texto_apellido = StringVar()


curso = TodosLosCursos()
#curso.ingles, curso.frances, curso.mandarin

val_radio = IntVar()

var_etiq_ing = StringVar()
var_etiq_fran = StringVar()
var_etiq_mand = StringVar()

'''En el directorio donde se guarde el archivo funete
se guardara el archivo que almacena los registros presto por practicidad
no se especifico un directorio de almacenamiento'''

ruta_fichero_binario = "Registro_Estudiantes.bin"
ruta_fichero_texto = "Registro_Estudiantes.txt"

now = datetime.now()


# TextBox se imprime lo guardado en un fichero cargado  o en el scrip

texto_impresion = scrolledtext.ScrolledText(
    root, undo=True, width=60, height=15, wrap='word')
texto_impresion['font'] = ('consolas', '11')
texto_impresion.place(x=40, y=140)


# Se podria mejorar la estructura visual usando algun marco para ordenar mejor los objetos

etiqueta_nomb = Label(root, text="Nombres:")
etiqueta_nomb.place(x=20, y=20)

etiqueta_apell = Label(root, text="Apellidos:")
etiqueta_apell.place(x=20, y=40)

entrada_nomb = Entry(root, textvariable=texto_nombre)
entrada_nomb.place(x=80, y=20)
entrada_nomb.focus()

entrada_apell = Entry(root, textvariable=texto_apellido)
entrada_apell.place(x=80, y=40)


boton_agregar = Button(root, text="Agregar nuevo alumno",
                       command=lambda: [agrega_nuevo_alumno()])
boton_agregar.place(x=40, y=60)


boton_imprimir = Button(root, text="Mostrar alumnos",
                        command=lambda: [imprimir_listado()])
boton_imprimir.place(x=40, y=100)


boton_abrir_fichero = Button(
    root, text="Abrir un Archivo", command=lambda: [habrir_fichero()])
boton_abrir_fichero.place(x=170, y=100)

boton_guardar_fichero = Button(
    root, text="Guardar registro", command=lambda: [guardar_fichero(curso)])
boton_guardar_fichero.place(x=290, y=100)


# Botornes para seleccionar en que curso inscribir a el estudiante

radio_ingles = Radiobutton(
    root, text="Ingles", value=1, variable=val_radio)
radio_ingles.deselect()
radio_ingles.place(x=220, y=20)

radio_frances = Radiobutton(
    root, text="Frances", value=2, variable=val_radio)
radio_frances.deselect()
radio_frances.place(x=220, y=40)

radio_mandarin = Radiobutton(
    root, text="Mandarin", value=3, variable=val_radio)
radio_mandarin.deselect()
radio_mandarin.place(x=220, y=60)


# En cada etiqueta almacenamos el numero de estudiantes Instritos por cursos

etiqueta_cantidad = Label(root, text="Estudiantes por curso:")
etiqueta_cantidad.place(x=300, y=0)

etiqueta_cantidad_ing = Label(root, textvariable=var_etiq_ing)
var_etiq_ing.set("0")
etiqueta_cantidad_ing.place(x=340, y=20)

etiqueta_cantidad_fra = Label(root, textvariable=var_etiq_fran)
var_etiq_fran.set("0")
etiqueta_cantidad_fra.place(x=340, y=40)

etiqueta_cantidad_man = Label(root, textvariable=var_etiq_mand)
var_etiq_mand.set("0")
etiqueta_cantidad_man.place(x=340, y=60)

root.mainloop()
