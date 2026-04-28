from joueur import Joueur
from action import Passe, Tir
from possession import Possession

j = Joueur("001", "Reda Hajhouj", "FUS Rabat", "Attaquant")

p1 = Passe(j, "00:10:00", 60, 40, 80, 40, 20, 0.02)
p2 = Passe(j, "00:11:00", 80, 40, 100, 38, 25, 0.05)
t1 = Tir(j, "00:37:00", 114, 35, 0.79, True, 0.64)

pos = Possession("84", "FUS Rabat")
pos.ajouter_action(p1)
pos.ajouter_action(p2)
pos.ajouter_action(t1)

print(pos)
print("P(marquer):", pos.probabilite_marquer())
print("P(encaisser):", pos.probabilite_encaisser())