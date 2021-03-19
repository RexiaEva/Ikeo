import sys
# import du module mysql.connector
from mysql.connector import connect, DatabaseError, InterfaceError

class BDD:
    """classe pour gérer une baseb de données"""
    def __init__(self, base, pseudo, passe, hote, port=None):
        """Se connecter à la base de données"""
        # connecte puis déconnecte (login,pwd) de la base [database] du serveur [host]
        # lance l'exception DatabaseError si problème
        self.connexion = None
        try:
            # connexion
            if port:
                self.connexion = connect(host=hote, user=pseudo, password=passe, database=base, port=port)
            else:
                self.connexion = connect(host=hote, user=pseudo, password=passe, database=base)
                self.nom = base
            print(
                f"Connexion réussie à la base database={base}, host={hote} sous l'identité user={pseudo}")
        except:
            print("Connexion échouée\n")
    def __del__(self):
        """Se déconnecter"""
        # on ferme la connexion si elle a été ouverte
        if self.connexion:
            self.connexion.close()
            print("Déconnexion réussie\n")
    def __repr__(self):
        """Quand on entre l'objet dans l'interpréteur"""
        return "Base : {}".format(self.nom)
    def __str__(self):
        """Afficher la base"""
        pass
    def execute_sql(self, update= str):
        """exécute une requête de mise à jour sur la connexion"""
        curseur = None
        try:
            # on demande un curseur
            self.curseur = self.connexion.cursor()
            # exécute la requête update sur la connexion
            self.curseur.execute(update)
        finally:
            # fermeture du curseur s'il a été obtenu
            if curseur:
                curseur.close()
    def select_sql(self, fonction="afficher", update= str):
        """exécute une requête de mise à jour sur la connexion"""
        curseur = None
        try:
            # on demande un curseur
            self.curseur = self.connexion.cursor()
            # exécute la requête update sur la connexion
            self.curseur.execute(update)
            rows = self.curseur.fetchall()
            for row in rows:
                if fonction == "afficher":
                    ligne = ""
                    for i in row:
                        ligne += " | " + i
                    print(ligne)
        finally:
            # fermeture du curseur s'il a été obtenu
            if curseur:
                curseur.close()

    # def update(self, table, condition, **donnees):
    #     """mettre à jour une ou des lignes"""
    #     try:
    #         requete = """UPDATE {} SET """.format(table)
    #         i = 0
    #         for cle, val in donnees.items():
    #             if isinstance(val, str):
    #                 requete+=(cle + " = '" + val + "'")
    #             else:
    #                 requete+=(cle + " = " + val)
    #             if i < len(donnees)-1:
    #                 requete+=", "
    #             i += 1
    #         requete+= """ WHERE {}""".format(condition)
    #         print("requète =", requete)
    #         self.curseur.execute(requete)
    #         self.connexion.commit()
    #     except:
    #         print("ERREUR : requète =", requete)
    #         self.connexion.rollback()
    # def inserer(self, table, *donnees, **nommes):
    #     """Insérer des données ou ajouter une ligne"""
    #     requete = ""
    #     try:
    #         # print("donnees =", donnees)
    #         # print("nommes =", nommes)
    #         # print("!donnees =", not donnees)
    #         # print("!nommes =", not nommes)
    #         if donnees and not nommes:
    #             requete = """INSERT INTO {} VALUES {}""".format(table, donnees)
    #         elif nommes and not donnees:
    #             i = 0
    #             cles = "("
    #             # print("cles =", cles)
    #             vals = "("
    #             # print("vals =", vals)
    #             for cle, val in nommes.items():
    #                 # print("cle, val =", (cle, val))
    #                 # print("i =", i)
    #                 if i < len(nommes)-1:
    #                     cles+=(cle + ", ")
    #                     # print("cles =", cles)
    #                     vals+=("\"" + str(val) + "\",")
    #                     # print("vals =", vals)
    #                 else:
    #                     cles+=(cle + ")")
    #                     # print("cles =", cles)
    #                     vals+=("\"" + str(val) + "\")")
    #                     # print("vals =", vals)
    #                 i+=1
    #             requete = """INSERT INTO {} {} VALUES {}""".format(table, cles, vals)
    #         self.curseur.execute(requete)
    #         print("EXECUTION : requète =", requete)
    #         self.connexion.commit()
    #     except:
    #         print("ERREUR : requète =", requete)
    #         self.connexion.rollback()
    # def creerTable(self, table, instr):
    #     """Créer une table"""
    #     requete = """CREATE TABLE IF NOT EXISTS {} ({});""".format(table, instr)
    #     print("requète =", requete)
    #     self.curseur.execute(requete)
    # def ajoutcolonne(self, table, col):
    #     """Ajouter une colonne"""
    #     requete = """ALTER TABLE {} 
    #     ADD {};""".format(table, col)
    #     print("requète =", requete)
    #     self.curseur.execute(requete)

if __name__ == "__main__":
    
    # connexion à une base MySql [dbpersonnes]
    # l'identité de l'utilisateur est (admpersonnes,nobody)
    USER = "root"
    PWD = "root"
    HOST = "localhost"
    PORT = 8081
    DATABASE = "ikeo"

    # connexion d'un utilisateur inexistant
    try:
        base = BDD(DATABASE, USER, PWD, HOST, PORT)
    except (InterfaceError, DatabaseError) as erreur:
        # on affiche l'erreur
        print(f"L'erreur suivante s'est produite : {erreur}")
        # on quitte
        sys.exit()