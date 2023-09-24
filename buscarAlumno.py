import tkinter as tk
import keyboard

def busqueda():
    respuesta = ""  # Inicializar la variable respuesta
    label_mensaje = None
    
    def on_key(event):
        entry_widget = event.widget
        text = entry_widget.get()
        print(len(text))
        
        if (len(text)==2 or len(text)==6) and keyboard.is_pressed("backspace")!=True:
            entry_widget.insert(tk.END,".")
        
        if len(text)==10 and keyboard.is_pressed("backspace")!=True:
            entry_widget.insert(tk.END,"-")
        
    def limpiar_mensaje():
        nonlocal label_mensaje
        if label_mensaje is not None:
            label_mensaje.grid_forget()  # Eliminar el label de la ventana
            label_mensaje = None
            
    def enviar_busqueda():
        nonlocal respuesta  # Utilizar respuesta como una variable no local
        
        if entry_nombre.get() != "" and entry_rut.get() == "":
            respuesta = entry_nombre.get()
            ventana.destroy()
            
        elif entry_rut.get() != "" and entry_nombre.get() == "":
            respuesta = entry_rut.get()
            ventana.destroy()
            
        elif entry_rut.get() != "":
            nonlocal label_mensaje
            label_mensaje = tk.Label(ventana, text="ERROR RUT",bg="RED",width=40)
            label_mensaje.grid(row=7, column=0, columnspan=2)
            ventana.after(3000, limpiar_mensaje)

    ventana = tk.Toplevel()  # Ventana secundaria
    label_mensaje = tk.Label(ventana, text="Buscar Por Rut o Nombre", bg="pink", width=40)
    label_mensaje.grid(row=0, column=0, columnspan=2)
    
    label_mensaje = tk.Label(ventana)
    label_mensaje.grid(row=1, column=0, columnspan=2)
    
    label_nombre = tk.Label(ventana, text="Nombre:", bg="salmon")
    label_nombre.grid(row=2, column=0)
    entry_nombre = tk.Entry(ventana)
    entry_nombre.grid(row=2, column=1)
    
    label_mensaje = tk.Label(ventana)
    label_mensaje.grid(row=3, column=0, columnspan=2)
    
    label_rut = tk.Label(ventana, text="RUT:", bg="salmon")
    label_rut.grid(row=4, column=0)
    entry_rut = tk.Entry(ventana)
    entry_rut.config(validate="key")
    entry_rut.config(validatecommand=(entry_rut.register(lambda text: len(text) <= 12), "%P"))
    entry_rut.grid(row=4, column=1)
    entry_rut.bind("<Key>", on_key)
    
    label_mensaje = tk.Label(ventana)
    label_mensaje.grid(row=5, column=0, columnspan=2)
    
    boton_guardar = tk.Button(ventana, text="Buscar", command=enviar_busqueda)
    boton_guardar.grid(row=6, column=1, columnspan=2)
    
    label_mensaje = tk.Label(ventana)
    label_mensaje.grid(row=7, column=0, columnspan=2)
    
    ventana.wait_window()  # Esperar hasta que se cierre la ventana secundaria

    return respuesta