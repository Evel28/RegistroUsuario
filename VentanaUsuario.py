import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
import Usuario

class Aplicacion:
    def __init__(self):
        self.registrar= Usuario.usuario()
        
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("Registro Principal")
        self.cuaderno1 = ttk.Notebook(self.ventana1)  
        self.registrarUsuario()
        self.ConsultarUsuario()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)

        self.ventana1.mainloop()

    def registrarUsuario(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Registrar Usuario")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Usuario")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #
        self.Cedula = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Cedula:")# se crea el control Label para la etiqueta     
        self.label2.grid(column=0, row=0, padx=4, pady=4)# se coloca la ubicacion del Label
        self.entryCedula=ttk.Entry(self.labelframe1, textvariable=self.Cedula)# se crea el control Entry     
        self.entryCedula.grid(column=1, row=0, padx=4, pady=4)# se coloca la ubicacion del Entry
        #
        self.Nombre = tk.StringVar()# se declara la variable
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.entryNombre=ttk.Entry(self.labelframe1, textvariable=self.Nombre)
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)
        #
        self.Apellido = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Apellido:")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.entryApellido=ttk.Entry(self.labelframe1, textvariable=self.Apellido)
        self.entryApellido.grid(column=1, row=2, padx=4, pady=4)
        #
        self.Edad = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Edad:")        
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.entryEdad=ttk.Entry(self.labelframe1, textvariable=self.Edad)
        self.entryEdad.grid(column=1, row=3, padx=4, pady=4)
        #
        self.boton1=ttk.Button(self.labelframe1, text="Registrar", command=self.Registrar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def ConsultarUsuario(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta Usuario")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Consulta")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        #
        self.Cedula = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Cedula:")        
        self.label2.grid(column=0, row=0, padx=4, pady=4)
        self.entryCedula=ttk.Entry(self.labelframe1, textvariable=self.Cedula)
        self.entryCedula.grid(column=1, row=0, padx=4, pady=4)
        #
        self.Nombre = tk.StringVar()# se declara la variable
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=1, padx=4, pady=4)
        self.entryNombre=ttk.Entry(self.labelframe1, textvariable=self.Nombre,state="readonly")
        self.entryNombre.grid(column=1, row=1, padx=4, pady=4)
        #
        self.Apellido = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Apellido:")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.entryApellido=ttk.Entry(self.labelframe1, textvariable=self.Apellido, state="readonly")
        self.entryApellido.grid(column=1, row=2, padx=4, pady=4)
        #
        self.Edad = tk.StringVar()# se declara la variable
        self.label2=ttk.Label(self.labelframe1, text="Edad:")        
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.entryEdad=ttk.Entry(self.labelframe1, textvariable=self.Edad, state="readonly")
        self.entryEdad.grid(column=1, row=3, padx=4, pady=4)
        #
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.Consultar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def Registrar(self):
        Datos = (self.Nombre.get(),self.Apellido.get(),self.Cedula.get(),self.Edad.get())
        self.registrar.Insertar(Datos)
        mb.showinfo("Información", "Los datos fueron cargados")

    def Consultar(self):
        if len(self.Cedula.get()) == 0:
            mb.showinfo("Información", "Debe introducir un numero de cedula.")
        else:
            Datos = (self.Cedula.get(),)
            respuesta = self.registrar.consultar(Datos)
            if len(respuesta)>0:
                self.Nombre.set(respuesta[0][0])
                self.Apellido.set(respuesta[0][1])
                self.Edad.set(respuesta[0][3])
            else:
                mb.showinfo("Información", "No existe el numero de cedula.")

aplicacion1=Aplicacion()