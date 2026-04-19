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
    def delete_salle(self, code):
        connexion = self.get_connection()
        cursor = connexion.cursor()
        requete = "DELETE FROM salle WHERE code = %s"
        cursor.execute(requete, (code,))
        connexion.commit()
        cursor.close()
        connexion.close()

    def get_salle(self, code):
        connexion = self.get_connection()
        cursor = connexion.cursor()

        requete = "SELECT code, libelle, type, capacite FROM salle WHERE code = %s"
        cursor.execute(requete, (code,))
        resultat = cursor.fetchone()
        cursor.close()
        connexion.close()
        if resultat:
            return Salle(resultat[0], resultat[1], resultat[2], resultat[3])
        return None