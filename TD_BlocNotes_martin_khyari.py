# creation d'un bloc notes

class BlocNotes:
    def __init__(self, fichier):
        self.fichier = fichier
        self.notes = []

    def ajouter_notes(self, nouvelle_note):
        self.notes.append(nouvelle_note)

    def afficher_notes(self):
        for note in self.notes:
            print(note)

    def rechercher_notes(self, mot_cle):
        for note in self.notes:
            if mot_cle in note:
                print(note)


class GestionNotes(BlocNotes):
    def __init__(self, fichier):
        super().__init__(fichier)
        self.notes = []

    def charger_notes(self):
        with open(self.fichier, "r") as f:
            self.notes = f.readlines()

    def sauvegarder_notes(self, notes):
        # partie est fait avec chat gpt
        # on va sauvegarder les notes dans un fichier
        try:
            # on ouvre le fichier en mode écriture
            with open(self.fichier, 'w') as f:
                # on écrit chaque note dans le fichier
                for note in notes:
                    # on ajoute un retour à la ligne
                    f.write(note + '\n')
                    # on affiche un message de confirmation
            print("Le bloc-notes a été sauvegardé.")
        # si on a une erreur
        except Exception as e:
            # on affiche un message d'erreur
            print(f"Erreur lors de la sauvegarde : {e}")


if __name__ == '__main__':
    bloc = "notes.txt"
    bloc = GestionNotes(bloc)

while True:
    print("1. Ajouter une note")
    print("2. Lire les notes")
    print("3. Rechercher une note")
    print("4. Sauvergarder les notes")
    print("5. Charger les notes")
    print("6. Quitter")

    choix = input("Que voulez-vous faire ?")

    if choix == "1":
        nouvelle_note = input("Entrez votre note : ")
        bloc.ajouter_notes(nouvelle_note)
    elif choix == "2":
        bloc.afficher_notes()
    elif choix == "3":
        mot_cle = input("Entrez un mot clé : ")
        bloc.rechercher_notes(mot_cle)
    elif choix == "4":
        bloc.sauvegarder_notes(bloc.notes)
    elif choix == "5":
        bloc.charger_notes()
    elif choix == "6":
        print("Au revoir")
        break
    else:
        print("Choix invalide")
