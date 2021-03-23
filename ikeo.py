import bdd
from tkinter import *

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

base = bdd.BDD('ikeo', 'root', '', 'localhost')

# afficher tous les produits ainsi que leurs sites de production
rep1 = base.select('produits', '')
champ_label1 = Label(fenetre, text="Salut les Zér0s !")
champ_label1.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()