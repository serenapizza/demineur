import tkinter as tk

def lancer_jeu():
    jeu = tk.Tk()
    jeu.title("Jeu")
    jeu.geometry("300x300")

fenetre = tk.Tk()
fenetre.title("Démineur")
fenetre.geometry("500x500")
tk.Label(fenetre, text="Jeu de démineur", font=("Verdana", 20, "bold")).grid(row=0, column=0)
tk.Button(fenetre, text="Cliquez ici pour commencer une partie", font="Verdana", command=lancer_jeu).grid(row=1, column=0)


tk.mainloop()

