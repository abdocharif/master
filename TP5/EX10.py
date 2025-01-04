import csv
import os

# Fichier CSV pour stocker les contacts
FICHIER_CONTACTS = "contacts.csv"

# Initialiser le fichier si nécessaire
if not os.path.exists(FICHIER_CONTACTS):
    with open(FICHIER_CONTACTS, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Nom", "Âge", "Ville"])


# Ajouter un contact
def ajouter_contact():
    with open(FICHIER_CONTACTS, "a", newline="") as file:
        writer = csv.writer(file)
        nom = input("Entrez le nom : ")
        age = input("Entrez l'âge : ")
        ville = input("Entrez la ville : ")
        writer.writerow([nom, age, ville])
        print("Contact ajouté avec succès !")


# Afficher tous les contacts
def afficher_contacts():
    with open(FICHIER_CONTACTS, "r") as file:
        reader = csv.DictReader(file)
        print("\nListe des contacts :")
        for row in reader:
            print(f"Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")
        print()


# Rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Entrez le nom du contact à rechercher : ")
    with open(FICHIER_CONTACTS, "r") as file:
        reader = csv.DictReader(file)
        found = False
        for row in reader:
            if row["Nom"].lower() == nom_recherche.lower():
                print(f"Contact trouvé : Nom : {row['Nom']}, Âge : {row['Âge']}, Ville : {row['Ville']}")
                found = True
        if not found:
            print("Aucun contact trouvé avec ce nom.")


# Supprimer un contact
def supprimer_contact():
    nom_supprimer = input("Entrez le nom du contact à supprimer : ")
    contacts = []
    with open(FICHIER_CONTACTS, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Nom"].lower() != nom_supprimer.lower():
                contacts.append(row)
    if len(contacts) < sum(1 for _ in open(FICHIER_CONTACTS)) - 1:  # Ligne d'en-tête exclue
        with open(FICHIER_CONTACTS, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["Nom", "Âge", "Ville"])
            writer.writeheader()
            writer.writerows(contacts)
        print("Contact supprimé avec succès.")
    else:
        print("Aucun contact trouvé avec ce nom.")


# Menu principal
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")

        choix = input("Entrez votre choix (1-5) : ")
        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")


# Lancer le programme
if __name__ == "__main__":
    menu()
