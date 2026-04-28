import math

class Action:

    def __init__(self, joueur, timestamp, loc_x, loc_y, vaep=0.0):
        self.joueur = joueur
        self.timestamp = timestamp
        self.loc_x = loc_x
        self.loc_y = loc_y
        self.vaep = vaep

    def calculer_valeur(self):
        return self.vaep

    def distance_au_but(self):
        return math.sqrt((120 - self.loc_x)**2 + (40 - self.loc_y)**2)

    def __str__(self):
        return f"Action de {self.joueur.nom} en ({self.loc_x}, {self.loc_y})"


class Passe(Action):

    def __init__(self, joueur, timestamp, loc_x, loc_y,
                 dest_x, dest_y, longueur=0, vaep=0.0):
        super().__init__(joueur, timestamp, loc_x, loc_y, vaep)
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.longueur = longueur

    def calculer_valeur(self):
        gain_x = self.dest_x - self.loc_x
        bonus = 0.01 if gain_x > 0 else -0.005
        return self.vaep + bonus

    def __str__(self):
        return (f"Passe de {self.joueur.nom}: "
                f"({self.loc_x},{self.loc_y}) -> ({self.dest_x},{self.dest_y}) "
                f"VAEP={self.vaep:.4f}")


class Tir(Action):

    def __init__(self, joueur, timestamp, loc_x, loc_y,
                 xg=0.0, but=False, vaep=0.0):
        super().__init__(joueur, timestamp, loc_x, loc_y, vaep)
        self.xg = xg
        self.but = but

    def calculer_valeur(self):
        if self.but:
            return 1.0 - self.xg
        else:
            return -self.xg

    def __str__(self):
        resultat = "BUT" if self.but else "rate"
        return (f"Tir de {self.joueur.nom}: "
                f"xG={self.xg:.3f} {resultat} "
                f"VAEP={self.vaep:.4f}")


class Dribble(Action):

    def __init__(self, joueur, timestamp, loc_x, loc_y,
                 reussi=True, vaep=0.0):
        super().__init__(joueur, timestamp, loc_x, loc_y, vaep)
        self.reussi = reussi

    def calculer_valeur(self):
        return self.vaep if self.reussi else -abs(self.vaep)

    def __str__(self):
        etat = "reussi" if self.reussi else "rate"
        return f"Dribble {etat} de {self.joueur.nom} VAEP={self.vaep:.4f}"