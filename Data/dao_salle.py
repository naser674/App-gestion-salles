import json
import mysql.connector
from models.salle import Salle


class DataSalle:
    def __init__(self):
        self.config_path = "data/config.json"

    def get_connection(self):
        with open(self.config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        conn = mysql.connector.connect(
            host=config["host"],
            user=config["user"],
            password=config["password"],
            database=config["database"]
        )
        return conn

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "INSERT INTO Salle (code, libelle, type, capacite) VALUES (%s, %s, %s, %s)"
        values = (salle.code, salle.libelle, salle.type, salle.capacite)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "UPDATE Salle SET libelle=%s, type=%s, capacite=%s WHERE code=%s"
        values = (salle.libelle, salle.type, salle.capacite, salle.code)
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "DELETE FROM Salle WHERE code=%s"
        cursor.execute(sql, (code,))
        conn.commit()
        cursor.close()
        conn.close()

    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "SELECT code, libelle, type, capacite FROM Salle WHERE code=%s"
        cursor.execute(sql, (code,))
        row = cursor.fetchone()
        cursor.close()
        conn.close()

        if row:
            return Salle(row[0], row[1], row[2], row[3])
        return None

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        sql = "SELECT code, libelle, type, capacite FROM Salle"
        cursor.execute(sql)
        rows = cursor.fetchall()
        cursor.close()
        conn.close()

        salles = []
        for row in rows:
            salles.append(Salle(row[0], row[1], row[2], row[3]))
        return salles