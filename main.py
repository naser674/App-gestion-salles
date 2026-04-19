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

dao.delete_salle(code_test)
print("Salle supprimée")

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

code_test = "A201"

# Ajouter une salle
salle1 = Salle(code_test, "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")

# Modifier une salle
salle1.libelle = "Salle Informatique"
salle1.type = "Laboratoire"
salle1.capacite = 35
dao.update_salle(salle1)
print("Salle modifiée")

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

code_test = "A202"

# Ajouter une salle
salle1 = Salle(code_test, "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")

# Modifier une salle
salle1.libelle = "Salle Informatique"
salle1.type = "Laboratoire"
salle1.capacite = 35
dao.update_salle(salle1)
print("Salle modifiée")

# Rechercher une salle par son code
salle_trouvee = dao.get_salle(code_test)
if salle_trouvee:
    print("Salle trouvée :")
    salle_trouvee.afficher_infos()

