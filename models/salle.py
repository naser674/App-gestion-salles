class Salle:
    def _init_(self, code, libelle, type, capacite):
        self.code = code
        self.libelle = libelle
        self.type = type
        self.capacite = capacite
    def afficher_infos(self):
        print("code:", self.code)
        print("libelle:", self.libelle)
        print("type:", self.type)
        print("capacite:", self.capacite)