class Balle:
    
    def __init__(self, x=0, y=0):
        # On initialise la position de la balle
        self.__x = x
        self.__y = y

    def get_position(self):
        # Cette méthode retourne la position actuelle
        return self.__x, self.__y

    def set_position(self, x, y):
        # Permet de modifier la position de la balle
        self.__x = x
        self.__y = y

    def en_zone_dangereuse(self):
        # On considère que le terrain fait 120m
        # La zone dangereuse correspond aux 18 derniers mètres
        limite = 120 - 18

        if self.__x > limite:
            return True
        else:
            return False

    def __str__(self):
        return "Balle position : (" + str(self.__x) + ", " + str(self.__y) + ")"