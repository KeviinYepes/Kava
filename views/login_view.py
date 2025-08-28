import tkinter as tk
from tkinter import messagebox
from controllers.auth_controller import AuthController

class LoginView:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")

        # Pantalla completa
        self.root.state("zoomed")  # En Windows (para Linux/Mac usar: self.root.attributes("-fullscreen", True))
        self.root.configure(bg="#d0f0c0")  # Verde claro de fondo

        # Frame central para centrar contenido
        frame = tk.Frame(root, bg="#ffffff", bd=5, relief="ridge")
        frame.place(relx=0.5, rely=0.5, anchor="center")

        # Título principal
        tk.Label(frame, 
                 text="🌿 Bienvenido a Kava", 
                 font=("Arial", 26, "bold"), 
                 fg="#2e7d32", 
                 bg="#ffffff").pack(pady=(10, 20))

        # Usuario
        tk.Label(frame, 
                 text="Usuario:", 
                 font=("Arial", 14), 
                 bg="#ffffff").pack(anchor="w", padx=20)
        self.username_entry = tk.Entry(frame, font=("Arial", 14), width=25, bd=3, relief="solid")
        self.username_entry.pack(pady=(0, 15), padx=20)

        # Contraseña
        tk.Label(frame, 
                 text="Contraseña:", 
                 font=("Arial", 14), 
                 bg="#ffffff").pack(anchor="w", padx=20)
        self.password_entry = tk.Entry(frame, font=("Arial", 14), show="*", width=25, bd=3, relief="solid")
        self.password_entry.pack(pady=(0, 25), padx=20)

        # Botón ingresar
        tk.Button(frame, 
                  text="Ingresar", 
                  command=self.login, 
                  font=("Arial", 14, "bold"), 
                  bg="#66bb6a", 
                  fg="white", 
                  activebackground="#388e3c", 
                  activeforeground="white", 
                  relief="flat", 
                  width=20, 
                  height=2).pack(pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        user = AuthController.login(username, password)

        if user:
            messagebox.showinfo("Éxito", f"Bienvenido {user.username}")
            # Aquí puedes abrir dashboard_view
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")
