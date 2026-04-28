from joueur import Joueur

j = Joueur("001", "Reda Hajhouj", "FUS Rabat", "Attaquant")
print(j)
print("Actions:", j.get_actions())
print("VAEP total:", j.vaep_total())