from balle import Balle

b = Balle(60, 40)
print(b)
print("Position:", b.get_position())

b.set_position(110, 35)
print(b)
print("Zone dangereuse?", b.en_zone_dangereuse())