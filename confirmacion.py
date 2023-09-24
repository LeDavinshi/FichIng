import tkinter as tk

def confirmacion(mensaje):
    ventana = tk.Toplevel()  # Crear una ventana secundaria
    
    confirmado = False  # Inicializar la variable confirmado
    
    def confirmar_eliminacion():
        nonlocal confirmado  # Utilizar la variable confirmado de la función padre
        if entry_clave.get() == "0210":  # Verificar si la clave ingresada es correcta
            confirmado = True
            ventana.destroy()
    
    def cancelar_eliminacion():
        nonlocal confirmado  # Utilizar la variable confirmado de la función padre
        ventana.destroy()
    
    def cerrar_ventana():
        nonlocal confirmado  # Utilizar la variable confirmado de la función padre
        ventana.destroy()
    
    ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)  # Capturar el evento de cierre de la ventana
    
    label_confirmacion = tk.Label(ventana, text=mensaje)
    label_confirmacion.pack()
    
    entry_clave = tk.Entry(ventana, show="*", width=10)  # Cuadro de ingreso de clave (mostrar asteriscos)
    entry_clave.pack()
    
    frame_botones = tk.Frame(ventana)
    frame_botones.pack()
    
    boton_confirmar = tk.Button(frame_botones, text="Confirmar", command=confirmar_eliminacion)
    boton_confirmar.pack(side=tk.LEFT, padx=5)
    
    boton_cancelar = tk.Button(frame_botones, text="Cancelar", command=cancelar_eliminacion)
    boton_cancelar.pack(side=tk.LEFT, padx=5)
    
    ventana.wait_window()  # Esperar hasta que se cierre la ventana secundaria
    print(confirmado)
    return confirmado

