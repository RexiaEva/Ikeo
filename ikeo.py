import bdd
import sys
from mysql.connector import connect, DatabaseError, InterfaceError

USER = "root"
PWD = "root"
HOST = "localhost"
PORT = 8081
DATABASE = "ikeo"

# connexion d'un utilisateur inexistant
try:
    base = bdd.BDD(DATABASE, USER, PWD, HOST, PORT)
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}")
    # on quitte
    sys.exit()

# afficher tous les produits ainsi que leurs sites de production
requete = """SELECT `nom_p`, `descrip_p`, nom_u
FROM `produits`
INNER JOIN produits_usines
    ON produits.id_p = produits_usines.produit_id
INNER JOIN usines
    ON produits_usines.usine_id = usines.id_u
WHERE 1"""
try:
    # exécution requête
    Q1 = base.select('produits', '1', 'nom_p', 'descrip_p')
    ligne = base.curseur.fetchall()
    for i in ligne:
        print(i)
    # affichage
    print(f"{requete} : requête réussie")
except (InterfaceError, DatabaseError) as erreur:
    # on affiche l'erreur
    print(f"L'erreur suivante s'est produite : {erreur}") 