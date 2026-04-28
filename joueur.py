class Joueur:

    def __init__(self, id_joueur, nom, equipe, position="Inconnu"):
        self.id_joueur = id_joueur
        self.nom = nom
        self.equipe = equipe
        self.position = position
        self.__actions = []        # liste privée

    def ajouter_action(self, action):
        self.__actions.append(action)

    def get_actions(self):
        return self.__actions

    def vaep_total(self):
        return sum(a.vaep for a in self.__actions)

    def xg_total(self):
        return sum(a.xg for a in self.__actions if hasattr(a, 'xg'))

    def __str__(self):
        return f"{self.nom} ({self.equipe}) - {self.position}"