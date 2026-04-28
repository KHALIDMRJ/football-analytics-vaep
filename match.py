import csv
from joueur import Joueur
from action import Passe, Tir, Dribble, Action
from possession import Possession

class Match:

    def __init__(self, fichier_csv):
        self.fichier_csv = fichier_csv
        self.__joueurs = {}
        self.__possessions = {}
        self.__charger_donnees()

    def __charger_donnees(self):
        with open(self.fichier_csv, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            lignes_vues = set()
            for row in reader:
                cle = (row['id'], row['player_id'], row['event_type_name'])
                if cle in lignes_vues:
                    continue
                lignes_vues.add(cle)
                self.__traiter_ligne(row)

    def __traiter_ligne(self, row):
        id_j = row['player_id']
        if not id_j:
            return

        if id_j not in self.__joueurs:
            self.__joueurs[id_j] = Joueur(
                id_j,
                row['player_name'],
                row['team_name'],
                row['player_position_name']
            )

        joueur = self.__joueurs[id_j]

        id_pos = row['possession']
        equipe_pos = row['possession_team_name']
        if id_pos not in self.__possessions:
            self.__possessions[id_pos] = Possession(id_pos, equipe_pos)

        possession = self.__possessions[id_pos]

        vaep = float(row['obv_total_net']) if row['obv_total_net'] else 0.0
        loc_x = float(row['location_x']) if row['location_x'] else 0.0
        loc_y = float(row['location_y']) if row['location_y'] else 0.0
        timestamp = row['timestamp']
        event_type = row['event_type_name']

        if event_type == 'Pass':
            dest_x = float(row['end_location_x']) if row['end_location_x'] else loc_x
            dest_y = float(row['end_location_y']) if row['end_location_y'] else loc_y
            longueur = float(row['pass_length']) if row['pass_length'] else 0.0
            action = Passe(joueur, timestamp, loc_x, loc_y,
                          dest_x, dest_y, longueur, vaep)

        elif event_type == 'Shot':
            xg = float(row['statsbomb_xg']) if row['statsbomb_xg'] else 0.0
            but = row['outcome_name'] == 'Goal'
            action = Tir(joueur, timestamp, loc_x, loc_y, xg, but, vaep)

        elif event_type == 'Dribble':
            reussi = row['outcome_name'] == 'Complete'
            action = Dribble(joueur, timestamp, loc_x, loc_y, reussi, vaep)

        else:
            action = Action(joueur, timestamp, loc_x, loc_y, vaep)

        possession.ajouter_action(action)
        joueur.ajouter_action(action)

    def get_joueurs(self):
        return list(self.__joueurs.values())

    def get_possessions(self):
        return list(self.__possessions.values())

    def top_joueurs_vaep(self, n=5):
        joueurs = self.get_joueurs()
        return sorted(joueurs, key=lambda j: j.vaep_total(), reverse=True)[:n]

    def analyser(self):
        print("=" * 55)
        print("       ANALYSE DU MATCH - FUS RABAT vs FAR")
        print("=" * 55)
        print(f"Joueurs detectes   : {len(self.__joueurs)}")
        print(f"Possessions totales: {len(self.__possessions)}")
        print()

        print("TOP 5 JOUEURS par VAEP:")
        print("-" * 45)
        for i, j in enumerate(self.top_joueurs_vaep(), 1):
            print(f"  {i}. {j.nom:25} | VAEP: {j.vaep_total():+.4f} | xG: {j.xg_total():.4f}")

        print()
        print("TOP 5 POSSESSIONS les plus dangereuses:")
        print("-" * 45)
        possessions = sorted(self.get_possessions(),
                            key=lambda p: p.calculer_VAEP(),
                            reverse=True)
        for p in possessions[:5]:
            print(f"  {p}")

    def __str__(self):
        return (f"Match charge depuis '{self.fichier_csv}': "
                f"{len(self.__joueurs)} joueurs, "
                f"{len(self.__possessions)} possessions")