# views/dashboard_view.py
import tkinter as tk

class DashboardView:
    def __init__(self, root):
        self.root = root
        self.root.title("Dashboard")

        tk.Label(root, text="Bienvenido al sistema KAVA").pack()
