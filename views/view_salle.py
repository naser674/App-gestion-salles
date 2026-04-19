import customtkinter as ctk
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("750x550")

        self.service_salle = ServiceSalle()
        self.cadreInfo = ctk.CTkFrame(self, corner_radius=10)
        self.cadreInfo.pack(pady=10, padx=10, fill="x")

        self.label_code = ctk.CTkLabel(self.cadreInfo, text="Code salle :")
        self.label_code.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_code = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_code.grid(row=0, column=1, padx=10, pady=10)

        self.label_libelle = ctk.CTkLabel(self.cadreInfo, text="Libellé :")
        self.label_libelle.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_libelle = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=10)

        self.label_type = ctk.CTkLabel(self.cadreInfo, text="Type :")
        self.label_type.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_type = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_type.grid(row=2, column=1, padx=10, pady=10)

        self.label_capacite = ctk.CTkLabel(self.cadreInfo, text="Capacité :")
        self.label_capacite.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.entry_capacite = ctk.CTkEntry(self.cadreInfo, width=200)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=10)

        self.cadreAction = ctk.CTkFrame(self, corner_radius=10)
        self.cadreAction.pack(pady=10, padx=10, fill="x")
        self.btn_ajouter = ctk.CTkButton(self.cadreAction, text="Ajouter")
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)
        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier")
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)
        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer")
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)
        self.btn_rechercher = ctk.CTkButton(self.cadreAction, text="Rechercher")
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

    def ajouter_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )

        succes, message = self.service_salle.ajouter_salle(salle)

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def modifier_salle(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_libelle.get(),
            self.entry_type.get(),
            self.entry_capacite.get()
        )

        succes, message = self.service_salle.modifier_salle(salle)

        if succes:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)


        self.btn_modifier = ctk.CTkButton(self.cadreAction, text="Modifier", command=self.modifier_salle)

        def supprimer_salle(self):
            code = self.entry_code.get()

            succes, message = self.service_salle.supprimer_salle(code)

            if succes:
                messagebox.showinfo("Succès", message)
            else:
                messagebox.showerror("Erreur", message)

        self.btn_supprimer = ctk.CTkButton(self.cadreAction, text="Supprimer", command=self.supprimer_salle)