import tkinter as tk

root = tk.Tk()
root.geometry("800x600")  # taille initiale

# Créer le bouton
button = tk.Button(root, text="Clique-moi", font=("Arial", 24))

# Le bouton prend toute la fenêtre
button.pack(fill="both", expand=True)

root.mainloop()
