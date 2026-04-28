from joueur import Joueur
from action import Passe, Tir, Dribble

j = Joueur("001", "Reda Hajhouj", "FUS Rabat", "Attaquant")

p = Passe(j, "00:10:00", 60, 40, 80, 40, 20, 0.02)
t = Tir(j, "00:37:00", 114, 35, 0.79, True, 0.64)
d = Dribble(j, "00:20:00", 90, 45, True, 0.05)

print(p)
print(t)
print(d)

print("Valeur passe:", p.calculer_valeur())
print("Valeur tir:", t.calculer_valeur())
print("Distance au but:", round(t.distance_au_but(), 2))