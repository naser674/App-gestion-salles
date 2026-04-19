import json
import mysql.connector
class DataSalle:
    def get_connection(self):
        with open("Data/config.json", "r", encoding="utf-8") as fichier:
            config = json.load(fichier)
        connexion = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return connexion
    def insert_salle(self,salle):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete ="""
        INSERT INTO salle (code, libelle, type, capacite)
        VALUES (%s, %s, %s, %s)
        """
        valeurs = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(requete, valeurs)
        connexion.commit()
        cursor.close()
        connexion.close()