import tkinter as tk 
from tkinter import messagebox 
from controllers.auth_controller import AuthController #Importamos la clase donde se valida el usuario

# Clase que representa la vista de Login en la aplicación
class LoginView:
    def __init__(self, root):
        # Guardamos la ventana principal (root)
        self.root = root
        self.root.title("Login")  # Título de la ventana

        # Etiqueta y campo de entrada para el usuario
        tk.Label(root, text="Usuario").pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        # Etiqueta y campo de entrada para la contraseña
        tk.Label(root, text="Contraseña").pack()
        self.password_entry = tk.Entry(root, show="*")  # show="*" oculta la contraseña
        self.password_entry.pack()

        # Botón que ejecuta la función login() cuando se presiona
        tk.Button(root, text="Ingresar", command=self.login).pack()

    # Método que maneja el proceso de autenticación
    def login(self):
        # Se obtienen los valores que el usuario escribió en los campos
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Se llama al controlador de autenticación para validar credenciales
        user = AuthController.login(username, password)

        # Si el controlador devuelve un usuario válido → éxito
        if user:
            messagebox.showinfo("Éxito", f"Bienvenido {user.username}")
            # Aquí podrías redirigir a otra vista, como dashboard_view.py
        else:
            # Si no coincide usuario/contraseña, muestra error
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")