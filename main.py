# main.py
# Point d'entrée de l'application
# Version 2.0 - Interface graphique Tkinter

import tkinter as tk
from interface.fenetre_principale import FenetrePrincipale

if __name__ == "__main__":
    root = tk.Tk()
    app = FenetrePrincipale(root)
    root.mainloop()