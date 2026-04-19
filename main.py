from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Tester la connexion à la base de données
connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

# Ajouter une salle
salle1 = Salle("A102", "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Tester la connexion à la base de données
connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

# Ajouter une salle
salle1 = Salle("A102", "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

# Tester la connexion
connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

# Ajouter une salle
salle1 = Salle("A103", "Salle Info", "Laboratoire", 30)
dao.insert_salle(salle1)
print("Salle ajoutée")

# Modifier une salle
salle1.libelle = "Salle Informatique"
salle1.type = "Laboratoire"
salle1.capacite = 35
dao.update_salle(salle1)
print("Salle modifiée")