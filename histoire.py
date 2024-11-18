class Personnage:
    """
    Représente le personnage principal du jeu.
    """
    def __init__(self, nom):
        self.nom = nom
        self.position = [0, 0]  # Position initiale (x, y)

    def deplacer(self, direction):
        """
        Déplace le personnage dans la direction donnée.
        :param direction: 'z', 's', 'q', 'd' pour Nord, Sud, Ouest, Est
        """
        if direction == 'z':  # Nord
            self.position[1] += 1
        elif direction == 's':  # Sud
            self.position[1] -= 1
        elif direction == 'q':  # Ouest
            self.position[0] -= 1
        elif direction == 'd':  # Est
            self.position[0] += 1
        else:
            raise ValueError("Direction invalide. Utilisez 'z', 's', 'q', ou 'd'.")
    
    def afficher_position(self):
        """
        Affiche la position actuelle du personnage.
        """
        print(f"{self.nom} est maintenant à la position {self.position}.")


# Début du jeu
print("Bienvenue dans le Monde des Singes !")

# Demander le nom du joueur
nom_joueur = input("Quel est ton nom, aventurier ? ")
joueur = Personnage(nom=nom_joueur)

# Boucle principale du jeu
while True:
    print("\nOù veux-tu aller ?")
    print("Nord : 'z', Sud : 's', Ouest : 'q', Est : 'd'")
    choix = input("Choisis une direction : ").lower()

    try:
        joueur.deplacer(choix)
        joueur.afficher_position()
    except ValueError:
        print("Entrée invalide. Utilise 'z', 's', 'q', ou 'd' pour te déplacer.")
