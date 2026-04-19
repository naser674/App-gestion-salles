from Data.dao_salle import DataSalle

dao = DataSalle()

connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

code_test = "A200"

salle1 = Salle(code_test, "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")