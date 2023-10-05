import tkinter as tk
import sqlite3
import keyboard #me dio flojera hacer un programa que estandarize en tiempo real el rut por eso implementé esto (me da verguenza)

import visualizador
import buscarAlumno
import guardar
import eliminar


from tkinter import ttk
from confirmacion import confirmacion 
from guardadorPuntual import guardadorPuntual

guardar #llamamos a una funcion que guarda una copia de la base de datos con su fecha y nombre
eliminar #llamamos una funcion que eliminar una copia de la base de datos si tiene una antiguedad de 15 dias siempre quedan los ultimos 5 archivos copiados

#Informacion basica de la pantalla
ventana = tk.Tk()
ventana.title("FichIng V 2.6.4")
ventana.configure(bg='gray')

#Funcion para guardar los datos que hay puestos en el programa
def guardar_datos():
    try:
        
        # Conectar a la base de datos
        conexion = sqlite3.connect('FichaAlumnos.db')
        cursor = conexion.cursor()

        # Verificar si el RUT ya existe en la base de datos
        cursor.execute("SELECT rut FROM alumnos WHERE rut=?", (entry_rut.get(),))
        resultado = cursor.fetchone()

        if resultado:
            # Actualizar los datos del alumno
            print("resultado")
            actualizardatos()
            
        else:
            # Insertar los datos del alumno
            cursor.execute("INSERT INTO alumnos (nombre, rut, fecha_nacimiento, direccion, colegio_procedencia, cursos_repetidos, nombre_padre, rut_padre, nombre_madre, rut_madre, chile_solidario, presento_certificado, necesita_PAE, nombre_contest_encuesta, jefe_hogar, vive_hogar, titular, suplente, titrut, suprut, titphone, supphone, n_hermanos, hermanos_estudian, hermanos_no_estudian, otros_viven, ultimo_ano_madre, ultimo_ano_jefe, ocupacion_madre, ocupacion_jefe, figura_pate, fig_aporta_recursos, psicolog, enfermedad, aprende, estudia, religion, asistereligion, pie, locomocion, emergencia, domicilio, celular,curso,letra) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)",
                        (
                            obtener_valor_predeterminado(entry_nombre.get()),
                            entry_rut.get(),
                            obtener_valor_predeterminado(entry_fecha_nacimiento.get()),
                            obtener_valor_predeterminado(entry_direccion.get()),
                            obtener_valor_predeterminado(entry_colegio_procedencia.get()),
                            obtener_valor_predeterminado(entry_cursos_repetidos.get()),
                            obtener_valor_predeterminado(entry_nombre_padre.get()),
                            obtener_valor_predeterminado(entry_rut_padre.get()),
                            obtener_valor_predeterminado(entry_nombre_madre.get()),
                            obtener_valor_predeterminado(entry_rut_madre.get()),
                            chile_solidario_var.get(),  # Convertir a entero
                            presento_certificado_var.get(),  # Convertir a entero
                            necesita_PAE_var.get(),  # Convertir a entero
                            obtener_valor_predeterminado(entry_nombre_contest_encuesta.get()),
                            obtener_valor_predeterminado(entry_jefe_hogar.get()),
                            obtener_valor_predeterminado((entry_vive_hogar.get())),
                            obtener_valor_predeterminado(entry_titular.get()),
                            obtener_valor_predeterminado(entry_suplente.get()),
                            obtener_valor_predeterminado(entry_titrut.get()),
                            obtener_valor_predeterminado(entry_suprut.get()),
                            obtener_valor_predeterminado((entry_titphone.get())),
                            obtener_valor_predeterminado((entry_supphone.get())),
                            obtener_valor_predeterminado((entry_n_hermanos.get())),
                            obtener_valor_predeterminado((entry_hermanos_estudian.get())),
                            obtener_valor_predeterminado((entry_hermanos_no_estudian.get())),
                            obtener_valor_predeterminado((entry_otros_viven.get())),
                            obtener_valor_predeterminado(selected_ano_madre.get()),
                            obtener_valor_predeterminado(selected_ano_jefe.get()),
                            obtener_valor_predeterminado(entry_ocupacion_madre.get()),
                            obtener_valor_predeterminado(entry_ocupacion_jefe.get()),
                            figura_pate_var.get(),
                            fig_aporta_recursos_var.get(),
                            obtener_valor_predeterminado(entry_psicolog.get()),
                            obtener_valor_predeterminado(entry_enfermedad.get()),
                            obtener_valor_predeterminado(entry_aprende.get()),
                            obtener_valor_predeterminado(entry_estudia.get()),
                            obtener_valor_predeterminado(entry_religion.get()),
                            asistereligion_var.get(),  # Convertir a entero
                            obtener_valor_predeterminado(entry_pie.get()),
                            locomocion_var.get(),  # Convertir a entero
                            obtener_valor_predeterminado(entry_emergencia.get()),
                            obtener_valor_predeterminado(entry_domicilio.get()),
                            obtener_valor_predeterminado(entry_celular.get()),
                            obtener_valor_predeterminado(selected_option.get()),
                            obtener_valor_predeterminado(selected_letra.get())
                        ))
            mostrar_mensaje("Guardado Correctamente","green")

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión a la base de datos
        conexion.close()

        # Mostrar mensaje de éxito

    except Exception as e:
        # Mostrar mensaje de error con la información de la excepción
        mostrar_mensaje(f"Error: {str(e)}","red")

        
# función que sirve para limpiar los campos de entrada.
def limpiar_entradas():
    entry_rut.delete(0, tk.END)
    entry_nombre.delete(0, tk.END)
    entry_fecha_nacimiento.delete(0, tk.END)
    entry_direccion.delete(0, tk.END)
    entry_colegio_procedencia.delete(0, tk.END)
    entry_cursos_repetidos.delete(0, tk.END)
    entry_nombre_padre.delete(0, tk.END)
    entry_rut_padre.delete(0, tk.END)
    entry_nombre_madre.delete(0, tk.END)
    entry_rut_madre.delete(0, tk.END)
    entry_nombre_contest_encuesta.delete(0, tk.END)
    entry_jefe_hogar.delete(0, tk.END)
    entry_vive_hogar.delete(0, tk.END)
    entry_titular.delete(0, tk.END)
    entry_suplente.delete(0, tk.END)
    entry_titrut.delete(0, tk.END)
    entry_suprut.delete(0, tk.END)
    entry_titphone.delete(0, tk.END)
    entry_supphone.delete(0, tk.END)
    entry_n_hermanos.delete(0, tk.END)
    entry_hermanos_estudian.delete(0, tk.END)
    entry_hermanos_no_estudian.delete(0, tk.END)
    entry_otros_viven.delete(0, tk.END)
    entry_ocupacion_madre.delete(0, tk.END)
    entry_ocupacion_jefe.delete(0, tk.END)
    entry_psicolog.delete(0, tk.END)
    entry_aprende.delete(0, tk.END)
    entry_estudia.delete(0, tk.END)
    entry_religion.delete(0, tk.END)
    entry_pie.delete(0, tk.END)
    entry_emergencia.delete(0, tk.END)
    entry_domicilio.delete(0, tk.END)
    entry_celular.delete(0, tk.END)
    entry_enfermedad.delete(0, tk.END)
    #booleanos y menues
    selected_letra.set("Nulo")
    selected_option.set("Nulo")
    selected_ano_madre.set("Nulo")
    selected_ano_jefe.set("Nulo")
    figura_pate_var.set(False)
    fig_aporta_recursos_var.set(False)
    locomocion_var.set(False)
    presento_certificado_var.set(False)
    necesita_PAE_var.set(False)
    #enfermedad_var.set(False)
    asistereligion_var.set(False)
    locomocion_var.set(False)
    
#funcion que carga  los datos de un alumno que se ha cargado
#utriliza el rut para cargarlo en el sistema
#NO MODIFICA AL ALUMNO SINO QUE CARGA SUS DATOS EN LOS RECUADROS
def editar_alumno():
    print("dato")
    dato=buscarAlumno.busqueda()
    if (dato!=""):
        limpiar_entradas()
    print("dato :"+dato)
    mostrar_mensaje("Alumno Cargado","green")
    conexion = sqlite3.connect('FichaAlumnos.db')
    cursor = conexion.cursor()
    # Consultar los datos específicos de la base de datos
    cursor.execute("SELECT * FROM alumnos WHERE rut = ? OR nombre = ?", (dato, dato))
    datos_alumnos = cursor.fetchall()
    conexion.close()
    
    for alumno in datos_alumnos:
        entry_rut.insert(0, alumno[0])
        entry_nombre.insert(0, alumno[1])
        entry_fecha_nacimiento.insert(0, alumno[2])
        entry_direccion.insert(0, alumno[3])
        entry_colegio_procedencia.insert(0, alumno[4])
        entry_cursos_repetidos.insert(0, alumno[5])
        entry_nombre_padre.insert(0, alumno[6])
        entry_rut_padre.insert(0, alumno[7])
        entry_nombre_madre.insert(0, alumno[8])
        entry_rut_madre.insert(0, alumno[9])
        chile_solidario_var.set(alumno[10])
        presento_certificado_var.set(alumno[11])
        necesita_PAE_var.set(alumno[12])
        entry_nombre_contest_encuesta.insert(0, alumno[13])
        entry_jefe_hogar.insert(0, alumno[14])
        entry_vive_hogar.insert(0, alumno[15])
        entry_titular.insert(0, alumno[16])
        entry_suplente.insert(0, alumno[17])
        entry_titrut.insert(0, alumno[18])
        entry_suprut.insert(0, alumno[19])
        entry_titphone.insert(0, alumno[20])
        entry_supphone.insert(0, alumno[21])
        entry_n_hermanos.insert(0, alumno[22])
        entry_hermanos_estudian.insert(0, alumno[23])
        entry_hermanos_no_estudian.insert(0, alumno[24])
        entry_otros_viven.insert(0, alumno[25])
        selected_ano_madre.set(alumno[26])
        selected_ano_jefe.set(alumno[27])
        entry_ocupacion_madre.insert(0, alumno[28])
        entry_ocupacion_jefe.insert(0, alumno[29])
        figura_pate_var.set(alumno[30])
        fig_aporta_recursos_var.set(alumno[31])
        entry_psicolog.insert(0, alumno[32])
        entry_enfermedad.insert(0, alumno[33])
        entry_aprende.insert(0, alumno[34])
        entry_estudia.insert(0, alumno[35])
        entry_religion.insert(0, alumno[36])
        asistereligion_var.set(alumno[37])
        entry_pie.insert(0, alumno[38])
        locomocion_var.set(alumno[39])
        entry_emergencia.insert(0, alumno[40])
        entry_domicilio.insert(0, alumno[41])
        entry_celular.insert(0, alumno[42])
        selected_letra.set(alumno[43])
        selected_option.set(alumno[44])

#funcion que cambia los valores vacios por la palabra Nulo para que no estén vacios
#en el archivo word de ficha
def obtener_valor_predeterminado(valor):
    if valor.strip() == '':
        return "Nulo"
    return valor

#limpia los mensajes que genera mostrar_mensaje
def limpiar_mensaje():
    global label_mensaje
    if label_mensaje is not None:
        label_mensaje.grid_forget()  # Eliminar el label de la ventana
        label_mensaje = None
        
#mostrar mensaje se encarga de mostrar mensajes en una zona especifica de la pantalla
#se debe colocar el mensaje entre comillas y el color del recuadro
def mostrar_mensaje(mensaje,color):
    global label_mensaje
    if label_mensaje is not None:
        label_mensaje.grid_forget()  # Eliminar el label existente antes de crear uno nuevo

    label_mensaje = tk.Label(ventana)
    label_mensaje.config(text=mensaje, bg=color)
    label_mensaje.grid(row=10, column=4)

    # Programar la limpieza del mensaje después de 3 segundos (3000 ms)
    ventana.after(3000, limpiar_mensaje)

#funciones basicas para continuar al siguiente recuadro
def on_enter(event):
    event.widget.tk_focusNext().focus()
    

def on_key(event):
    entry_widget = event.widget
    text = entry_widget.get()
    print(len(text))
    
    if (len(text)==2 or len(text)==6) and keyboard.is_pressed("backspace")!=True:
        entry_widget.insert(tk.END,".")
    
    if len(text)==10 and keyboard.is_pressed("backspace")!=True:
        entry_widget.insert(tk.END,"-")

def select_entry(entry):
    entry.focus_set()  # Establecer el foco en el cuadro de texto
    entry.select_range(0, tk.END)  # Seleccionar todo el contenido del cuadro de texto

#borra todos los datos de la base de datos
def eliminardatos():
    flag=confirmacion("¿Estás seguro que deseas eliminar los datos?")
    if flag:
        conexion = sqlite3.connect('FichaAlumnos.db')
        cursor = conexion.cursor()
    
        # Eliminar los datos en la tabla Alumnos
        cursor.execute("DELETE FROM alumnos")
        mostrar_mensaje("Datos Eliminados", "green")
        # Guardar los cambios en la base de datos
        conexion.commit()
    
        # Cerrar la conexión a la base de datos
        conexion.close()

#modifica los datos de un alumno
def actualizardatos():
    flag = confirmacion("Este alumno ya existe. ¿Desea actualizar la información?")
    if flag:
        conexion = sqlite3.connect('FichaAlumnos.db')
        cursor = conexion.cursor()

        # Actualizar los datos en la tabla Alumnos
        cursor.execute("UPDATE alumnos SET nombre=?, fecha_nacimiento=?, direccion=?, colegio_procedencia=?, cursos_repetidos=?, nombre_padre=?, rut_padre=?, nombre_madre=?, rut_madre=?, chile_solidario=?, presento_certificado=?, necesita_PAE=?, nombre_contest_encuesta=?, jefe_hogar=?, vive_hogar=?, titular=?, suplente=?, titrut=?, suprut=?, titphone=?, supphone=?, n_hermanos=?, hermanos_estudian=?, hermanos_no_estudian=?, otros_viven=?, ultimo_ano_madre=?, ultimo_ano_jefe=?, ocupacion_madre=?, ocupacion_jefe=?, figura_pate=?, fig_aporta_recursos=?, psicolog=?, enfermedad=?, aprende=?, estudia=?, religion=?, asistereligion=?, pie=?, locomocion=?, emergencia=?, domicilio=?, celular=?, curso=?, letra=? WHERE rut=?",
                       (
                           obtener_valor_predeterminado(entry_nombre.get()),
                           obtener_valor_predeterminado(entry_fecha_nacimiento.get()),
                           obtener_valor_predeterminado(entry_direccion.get()),
                           obtener_valor_predeterminado(entry_colegio_procedencia.get()),
                           obtener_valor_predeterminado(entry_cursos_repetidos.get()),
                           obtener_valor_predeterminado(entry_nombre_padre.get()),
                           obtener_valor_predeterminado(entry_rut_padre.get()),
                           obtener_valor_predeterminado(entry_nombre_madre.get()),
                           obtener_valor_predeterminado(entry_rut_madre.get()),
                           chile_solidario_var.get(),  # Convertir a entero
                           presento_certificado_var.get(),  # Convertir a entero
                           necesita_PAE_var.get(),  # Convertir a entero
                           obtener_valor_predeterminado(entry_nombre_contest_encuesta.get()),
                           obtener_valor_predeterminado(entry_jefe_hogar.get()),
                           obtener_valor_predeterminado(entry_vive_hogar.get()),
                           obtener_valor_predeterminado(entry_titular.get()),
                           obtener_valor_predeterminado(entry_suplente.get()),
                           obtener_valor_predeterminado(entry_titrut.get()),
                           obtener_valor_predeterminado(entry_suprut.get()),
                           obtener_valor_predeterminado(entry_titphone.get()),
                           obtener_valor_predeterminado(entry_supphone.get()),
                           obtener_valor_predeterminado(entry_n_hermanos.get()),
                           obtener_valor_predeterminado(entry_hermanos_estudian.get()),
                           obtener_valor_predeterminado(entry_hermanos_no_estudian.get()),
                           obtener_valor_predeterminado(entry_otros_viven.get()),
                           obtener_valor_predeterminado(selected_ano_madre.get()),
                           obtener_valor_predeterminado(selected_ano_jefe.get()),
                           obtener_valor_predeterminado(entry_ocupacion_madre.get()),
                           obtener_valor_predeterminado(entry_ocupacion_jefe.get()),
                           figura_pate_var.get(),
                           fig_aporta_recursos_var.get(),
                           obtener_valor_predeterminado(entry_psicolog.get()),
                           obtener_valor_predeterminado(entry_enfermedad.get()),
                           obtener_valor_predeterminado(entry_aprende.get()),
                           obtener_valor_predeterminado(entry_estudia.get()),
                           obtener_valor_predeterminado(entry_religion.get()),
                           asistereligion_var.get(),  # Convertir a entero
                           obtener_valor_predeterminado(entry_pie.get()),
                           locomocion_var.get(),  # Convertir a entero
                           obtener_valor_predeterminado(entry_emergencia.get()),
                           obtener_valor_predeterminado(entry_domicilio.get()),
                           obtener_valor_predeterminado(entry_celular.get()),
                           obtener_valor_predeterminado(selected_option.get()),
                           obtener_valor_predeterminado(selected_letra.get()),
                           entry_rut.get()
                       ))

        # Guardar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión a la base de datos
        conexion.close()
        mostrar_mensaje("Guardado Correctamente","green")
        limpiar_entradas()
        
#FUNCION QUE LLAMA A VISUALIZADOR QUE GENERA LOS ARCHIVOS WORD DE LAS FICHAS
def visualizadorejecut():
    try:
        visualizador.visualizador()
        mostrar_mensaje("Generadas Las Fichas","green")
    except Exception as e:
        # Mostrar mensaje de error con la información de la excepción
        mostrar_mensaje(f"Error: {str(e)}","red")

#VERIFICA VARIAS COSAS ANTES DE GUARDAR:
    #RUT CORRECTO
    #QUE LA LETRA Y EL CURSO NO SEAN NULOS
def verificaciones():
    if  len(entry_rut.get()) != 12:
        mostrar_mensaje("Error RUT","red")
        return False
    
    if selected_letra.get()=="Nulo" or selected_option.get()=="Nulo":
        mostrar_mensaje("Curso o Letra son Nulo", "red")
        return False
    
    else: guardar_datos()


#FUNCION DE IMPRIMIR ARCHIVO, DEBERIA IMPRIMIRLO 2 VECES PERO NO FUNCIONA
def imprimir_archivo():
    guardadorPuntual(entry_rut.get())  

# BOTONES QUE ESCRIBEN AUTOMATICAMENTE SI LA MADRE O EL PADRE ES APODERADO O SUPLENTE.
def madreApod():
    entry_titular.delete(0, tk.END)
    entry_titrut.delete(0, tk.END)
    entry_titular.insert(0, entry_nombre_madre.get())
    entry_titrut.insert(0, entry_rut_madre.get())
    
def padreApod():
    entry_titular.delete(0, tk.END)
    entry_titrut.delete(0, tk.END)
    entry_titular.insert(0, entry_nombre_padre.get())
    entry_titrut.insert(0, entry_rut_padre.get())

def madreSup():
    entry_suplente.delete(0, tk.END)
    entry_suprut.delete(0, tk.END)
    entry_suplente.insert(0, entry_nombre_madre.get())
    entry_suprut.insert(0, entry_rut_madre.get())
    
def padreSup():
    entry_suplente.delete(0, tk.END)
    entry_suprut.delete(0, tk.END)
    entry_suplente.insert(0, entry_nombre_padre.get())
    entry_suprut.insert(0, entry_rut_padre.get())

def madreEmer():
    entry_emergencia.delete(0, tk.END)
    entry_emergencia.insert(0, entry_nombre_madre.get())
    
def padreEmer():
    entry_emergencia.delete(0, tk.END)
    entry_emergencia.insert(0, entry_nombre_padre.get())


# CAMPOS DE ENTRADA
#=====================================================================#
label_curso = tk.Label(ventana, text="Curso:", bg="salmon")
label_curso.grid(row=3, column=2)

options = ["1", "2", "3", "4"]
selected_option = tk.StringVar()

option_menu = tk.OptionMenu(ventana, selected_option, *options)
option_menu.grid(row=3, column=2,columnspan=2)

#=====================================================================#

label_letra = tk.Label(ventana, text="Letra:", bg="salmon")
label_letra.grid(row=3, column=3)

letras = ["A", "B", "C", "D","E","F","G"]
selected_letra = tk.StringVar()

letras_menu = tk.OptionMenu(ventana, selected_letra, *letras)
letras_menu.grid(row=3, column=3,columnspan=2)

#=====================================================================#

label_nombre = tk.Label(ventana, text="Nombre:", bg="salmon",width=21)
label_nombre.grid(row=1, column=0)
entry_nombre = tk.Entry(ventana,width=34)
entry_nombre.grid(row=1, column=1)
entry_nombre.bind("<Return>", on_enter)

#=====================================================================#

label_rut = tk.Label(ventana, text="RUT:", bg="salmon")
label_rut.grid(row=1, column=4)

entry_rut = tk.Entry(ventana, width=12)
entry_rut.config(validate="key")
entry_rut.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 12), "%P"))
entry_rut.grid(row=1, column=4, columnspan=2)
entry_rut.bind("<Key>", on_key)
entry_rut.bind("<Return>", on_enter)

#=====================================================================#

label_fecha_nacimiento = tk.Label(ventana, text="Fecha de Nacimiento:", bg="salmon",width=16)
label_fecha_nacimiento.grid(row=1, column=2)

entry_fecha_nacimiento = tk.Entry(ventana)
entry_fecha_nacimiento.grid(row=1, column=2,columnspan=3)
entry_fecha_nacimiento.bind("<Return>", on_enter)

label_mensaje = tk.Label(ventana, text="", bg="gray",width=20)
label_mensaje.grid(row=0, column=2)
#=====================================================================#

label_direccion = tk.Label(ventana, text="Dirección:", bg="salmon",width=21)
label_direccion.grid(row=2, column=0)
entry_direccion = tk.Entry(ventana,width=34)
entry_direccion.grid(row=2, column=1)
entry_direccion.bind("<Return>", on_enter)

#=====================================================================#

label_colegio_procedencia = tk.Label(ventana, text="Colegio de Procedencia:", bg="salmon",width=21)
label_colegio_procedencia.grid(row=3, column=0)
entry_colegio_procedencia = tk.Entry(ventana)
entry_colegio_procedencia.grid(row=3, column=1)
entry_colegio_procedencia.bind("<Return>", on_enter)

#=====================================================================#

label_cursos_repetidos = tk.Label(ventana, text="Cursos Repetidos:", bg="salmon",width=21)
label_cursos_repetidos.grid(row=4, column=0)
entry_cursos_repetidos = tk.Entry(ventana)
entry_cursos_repetidos.grid(row=4, column=1)
entry_cursos_repetidos.bind("<Return>", on_enter)

#=====================================================================#

label_nombre_padre = tk.Label(ventana, text="Nombre padre:", bg="salmon",width=21)
label_nombre_padre.grid(row=5, column=0)
entry_nombre_padre = tk.Entry(ventana,width=34)
entry_nombre_padre.grid(row=5, column=1)
entry_nombre_padre.bind("<Return>", on_enter)

#=====================================================================#

label_rut_padre = tk.Label(ventana, text="Rut:", bg="salmon",width=4)
label_rut_padre.grid(row=5, column=2)

entry_rut_padre = tk.Entry(ventana,width=12)
entry_rut_padre.config(validate="key")
entry_rut_padre.config(validatecommand=(entry_rut_padre.register(lambda text: len(text) <= 12), "%P"))
entry_rut_padre.grid(row=5, column=2,columnspan=2)

entry_rut_padre.bind("<Key>", on_key)
entry_rut_padre.bind("<Return>", on_enter)

#=====================================================================#

label_nombre_madre = tk.Label(ventana, text="Nombre madre:", bg="salmon",width=21)
label_nombre_madre.grid(row=6, column=0)
entry_nombre_madre = tk.Entry(ventana,width=34)
entry_nombre_madre.grid(row=6, column=1)
entry_nombre_madre.bind("<Return>", on_enter)

#=====================================================================#

label_rut_madre = tk.Label(ventana, text="Rut:", bg="salmon",width=4)
label_rut_madre.grid(row=6, column=2)

entry_rut_madre = tk.Entry(ventana,width=12)
entry_rut_madre.config(validate="key")
entry_rut_madre.config(validatecommand=(entry_rut_madre.register(lambda text: len(text) <= 12), "%P"))
entry_rut_madre.grid(row=6, column=2,columnspan=2)

entry_rut_madre.bind("<Key>", on_key)
entry_rut_madre.bind("<Return>", on_enter)

#=====================================================================#

label_nombre_contest_encuesta = tk.Label(ventana, text="Quien contesta encuesta:",bg="lightgreen",width=21)
label_nombre_contest_encuesta.grid(row=11, column=0)
entry_nombre_contest_encuesta = tk.Entry(ventana,width=34)
entry_nombre_contest_encuesta.grid(row=11, column=1)
entry_nombre_contest_encuesta.bind("<Return>", on_enter)

#=====================================================================#
#SE ME PIDIÓ CAMBIAR EL DATO "Jefe_hogar" por con quien vive, voy a cambiar solamente
#el texto
label_jefe_hogar = tk.Label(ventana, text="Con quien vive:",bg="lightgreen",width=21)
label_jefe_hogar.grid(row=12, column=0)
entry_jefe_hogar = tk.Entry(ventana,width=34)
entry_jefe_hogar.grid(row=12, column=1)
entry_jefe_hogar.bind("<Return>", on_enter)

#=====================================================================#

label_vive_hogar = tk.Label(ventana, text="Cuantos viven en el hogar:",bg="lightgreen")
label_vive_hogar.grid(row=12, column=2)
entry_vive_hogar = tk.Entry(ventana,width=3)
entry_vive_hogar.grid(row=12, column=3)
entry_vive_hogar.bind("<Return>", on_enter)

#=====================================================================#

label_titular = tk.Label(ventana, text="Apoderado Titular:",bg="lightgreen",width=21)
label_titular.grid(row=14, column=0)
entry_titular = tk.Entry(ventana,width=34)
entry_titular.grid(row=14, column=1)
entry_titular.bind("<Return>", on_enter)

#=====================================================================#

label_titrut = tk.Label(ventana, text="Rut:",bg="lightgreen",width=4)
label_titrut.grid(row=14, column=2)

entry_titrut = tk.Entry(ventana,width=12)
entry_titrut.config(validate="key")
entry_titrut.config(validatecommand=(entry_titrut.register(lambda text: len(text) <= 12), "%P"))
entry_titrut.grid(row=14, column=2,columnspan=2)

entry_titrut.bind("<Key>", on_key)
entry_titrut.bind("<Return>", on_enter)

#=====================================================================#

label_titphone = tk.Label(ventana, text="Celular Titular:",bg="lightgreen",width=12)
label_titphone.grid(row=14, column=3)
entry_titphone = tk.Entry(ventana)
entry_titphone.grid(row=14, column=4)
entry_titphone.bind("<Return>", on_enter)

#=====================================================================#

label_suplente = tk.Label(ventana, text="Apoderado Suplente:",bg="lightgreen",width=21)
label_suplente.grid(row=15, column=0)
entry_suplente = tk.Entry(ventana,width=34)
entry_suplente.grid(row=15, column=1)
entry_suplente.bind("<Return>", on_enter)

#=====================================================================#

label_suprut = tk.Label(ventana, text="Rut:",bg="lightgreen",width=4)
label_suprut.grid(row=15, column=2)

entry_suprut = tk.Entry(ventana,width=12)
entry_suprut.config(validate="key")
entry_suprut.config(validatecommand=(entry_suprut.register(lambda text: len(text) <= 12), "%P"))
entry_suprut.grid(row=15, column=2,columnspan=2)

entry_suprut.bind("<Key>", on_key)
entry_suprut.bind("<Return>", on_enter)

#=====================================================================#

label_supphone = tk.Label(ventana, text="Celular Suplente:",bg="lightgreen",width=12)
label_supphone.grid(row=15, column=3)
entry_supphone = tk.Entry(ventana)
entry_supphone.grid(row=15, column=4)
entry_supphone.bind("<Return>", on_enter)

#=====================================================================#
label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=16, column=0, columnspan=2)
#=====================================================================#

label_n_hermanos = tk.Label(ventana, text="N. Hermanos:", bg="pink",width=10)
label_n_hermanos.grid(row=17, column=0)
entry_n_hermanos = tk.Entry(ventana)
entry_n_hermanos.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 2), "%P"),width=3)
entry_n_hermanos.grid(row=17, column=0,columnspan=2)
entry_n_hermanos.bind("<Return>", on_enter)

#=====================================================================#

label_hermanos_estudian = tk.Label(ventana, text="Estudian:",bg="pink",width=10)
label_hermanos_estudian.grid(row=17, column=1)
entry_hermanos_estudian = tk.Entry(ventana)
entry_hermanos_estudian.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 2), "%P"),width=3)
entry_hermanos_estudian.grid(row=17, column=1,columnspan=2)
entry_hermanos_estudian.bind("<Return>", on_enter)

#=====================================================================#

label_hermanos_no_estudian = tk.Label(ventana, text="No Estudian:",bg="pink",width=10)
label_hermanos_no_estudian.grid(row=17, column=2)
entry_hermanos_no_estudian = tk.Entry(ventana)
entry_hermanos_no_estudian.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 2), "%P"),width=3)
entry_hermanos_no_estudian.grid(row=17, column=2,columnspan=2)
entry_hermanos_no_estudian.bind("<Return>", on_enter)

#=====================================================================#

label_otros_viven = tk.Label(ventana, text="Otros:",bg="pink",width=10)
label_otros_viven.grid(row=17, column=3)
entry_otros_viven = tk.Entry(ventana)
entry_otros_viven.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 2), "%P"),width=3)
entry_otros_viven.grid(row=17, column=3,columnspan=2)
entry_otros_viven.bind("<Return>", on_enter)

label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=18, column=0, columnspan=2)

#=====================================================================#

label_ocupacion_madre = tk.Label(ventana, text="Ocupación Madre:", bg="pink",width=21)
label_ocupacion_madre.grid(row=19, column=0)
entry_ocupacion_madre = tk.Entry(ventana)
entry_ocupacion_madre.grid(row=19, column=1)
entry_ocupacion_madre.bind("<Return>", on_enter)

#=====================================================================#

label_ultimo_ano_madre = tk.Label(ventana, text="Estudios Madre", bg="pink",width=16)
label_ultimo_ano_madre.grid(row=19, column=2)

ano_madre = ["Sin estudios", "1ro Basico", "2do Basico", "3ro Basico","4to Basico","5to Basico","6to Basico","7mo Basico","8vo Basico","1ro Medio","2do Medio","3ro Medio","4to Medio","Superior Incompleta","Superior"]
selected_ano_madre = tk.StringVar()


ano_madre_menu = tk.OptionMenu(ventana, selected_ano_madre, *ano_madre)
ano_madre_menu.grid(row=19, column=3)

#=====================================================================#

label_ocupacion_jefe = tk.Label(ventana, text="Ocupación de con quien vive:", bg="pink",width=21)
label_ocupacion_jefe.grid(row=21, column=0)
entry_ocupacion_jefe = tk.Entry(ventana)
entry_ocupacion_jefe.grid(row=21, column=1)
entry_ocupacion_jefe.bind("<Return>", on_enter)

#=====================================================================#

label_ultimo_ano_jefe = tk.Label(ventana, text="Estudios Jefe", bg="pink",width=16)
label_ultimo_ano_jefe.grid(row=21, column=2)

ano_jefe = ["Sin estudios", "1ro Basico", "2do Basico", "3ro Basico","4to Basico","5to Basico","6to Basico","7mo Basico","8vo Basico","1ro Medio","2do Medio","3ro Medio","4to Medio","Superior Incompleta","Superior"]
selected_ano_jefe = tk.StringVar()

ano_jefe_menu = tk.OptionMenu(ventana, selected_ano_jefe, *ano_jefe)
ano_jefe_menu.grid(row=21, column=3)

#=====================================================================#
label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=24, column=0, columnspan=2)

label_psicolog = tk.Label(ventana, text="Asistencia a Especialista:", bg="pink",width=21)
label_psicolog.grid(row=25, column=0)
entry_psicolog = tk.Entry(ventana)
entry_psicolog.grid(row=25, column=1)
entry_psicolog.bind("<Return>", on_enter)

#=====================================================================#

label_enfermedad = tk.Label(ventana, text="Enfermedad Prolongada", bg="pink",width=15)
label_enfermedad.grid(row=25, column=2)
entry_enfermedad = tk.Entry(ventana)
entry_enfermedad.grid(row=25, column=3)
entry_enfermedad.bind("<Return>", on_enter)

#=====================================================================#

label_aprende = tk.Label(ventana, text="Aprende:", bg="pink",width=15)
label_aprende.grid(row=26, column=0)

# Opciones del menú desplegable
opciones_aprende = ["con dificultad", "sin dificultad", "lentitud","rapidez"]
entry_aprende = ttk.Combobox(ventana, values=opciones_aprende,width=10)
entry_aprende.grid(row=26, column=1)

#=====================================================================#

label_estudia = tk.Label(ventana, text="Estudia ", bg="pink",width=15)
label_estudia.grid(row=26, column=2)

# Opciones del menú desplegable
opciones_estudia = ["siempre", "nunca", "a veces", "solo para pruebas"]
entry_estudia = ttk.Combobox(ventana, values=opciones_estudia,width=14)
entry_estudia.grid(row=26, column=3)

#=====================================================================#

label_religion = tk.Label(ventana, text="Religión", bg="pink",width=15)
label_religion.grid(row=26, column=4)
entry_religion = tk.Entry(ventana)
entry_religion.grid(row=26, column=5)
entry_religion.bind("<Return>", on_enter)

#=====================================================================#

label_pie = tk.Label(ventana, text="Necesita PIE", bg="pink",width=21)
label_pie.grid(row=27, column=0)
entry_pie = tk.Entry(ventana)
entry_pie.grid(row=27, column=1)
entry_pie.bind("<Return>", on_enter)

#=====================================================================#
label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=28, column=0, columnspan=2)

label_emergencia = tk.Label(ventana, text="Contacto Emergencia", bg="lightblue",width=21)
label_emergencia.grid(row=29, column=0)
entry_emergencia = tk.Entry(ventana)
entry_emergencia.grid(row=29, column=1)
entry_emergencia.bind("<Return>", on_enter)

#=====================================================================#

label_domicilio = tk.Label(ventana, text="Domicilio", bg="lightblue")
label_domicilio.grid(row=29, column=2)
entry_domicilio = tk.Entry(ventana)
entry_domicilio.grid(row=29, column=3)
entry_domicilio.bind("<Return>", on_enter)

#=====================================================================#

label_celular = tk.Label(ventana, text="Teléfono", bg="lightblue")
label_celular.grid(row=29, column=4)
entry_celular = tk.Entry(ventana)
entry_celular.grid(row=29, column=5)
entry_celular.bind("<Return>", on_enter)

#=====================================================================#

#booleanos
chile_solidario_var = tk.BooleanVar()
check_chile_solidario = tk.Checkbutton(ventana, text="Chile Solidario", variable=chile_solidario_var, bg="salmon",width=18)
check_chile_solidario.grid(row=8, column=0)

#=====================================================================#

presento_certificado_var = tk.BooleanVar()
check_presento_certificado = tk.Checkbutton(ventana, text="Presentó Certificado", variable=presento_certificado_var, bg="salmon")
check_presento_certificado.grid(row=8, column=1)

label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=9, column=0, columnspan=2)
#=====================================================================#

necesita_PAE_var = tk.BooleanVar()
check_necesita_PAE = tk.Checkbutton(ventana, text="Necesita PAE", variable=necesita_PAE_var,bg="lightgreen")
check_necesita_PAE.grid(row=11, column=2)

#=====================================================================#

locomocion_var = tk.BooleanVar()
check_locomocion = tk.Checkbutton(ventana, text="Locomoción", variable=locomocion_var, bg="pink")
check_locomocion.grid(row=27, column=2)

#=====================================================================#

asistereligion_var = tk.BooleanVar()
check_asistereligion = tk.Checkbutton(ventana, text="Asiste a Religión", variable=asistereligion_var, bg="pink")
check_asistereligion.grid(row=26, column=7,columnspan=2)
label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=26, column=6, columnspan=1)
#=====================================================================#

#enfermedad no es booleano, se quita de aquí y se mueve arriva
# enfermedad_var = tk.BooleanVar()
# check_enfermedad = tk.Checkbutton(ventana, text="Enfermedad prolongada", variable=enfermedad_var, bg="pink")
# check_enfermedad.grid(row=25, column=2)

#=====================================================================#

fig_aporta_recursos_var = tk.BooleanVar()
check_fig_aporta_recursos = tk.Checkbutton(ventana, text="Figura Aporta Recursos", variable=fig_aporta_recursos_var, bg="pink")
check_fig_aporta_recursos.grid(row=23, column=1)

#=====================================================================#
figura_pate_var = tk.BooleanVar()
check_figura_pate = tk.Checkbutton(ventana, text="Figura Paterna", variable=figura_pate_var, bg="pink")
check_figura_pate.grid(row=23, column=0)

#=====================Botones y titulos================================#
label_mensaje = tk.Label(ventana, text="",bg="gray")
label_mensaje.grid(row=30, column=0, columnspan=2)

boton_limpiar = tk.Button(ventana, text="Limpiar Datos", command=limpiar_entradas)
boton_limpiar.grid(row=31, column=0)

boton_guardar = tk.Button(ventana, text="Guardar", command=verificaciones)
boton_guardar.grid(row=31, column=1)

boton_imprimir = tk.Button(ventana, text="Imprimir archivo", command=imprimir_archivo)
boton_imprimir.grid(row=31, column=2)

boton_generar = tk.Button(ventana, text="Generar Fichas", command=visualizadorejecut)
boton_generar.grid(row=31, column=3)

boton_buscar = tk.Button(ventana, text="Buscar Alumno", command=editar_alumno)
boton_buscar.grid(row=31, column=4)

boton_guardar = tk.Button(ventana, text="Eliminar Datos", command=eliminardatos,bg="red")
boton_guardar.grid(row=31, column=5)

label_mensaje = tk.Label(ventana, text="Datos Personales",bg="salmon",width=21)
label_mensaje.grid(row=0, column=0, columnspan=1)

#==============APODERADO==============#

boton_apod_pad = tk.Button(ventana, text="Apoderado", command=padreApod,bg="green")
boton_apod_pad.grid(row=5, column=3,columnspan=1)

boton_apod_mad = tk.Button(ventana, text="Apoderado", command=madreApod,bg="green")
boton_apod_mad.grid(row=6, column=3,columnspan=1)

#==============SUPLENTE==============#

boton_sup_pad = tk.Button(ventana, text="Suplente", command=padreSup,bg="green")
boton_sup_pad.grid(row=5, column=3,columnspan=2)

boton_sup_mad = tk.Button(ventana, text="Suplente", command=madreSup,bg="green")
boton_sup_mad.grid(row=6, column=3,columnspan=2)

#==============EMERGENCIAS==============#

boton_emer_pad = tk.Button(ventana, text="Emergencia", command=padreEmer,bg="lightblue")
boton_emer_pad.grid(row=5, column=4)


boton_emer_mad = tk.Button(ventana, text="Emergencia", command=madreEmer,bg="lightblue")
boton_emer_mad.grid(row=6, column=4)
    
#SETEAR NULOS AUTOMATICAMENTE AL LOOPEAR EL PROGRAMA
selected_letra.set("Nulo")
selected_option.set("Nulo")
selected_ano_madre.set("Nulo")
selected_ano_jefe.set("Nulo")

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()