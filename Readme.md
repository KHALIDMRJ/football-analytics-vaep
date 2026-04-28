<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=28&pause=1000&color=00D4FF&center=true&vCenter=true&width=700&lines=Football+Analytics+%F0%9F%8F%9F%EF%B8%8F;VAEP+%7C+xG+%7C+xT+%7C+OOP+Python;FUS+Rabat+Match+Analysis" alt="Typing SVG" />

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Paradigm-OOP-FF6B35?style=for-the-badge&logo=databricks&logoColor=white)
![Status](https://img.shields.io/badge/Status-Production%20Ready-00C851?style=for-the-badge&logo=checkmarx&logoColor=white)
![License](https://img.shields.io/badge/License-Academic-9B59B6?style=for-the-badge&logo=opensourceinitiative&logoColor=white)
![Data](https://img.shields.io/badge/Data-StatsBomb-E74C3C?style=for-the-badge&logo=databricks&logoColor=white)

<br/>

> **Système d'analyse avancée de matchs de football basé sur la Programmation Orientée Objet (POO) en Python.**  
> Calcule automatiquement les métriques **VAEP**, **xG**, **xT** à partir de données réelles (FUS Rabat vs FAR).

<br/>

---

</div>

## 📋 Table des matières

- [📌 Présentation du projet](#-présentation-du-projet)
- [🎯 Objectifs](#-objectifs)
- [🧠 Concepts OOP utilisés](#-concepts-oop-utilisés)
- [📐 Architecture des classes](#-architecture-des-classes)
- [📊 Diagramme UML](#-diagramme-uml)
- [🔄 Diagramme de cas d'utilisation](#-diagramme-de-cas-dutilisation)
- [📁 Structure du projet](#-structure-du-projet)
- [📚 Métriques calculées](#-métriques-calculées)
- [⚡ Installation & Lancement](#-installation--lancement)
- [📈 Exemple de sortie](#-exemple-de-sortie)
- [👥 Auteurs](#-auteurs)

---

## 📌 Présentation du projet

Ce projet est un mini-projet académique développé dans le cadre du module **Programmation Orientée Objet (POO)**. Il s'appuie sur le framework **VAEP** *(Valuing Actions by Estimating Probabilities)*, issu d'un article de recherche présenté à **KDD 2019** et **IJCAI 2020** par Tom Decroos et al.

Le système analyse les événements d'un vrai match de football (données **StatsBomb**) pour évaluer objectivement la contribution de chaque joueur via des métriques avancées.

### 📖 Référence scientifique

> Decroos, T., Bransen, L., Van Haaren, J., & Davis, J. (2020).  
> **VAEP: An Objective Approach to Valuing On-the-Ball Actions in Soccer.**  
> *IJCAI-20 Sister Conferences Best Papers Track.*

---

## 🎯 Objectifs

| Objectif | Description |
|----------|-------------|
| 🏗️ **Modélisation OOP** | Concevoir un système orienté objet complet pour un match de football |
| ⚽ **Intervenants** | Modéliser tous les intervenants : joueurs, balle, actions, possessions |
| 📊 **Métriques** | Calculer XG, DXG, XT, DXT, VAEP pour chaque action |
| 🔢 **VAEP** | Implémenter `VAEP = P(marquer en k actions) - P(encaisser en k actions)` |
| 📁 **Données réelles** | Analyser les données du match FUS Rabat (StatsBomb format) |

---

## 🧠 Concepts OOP utilisés

```
╔══════════════════════════════════════════════════════════════╗
║                    CONCEPTS POO APPLIQUÉS                    ║
╠══════════════════════════════════════╦═══════════════════════╣
║  Concept                             ║  Où dans le code      ║
╠══════════════════════════════════════╬═══════════════════════╣
║  ✅ Classes & Objets                 ║  Tous les fichiers    ║
║  ✅ Constructeur __init__            ║  Chaque classe        ║
║  ✅ Encapsulation (__)               ║  Joueur, Match        ║
║  ✅ Héritage (super())               ║  Passe, Tir, Dribble  ║
║  ✅ Polymorphisme                    ║  calculer_valeur()    ║
║  ✅ Méthodes spéciales (__str__)     ║  Toutes les classes   ║
║  ✅ isinstance()                     ║  Possession           ║
║  ✅ Abstraction                      ║  Action (classe mère) ║
╚══════════════════════════════════════╩═══════════════════════╝
```

### 🔑 Points clés

**Encapsulation** — Les attributs sensibles sont privés (double underscore) :
```python
class Joueur:
    def __init__(self, id_joueur, nom, equipe):
        self.__actions = []   # privé → inaccessible de l'extérieur

    def get_actions(self):    # getter pour y accéder proprement
        return self.__actions
```

**Héritage + Polymorphisme** — Chaque type d'action redéfinit `calculer_valeur()` :
```python
class Action:                          # classe MÈRE
    def calculer_valeur(self):
        return self.vaep               # comportement par défaut

class Tir(Action):                     # classe FILLE
    def calculer_valeur(self):         # POLYMORPHISME : redéfinition
        if self.but:
            return 1.0 - self.xg      # comportement spécifique au Tir
        return -self.xg
```

---

## 📐 Architecture des classes

```
projet_foot/
│
├── 📄 balle.py          →  Classe Balle
│     └── Attributs privés : __x, __y
│     └── Méthodes : get_position(), set_position(), en_zone_dangereuse()
│
├── 📄 joueur.py         →  Classe Joueur
│     └── Attributs : id_joueur, nom, equipe, position
│     └── Privé : __actions (liste des actions du joueur)
│     └── Méthodes : vaep_total(), xg_total(), ajouter_action()
│
├── 📄 action.py         →  Classes Action + sous-classes
│     ├── Action          (classe mère abstraite)
│     ├── Passe(Action)   (hérite → héritage)
│     ├── Tir(Action)     (hérite → héritage)
│     └── Dribble(Action) (hérite → héritage)
│     └── Chacune redéfinit calculer_valeur() → polymorphisme
│
├── 📄 possession.py     →  Classe Possession
│     └── Contient une liste d'actions
│     └── Calcule VAEP, XG, probabilité marquer/encaisser
│
├── 📄 match.py          →  Classe Match (point central)
│     └── Charge le fichier CSV
│     └── Crée automatiquement Joueurs, Actions, Possessions
│     └── Génère les analyses et classements
│
├── 📄 main.py           →  Point d'entrée
└── 📊 fus_FAR.csv       →  Données réelles StatsBomb
```

---

## 📊 Diagramme UML

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        DIAGRAMME DE CLASSES UML                              │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐                              ┌──────────────────────────┐
  │    Balle     │                              │         Joueur           │
  ├──────────────┤                              ├──────────────────────────┤
  │ - __x: float │                              │ + id_joueur: str         │
  │ - __y: float │                              │ + nom: str               │
  ├──────────────┤                              │ + equipe: str            │
  │+get_position │                              │ + position: str          │
  │+set_position │                              │ - __actions: list        │
  │+en_zone_dan. │                              ├──────────────────────────┤
  └──────────────┘                              │ + vaep_total(): float    │
                                                │ + xg_total(): float      │
                                                │ + ajouter_action(action) │
                                                └──────────────────────────┘
                                                            ▲
                                                            │ utilise
                    ┌───────────────────────────────────────┤
                    │                                       │
          ┌─────────┴──────────────────────┐               │
          │         «abstract»             │               │
          │           Action               │───────────────┘
          ├────────────────────────────────┤
          │ + joueur: Joueur               │
          │ + timestamp: str               │
          │ + loc_x, loc_y: float          │
          │ + vaep: float                  │
          ├────────────────────────────────┤
          │ + calculer_valeur(): float     │
          │ + distance_au_but(): float     │
          │ + __str__(): str               │
          └────────────────────────────────┘
                         △ héritage
          ┌──────────────┼──────────────────┐
          │              │                  │
  ┌───────┴──────┐ ┌─────┴──────┐ ┌────────┴───────┐
  │    Passe     │ │    Tir     │ │    Dribble     │
  ├──────────────┤ ├────────────┤ ├────────────────┤
  │+dest_x: float│ │+xg: float  │ │+reussi: bool   │
  │+dest_y: float│ │+but: bool  │ ├────────────────┤
  │+longueur:flt │ ├────────────┤ │+calculer_valeur│ ← polymorphisme
  ├──────────────┤ │+calculer_v.│ │+__str__()      │
  │+calculer_val.│ │+__str__()  │ └────────────────┘
  │+__str__()    │ └────────────┘
  └──────────────┘

  ┌─────────────────────────────┐      ◆ contient      ┌──────────────────────────┐
  │        Possession           │◆────────────────────►│          Match           │
  ├─────────────────────────────┤                       ├──────────────────────────┤
  │ + id_possession: str        │                       │ + fichier_csv: str       │
  │ + equipe: str               │                       │ - __joueurs: dict        │
  │ - __actions: list           │                       │ - __possessions: dict    │
  ├─────────────────────────────┤                       ├──────────────────────────┤
  │ + calculer_VAEP(): float    │                       │ + analyser()             │
  │ + calculer_XG(): float      │                       │ + top_joueurs_vaep(n)    │
  │ + probabilite_marquer(k)    │                       │ + get_joueurs()          │
  │ + probabilite_encaisser(k)  │                       │ + get_possessions()      │
  └─────────────────────────────┘                       └──────────────────────────┘
```

---

## 🔄 Diagramme de cas d'utilisation

```
┌──────────────────────────────────────────────────────────────────┐
│                    SYSTÈME D'ANALYSE FOOTBALL                     │
│                                                                    │
│   ┌──────────────────┐        ┌──────────────────────────────┐   │
│   │                  │        │  UC1: Charger données CSV    │   │
│   │                  │───────►│  UC2: Créer joueurs          │   │
│   │                  │        │  UC3: Créer possessions      │   │
│   │   Analyste /     │        │  UC4: Identifier actions     │   │
│   │   Entraîneur     │        └──────────────────────────────┘   │
│   │                  │                                            │
│   │    (Acteur)      │        ┌──────────────────────────────┐   │
│   │                  │───────►│  UC5: Calculer VAEP          │   │
│   │                  │        │  UC6: Calculer xG des tirs   │   │
│   │                  │        │  UC7: Calculer P(marquer)    │   │
│   └──────────────────┘        │  UC8: Calculer P(encaisser)  │   │
│                               └──────────────────────────────┘   │
│                                                                    │
│                               ┌──────────────────────────────┐   │
│                          ┌───►│  UC9:  Afficher top joueurs  │   │
│                          │    │  UC10: Afficher possessions  │   │
│                          │    │  UC11: Analyser le match     │   │
│                          │    └──────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────┘
```

---

## 📁 Structure du projet

```
football-analytics-vaep/
│
├── 📄 README.md                  ← Ce fichier
├── 📊 fus_FAR.csv                ← Données match FUS Rabat (StatsBomb)
│
├── 🐍 balle.py                   ← Classe Balle (encapsulation)
├── 🐍 joueur.py                  ← Classe Joueur
├── 🐍 action.py                  ← Action + Passe, Tir, Dribble (héritage)
├── 🐍 possession.py              ← Classe Possession (VAEP, xG)
├── 🐍 match.py                   ← Classe Match (charge CSV, analyse)
└── 🐍 main.py                    ← Point d'entrée principal
```

---

## 📚 Métriques calculées

### ⚽ VAEP (Valuing Actions by Estimating Probabilities)

La formule fondamentale :

```
VAEP(action_i) = V(état_i) - V(état_i-1)

où :  V(état_i) = P_scores(état_i) - P_concedes(état_i)

      P_scores(état_i)   = probabilité de marquer dans les k prochaines actions
      P_concedes(état_i) = probabilité d'encaisser dans les k prochaines actions
```

> Une action `+0.05` → contribue 0.05 buts en faveur de l'équipe  
> Une action `-0.05` → risque de donner 0.05 buts à l'adversaire

### 📐 Métriques disponibles

| Métrique | Description | Colonne CSV |
|----------|-------------|-------------|
| **VAEP** | Valeur totale de l'action | `obv_total_net` |
| **VAEP offensif** | Contribution offensive | `obv_for_net` |
| **VAEP défensif** | Contribution défensive | `obv_against_net` |
| **xG** | Expected Goals (probabilité de but) | `statsbomb_xg` |
| **P(marquer k)** | Probabilité marquer en k actions | calculé dynamiquement |
| **P(encaisser k)** | Probabilité encaisser en k actions | calculé dynamiquement |

---

## ⚡ Installation & Lancement

### Prérequis

```bash
Python 3.10+
Aucune bibliothèque externe requise (stdlib uniquement : csv, math)
```

### Lancement

```bash
# 1. Cloner le projet
git clone https://github.com/votre-username/football-analytics-vaep.git
cd football-analytics-vaep

# 2. Vérifier que le CSV est présent
ls fus_FAR.csv

# 3. Lancer l'analyse
python main.py
```

### Tester chaque classe séparément

```bash
python test_balle.py       # Test classe Balle
python test_joueur.py      # Test classe Joueur
python test_action.py      # Test Passe, Tir, Dribble
python test_possession.py  # Test Possession + VAEP
```

---

## 📈 Exemple de sortie

```
=======================================================
       ANALYSE DU MATCH - FUS RABAT vs FAR
=======================================================
Joueurs detectes   : 24
Possessions totales: 89

TOP 5 JOUEURS par VAEP:
-------------------------------------------------------
  1. Reda Hajhouj              | VAEP: +0.6461 | xG: 0.7970
  2. Naoufel Zerhouni          | VAEP: +0.2340 | xG: 0.1200
  3. Omar Jerrari              | VAEP: +0.1890 | xG: 0.0000
  4. Ayoub Lakred              | VAEP: -0.0120 | xG: 0.0000
  5. ...                       | VAEP: ...     | xG: ...

TOP 5 POSSESSIONS les plus dangereuses:
-------------------------------------------------------
  Possession 84 - FUS Rabat: 6 actions | VAEP=0.7100 | XG=0.7900
  Possession 31 - FAR      : 4 actions | VAEP=0.2300 | XG=0.1500
  ...
```

---

## 🔬 Exemple détaillé — Séquence d'une possession

```
Possession #84 — FUS Rabat (contre-attaque)

  Action 1 : Passe   (60,40)→(80,42)   | VAEP = +0.00  [neutre]
  Action 2 : Passe   (80,42)→(95,38)   | VAEP = -0.01  [légère perte]
  Action 3 : Passe   (95,38)→(105,36)  | VAEP = +0.01  [progression]
  Action 4 : Dribble (105,36)           | VAEP = +0.05  [pénétration]
  Action 5 : Passe   (105,36)→(112,40) | VAEP = +0.09  [décisive]
  Action 6 : Tir ⚽  (114,35)           | VAEP = +0.64  [BUT !]

  VAEP total possession : +0.78
  xG du tir            :  0.797
```

---

## 🧪 Concepts POO démontrés en live

```python
# ── Héritage ───────────────────────────────────────────────────
class Passe(Action):          # Passe hérite de Action
    def __init__(self, ...):
        super().__init__(...)  # appel du constructeur parent

# ── Polymorphisme ───────────────────────────────────────────────
p = Passe(...)
t = Tir(...)
d = Dribble(...)

for action in [p, t, d]:
    print(action.calculer_valeur())   # 3 comportements DIFFÉRENTS
                                       # même nom de méthode → polymorphisme

# ── Encapsulation ───────────────────────────────────────────────
j = Joueur("001", "Reda Hajhouj", "FUS Rabat")
# j.__actions          → AttributeError : inaccessible !
j.get_actions()        # ✅ accès via le getter

# ── isinstance() ────────────────────────────────────────────────
for action in possession.get_actions():
    if isinstance(action, Tir):
        xg_total += action.xg   # traitement spécifique aux tirs
```

---

## 📖 Référence — Cahier des charges

Le projet répond aux exigences suivantes :

- ✅ Conception prenant en compte **tous les intervenants** (joueurs, balle)
- ✅ Méthodes pour calculer **XG, DXG, XT, DXT**
- ✅ **Possession** = équipe qui a la balle
- ✅ **Action** = succession de 2 à 5 passes
- ✅ Pour chaque action : `VAEP = P(marquer k actions) - P(encaisser k actions)`
- ✅ Programme Python **0 erreurs, 0 warnings**
- ✅ **POO** privilégiée : héritage, polymorphisme, encapsulation

---

## 👥 Auteurs

| Nom | Établissement |
|-----|---------------|
| Étudiant(e) 1 | [Votre université] |
| Étudiant(e) 2 | [Votre université] |

**Module** : Programmation Orientée Objet (POO)  
**Année** : 2025–2026  
**Encadrant** : [Nom du professeur]

---

<div align="center">

**⭐ Si ce projet vous a aidé, n'oubliez pas de laisser une étoile !**

![Made with Python](https://img.shields.io/badge/Made%20with-Python-1f425f?style=flat-square&logo=python)
![Football Analytics](https://img.shields.io/badge/Football-Analytics-00D4FF?style=flat-square&logo=databricks)
![OOP](https://img.shields.io/badge/POO-Héritage%20%7C%20Polymorphisme%20%7C%20Encapsulation-FF6B35?style=flat-square)

</div>