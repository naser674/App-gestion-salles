import customtkinter as ctk
from tkinter import ttk, messagebox

from models.salle import Salle
from services.service_salle import ServiceSalle


class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Gestion des salles")
        self.geometry("700x500")

        self.service_salle = ServiceSalle()

        # Cadre informations
        self.frame_info = ctk.CTkFrame(self)
        self.frame_info.pack(pady=10, padx=10, fill="x")

        ctk.CTkLabel(self.frame_info, text="Code :").grid(row=0, column=0, padx=10, pady=5)
        self.entry_code = ctk.CTkEntry(self.frame_info)
        self.entry_code.grid(row=0, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_info, text="Libellé :").grid(row=1, column=0, padx=10, pady=5)
        self.entry_libelle = ctk.CTkEntry(self.frame_info)
        self.entry_libelle.grid(row=1, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_info, text="Type :").grid(row=2, column=0, padx=10, pady=5)
        self.entry_type = ctk.CTkEntry(self.frame_info)
        self.entry_type.grid(row=2, column=1, padx=10, pady=5)

        ctk.CTkLabel(self.frame_info, text="Capacité :").grid(row=3, column=0, padx=10, pady=5)
        self.entry_capacite = ctk.CTkEntry(self.frame_info)
        self.entry_capacite.grid(row=3, column=1, padx=10, pady=5)

        # Cadre actions
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter", command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=5, pady=5)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier", command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=5, pady=5)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer", command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=5, pady=5)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher", command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=5, pady=5)

        # Cadre liste
        self.frame_liste = ctk.CTkFrame(self)
        self.frame_liste.pack(pady=10, padx=10, fill="both", expand=True)

        self.table = ttk.Treeview(
            self.frame_liste,
            columns=("code", "libelle", "type", "capacite"),
            show="headings"
        )

        self.table.heading("code", text="CODE")
        self.table.heading("libelle", text="LIBELLÉ")
        self.table.heading("type", text="TYPE")
        self.table.heading("capacite", text="CAPACITÉ")

        self.table.column("code", width=80)
        self.table.column("libelle", width=180)
        self.table.column("type", width=120)
        self.table.column("capacite", width=100)

        self.table.pack(fill="both", expand=True, padx=10, pady=10)

        self.lister_salles()

    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_libelle.delete(0, "end")
        self.entry_type.delete(0, "end")
        self.entry_capacite.delete(0, "end")

    def ajouter_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )
            succes, message = self.service_salle.ajouter_salle(salle)
            if succes:
                messagebox.showinfo("Succès", message)
                self.lister_salles()
                self.vider_champs()
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre")

    def modifier_salle(self):
        try:
            salle = Salle(
                self.entry_code.get(),
                self.entry_libelle.get(),
                self.entry_type.get(),
                int(self.entry_capacite.get())
            )
            succes, message = self.service_salle.modifier_salle(salle)
            if succes:
                messagebox.showinfo("Succès", message)
                self.lister_salles()
                self.vider_champs()
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "La capacité doit être un nombre")

    def supprimer_salle(self):
        code = self.entry_code.get()
        succes, message = self.service_salle.supprimer_salle(code)
        if succes:
            messagebox.showinfo("Succès", message)
            self.lister_salles()
            self.vider_champs()
        else:
            messagebox.showerror("Erreur", message)

    def rechercher_salle(self):
        code = self.entry_code.get()
        salle = self.service_salle.rechercher_salle(code)

        if salle:
            self.entry_libelle.delete(0, "end")
            self.entry_libelle.insert(0, salle.libelle)

            self.entry_type.delete(0, "end")
            self.entry_type.insert(0, salle.type)

            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, salle.capacite)
        else:
            messagebox.showerror("Erreur", "Salle introuvable")

    def lister_salles(self):
        self.table.delete(*self.table.get_children())
        salles = self.service_salle.recuperer_salles()

        for s in salles:
<<<<<<< HEAD
            self.table.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))
=======
            self.table.insert("", "end", values=(s.code, s.libelle, s.type, s.capacite))
>>>>>>> c5b04b10a85a47a8faefa978589beb42ece1d49e
