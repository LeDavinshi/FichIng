import sqlite3
from datetime import date
from docxtpl import DocxTemplate
import os
import tkinter as tk
from tkinter import ttk
#VISUALIZADOR SE DEDICA A GENERAR LOS ARCHIVOS DE FICHA Y LOS SEPARA POR CARPETA DE CURSOS

def visualizador():
    root = tk.Tk()
    root.title("Progreso")
    root.geometry("400x100")

    progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
    progress.pack(pady=20)

    label = tk.Label(root, text="Generando fichas...")
    label.pack()
    
    #genera la carpeta Fichas
    if not os.path.exists("fichas"):
        os.makedirs("fichas")
        
    conexion = sqlite3.connect('FichaAlumnos.db')
    cursor = conexion.cursor()
    
    # Consultar los datos específicos de la base de datos
    cursor.execute("SELECT * FROM alumnos")
    datos_alumnos = cursor.fetchall()
    conexion.close()
    
    total_alumnos = len(datos_alumnos)
    progress["maximum"] = total_alumnos
    
    # Crear un nuevo documento de Word
    doc = DocxTemplate("ficha.docx")
    
    #cambiar booleanos por "si" y "no"
    def convertir_booleano(valor):
        return "Sí" if valor else "No"
    
    for idx, alumno in enumerate(datos_alumnos):
        
        file_path = "fichas/{}{}/{}.docx".format(alumno[44], alumno[43], "{} {}".format(alumno[1], alumno[0]))
        if not os.path.exists(file_path):
            try:
                context = {
                'rut': alumno[0],
                'nombre': alumno[1],
                'fecha_nacimiento': alumno[2],
                'direccion': alumno[3],
                'colegio_procedencia': alumno[4],
                'cursos_repetidos': alumno[5],
                'nombre_padre': alumno[6],
                'rut_padre': alumno[7],
                'nombre_madre': alumno[8],
                'rut_madre': alumno[9],
                'chile_solidario': convertir_booleano(alumno[10]),
                'presento_certificado': convertir_booleano(alumno[11]),
                'necesita_PAE': convertir_booleano(alumno[12]),
                'nombre_contest_encuesta': alumno[13],
                'jefe_hogar': alumno[14],
                'vive_hogar': alumno[15],
                'titular': alumno[16],
                'suplente': alumno[17],
                'titrut': alumno[18],
                'suprut': alumno[19],
                'titphone': alumno[20],
                'supphone': alumno[21],
                'n_hermanos': alumno[22],
                'hermanos_estudian': alumno[23],
                'hermanos_no_estudian': alumno[24],
                'otros_viven': alumno[25],
                'ultimo_ano_madre': alumno[26],
                'ultimo_ano_jefe': alumno[27],
                'ocupacion_madre': alumno[28],
                'ocupacion_jefe': alumno[29],
                'figura_pate': convertir_booleano(alumno[30]),
                'fig_aporta_recursos': convertir_booleano(alumno[31]),
                'psicolog': alumno[32],
                'enfermedad': alumno[33],
                'aprende': alumno[34],
                'estudia': alumno[35],
                'religion': alumno[36],
                'asistereligion': convertir_booleano(alumno[37]),
                'pie': alumno[38],
                'locomocion':convertir_booleano(alumno[39]),
                'emergencia': alumno[40],
                'domicilio': alumno[41],
                'celular': alumno[42],
                'fecha_hoy': date.today().strftime("%d/%m/%Y"),
                'curso': alumno[44],
                'letra': alumno[43]
                }
                #reemplazar para este alumno los datos de la base de datos en el word
                doc.render(context)
                #crear el archivo y guardarlo
                os.makedirs("fichas/"+str(alumno[44])+str(alumno[43]), exist_ok=True)
                doc.save("fichas/"+str(alumno[44])+str(alumno[43])+"/"+str(alumno[1]+" "+str(alumno[0]))+".docx")
            except Exception as e:
                return
        progress["value"] = idx
        label["text"] = f"Generando fichas... ({idx}/{total_alumnos})"
        root.update()
    label["text"] = "Fichas generadas correctamente"
    root.destroy()