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

from Data.dao_salle import DataSalle
from models.salle import Salle

dao = DataSalle()

connexion = dao.get_connection()
if connexion.is_connected():
    print("Connexion réussie")
connexion.close()

code_test = "A203"

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

# Récupérer et afficher toutes les salles
print("\nListe des salles :")
liste_salles = dao.get_salles()
for salle in liste_salles:
    print("------------")
    salle.afficher_infos()
from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

# Afficher la liste des salles
print("Liste des salles :")
liste = service.recuperer_salles()
for salle in liste:
    print("------------")
    salle.afficher_infos()

# Ajouter une salle
salle1 = Salle("B101", "Salle Réseau", "Laboratoire", 20)
succes, message = service.ajouter_salle(salle1)
print(message)

# Modifier une salle
salle1.libelle = "Salle Réseau Cisco"
salle1.capacite = 25
succes, message = service.modifier_salle(salle1)
print(message)

# Rechercher une salle
salle_trouvee = service.rechercher_salle("B101")
if salle_trouvee:
    print("Salle trouvée :")
    salle_trouvee.afficher_infos()

# Supprimer une salle
succes, message = service.supprimer_salle("B101")
print(message)

from views.view_salle import ViewSalle

app = ViewSalle()
app.mainloop()