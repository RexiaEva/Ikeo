from tkinter import *
import bdd

# On crée une fenêtre, racine de notre interface
fenetre = Tk()
base = bdd.BDD('ikeo', 'root', 'root', 'localhost', 8081)

# On crée un label (ligne de texte)
champ_label = Label(fenetre, text="Afficher tous les produits ainsi que leurs sites de production")
# On affiche le label dans la fenêtre
champ_label.pack()
# afficher tous les produits ainsi que leurs sites de production
rep1 = base.selects('produits, produits_usines, usines', 'produits.id_p = produits_usines.produit_id AND produits_usines.usine_id = usines.id_u', 'nom_p', 'descrip_p')
# On crée un label (ligne de texte)
champ_label = Label(fenetre, text=rep1)
# On affiche le label dans la fenêtre
champ_label.pack()

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()