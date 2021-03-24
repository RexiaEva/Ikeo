from tkinter import *
import bdd

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
base = bdd.BDD('ikeo', 'root', 'root', 'localhost', 8081)

# afficher tous les produits ainsi que leurs sites de production
rep1 = base.select('produits', '')

# On crée un label (ligne de texte)
champ_label = Label(fenetre, text="Salut les Zér0s !")

# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()