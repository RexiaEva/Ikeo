import mysql.connector

class BDD:
    """classe pour gérer une baseb de données"""
    def __init__(self, base, pseudo, passe, hote, port=None):
        """Se connecter à la base de données"""
        self.nom = base
        if(port is None):
            self.connexion = mysql.connector.connect(host=hote,
                                                     user=pseudo, password=passe,
                                                     database=base)
        else:
            self.connexion = mysql.connector.connect(host=hote,
                                                     user=pseudo, password=passe,
                                                     database=base, port=port)
        self.curseur = self.connexion.cursor()
    def __del__(self):
        """Se déconnecter"""
        self.connexion.close()
    def __repr__(self):
        """Quand on entre l'objet dans l'interpréteur"""
        return "Base : {}".format(self.nom)
    def select(self, table, condition, *colonne):
        liste = list()
        col = ""
        for i, val in enumerate(colonne):
                if i < len(colonne)-1:
                    col+=(val + ", ")
                else:
                    col+=val
        requete = """SELECT {} FROM {} WHERE {}""".format(col, table, condition)
        print("requète =", requete)
        self.curseur.execute(requete)
        lignes = self.curseur.fetchall()
        for ligne in lignes:
            liste.append(ligne)
        return liste
    def update(self, table, condition, **donnees):
        """mettre à jour une ou des lignes"""
        try:
            requete = """UPDATE {} SET """.format(table)
            i = 0
            for cle, val in donnees.items():
                if isinstance(val, str):
                    requete+=(cle + " = '" + val + "'")
                else:
                    requete+=(cle + " = " + val)
                if i < len(donnees)-1:
                    requete+=", "
                i += 1
            requete+= """ WHERE {}""".format(condition)
            print("requète =", requete)
            self.curseur.execute(requete)
            self.connexion.commit()
        except:
            print("ERREUR : requète =", requete)
            self.connexion.rollback()
    def inserer(self, table, *donnees, **nommes):
        """Insérer des données ou ajouter une ligne"""
        try:
            if donnees and not nommes:
                requete = """INSERT INTO {} VALUES {}""".format(table, donnees)
            elif nommes and not donnees:
                i = 0
                cles = "("
                vals = list()
                for cle, val in nommes.items():
                    if i < len(donnees)-1:
                        cles+=(cle + ", ")
                        vals.append(val)
                    else:
                        cles+=(cle + ")")
                        vals.append(val)
                    i+=1
                requete = """INSERT INTO {} {} VALUES {}""".format(table, cles, vals)
            print("requète =", requete)
            self.curseur.execute(requete)
            self.connexion.commit()
        except:
            print("ERREUR : requète =", requete)
            self.connexion.rollback()
    def creerTable(self, table, instr):
        """Créer une table"""
        requete = """CREATE TABLE IF NOT EXISTS {} ({});""".format(table, instr)
        print("requète =", requete)
        self.curseur.execute(requete)
    def ajoutcolonne(self, table, col):
        """Ajouter une colonne"""
        requete = """ALTER TABLE {} 
        ADD {};""".format(table, col)
        print("requète =", requete)
        self.curseur.execute(requete)
