# -*- coding: utf-8 -*-
"""
Codigo que genera la ficha puntual que se va a imprimir, debería haber sido una implementacion breve
en guardado general seleccionando el alumno con un rut especifico pero me dio paja.
"""
from datetime import date
from docxtpl import DocxTemplate
from time import sleep

import sqlite3
import os

# Conectar a la base de datos
def guardadorPuntual(rutAlumn):
    conexion = sqlite3.connect('FichaAlumnos.db')
    cursor = conexion.cursor()
    
    # Consultar los datos específicos de la base de datos
    cursor.execute("SELECT * FROM alumnos where rut=?",(rutAlumn,))
    datos_alumnos = cursor.fetchall()
    conexion.close()
    # Crear un nuevo documento de Word
    doc = DocxTemplate("ficha.docx")
    #cambiar booleanos por "si" y "no"
    def convertir_booleano(valor):
        return "Sí" if valor else "No"
    
    for alumno in datos_alumnos:
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
            'chile_solidario': alumno[10],
            'presento_certificado': convertir_booleano(alumno[11]),
            'necesita_PAE': convertir_booleano(alumno[12]),
            'nombre_contest_encuesta': alumno[13],
            'jefe_hogar': alumno[14],
            'vive_hogar': alumno[15],
            'titular': alumno[16],
            'suplente': alumno[17],
            'titrut':alumno[18],
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
            'enfermedad': convertir_booleano(alumno[33]),
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
            doc.render(context)
            doc.save("ficha_puntual.docx")
            print("IMPRIMIR DOCUMENTO")
            os.startfile("ficha_puntual.docx", "print")
            sleep(2)
            os.startfile("ficha_puntual.docx", "print")
            print("DOCUMENTO IMPRESO")
        except Exception as e:
            #alumnos que no se imprimen (posiblemente esten guardados ya)
            print("nombre:"+str(alumno[0]))
            print("rut:"+alumno[1]+str(alumno[0]))