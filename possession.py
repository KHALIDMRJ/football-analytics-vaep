from action import Tir

class Possession:

    def __init__(self, id_possession, equipe):
        self.id_possession = id_possession
        self.equipe = equipe
        self.__actions = []

    def ajouter_action(self, action):
        self.__actions.append(action)

    def get_actions(self):
        return self.__actions

    def nb_actions(self):
        return len(self.__actions)

    def calculer_VAEP(self):
        return sum(a.vaep for a in self.__actions)

    def calculer_XG(self):
        return sum(a.xg for a in self.__actions if isinstance(a, Tir))

    def probabilite_marquer(self, k=5):
        actions_k = self.__actions[:k]
        valeurs = [a.vaep for a in actions_k if a.vaep > 0]
        if not valeurs:
            return 0.0
        return min(sum(valeurs), 1.0)

    def probabilite_encaisser(self, k=5):
        actions_k = self.__actions[:k]
        valeurs = [a.vaep for a in actions_k if a.vaep < 0]
        if not valeurs:
            return 0.0
        return min(abs(sum(valeurs)), 1.0)

    def __str__(self):
        return (f"Possession {self.id_possession} - {self.equipe}: "
                f"{self.nb_actions()} actions | "
                f"VAEP={self.calculer_VAEP():.4f} | "
                f"XG={self.calculer_XG():.4f}")