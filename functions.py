# ===== Gestion des équipes =====

def creer_equipe(nom):
    """Crée une équipe avec son nom, les autres caractéristiques sont à 0"""
    return {"nom": nom, "victoires": 0, "nuls": 0, "defaites": 0,
            "buts_marques": 0, "buts_encaisses": 0, "points": 0}


def recherche_lineaire(equipes, nom_equipe):
    """Renvoie le dictionnaire de l'équipe si elle est dans la liste, None sinon"""
    for equipe in equipes:
        if equipe["nom"].lower() == nom_equipe.strip().lower():
            return equipe
    return None


def ajouter_equipe(equipes, nom_equipe):
    """Vérifie si le nom est valide et si l'équipe existe déjà, sinon l'ajoute"""
    nom_equipe = nom_equipe.strip()
    if nom_equipe == "":
        print("Erreur : le nom ne peut pas être vide.")
    elif recherche_lineaire(equipes, nom_equipe) is None:
        equipes.append(creer_equipe(nom_equipe))
        print(f'Équipe "{nom_equipe}" ajoutée avec succès !')
    else:
        print("Erreur : cette équipe existe déjà.")


def matchs_joues(equipe):
    """Renvoie le nombre de matchs joués par une équipe"""
    return equipe["victoires"] + equipe["nuls"] + equipe["defaites"]


def difference_buts(equipe):
    """Renvoie la différence entre buts marqués et buts encaissés"""
    return equipe["buts_marques"] - equipe["buts_encaisses"]


def formater_stats(equipe):
    """Renvoie les statistiques d'une équipe sous forme de texte"""
    return (f"{equipe['points']:>2} pts | "
            f"V:{equipe['victoires']} N:{equipe['nuls']} D:{equipe['defaites']} | "
            f"Buts: {equipe['buts_marques']:>2}-{equipe['buts_encaisses']:<2} | "
            f"Diff: {difference_buts(equipe):+d}")


def afficher_equipes(equipes):
    """Affiche toutes les équipes, numérotées, avec leurs statistiques"""
    if len(equipes) == 0:
        print("Aucune équipe enregistrée.")
        return

    print("\n=== ÉQUIPES ===")
    for numero, equipe in enumerate(equipes, start=1):
        print(f"{numero:>2}. {equipe['nom']:<15} | {formater_stats(equipe)}")


# ===== Saisie des matchs =====

def demander_entier(message):
    """Demande un entier positif ou nul, redemande si la saisie est invalide"""
    while True:
        saisie = input(message)
        try:
            nombre = int(saisie)
        except ValueError:
            print("Erreur : il faut saisir un nombre entier.")
            continue
        if nombre < 0:
            print("Erreur : le nombre ne peut pas être négatif.")
        else:
            return nombre


def accorder(nombre, singulier, pluriel):
    """Renvoie le nombre suivi du texte au singulier ou au pluriel (ex : 1 but, 3 buts)"""
    if nombre > 1:
        return f"{nombre} {pluriel}"
    return f"{nombre} {singulier}"


def enregistrer_match(equipes, nom1, nom2, score1, score2):
    """Si l'entrée est correcte, met à jour les équipes après un match"""
    equipe1 = recherche_lineaire(equipes, nom1)
    equipe2 = recherche_lineaire(equipes, nom2)
    if equipe1 is None:
        print(f'Erreur : l\'équipe "{nom1}" n\'existe pas.')
        return False
    if equipe2 is None:
        print(f'Erreur : l\'équipe "{nom2}" n\'existe pas.')
        return False
    if equipe1 is equipe2:
        print("Erreur : une équipe ne peut pas jouer contre elle-même.")
        return False
    if score1 < 0 or score2 < 0:
        print("Erreur : les scores doivent être positifs.")
        return False

    equipe1["buts_marques"] += score1
    equipe1["buts_encaisses"] += score2
    equipe2["buts_marques"] += score2
    equipe2["buts_encaisses"] += score1

    if score1 > score2:
        equipe1["victoires"] += 1
        equipe2["defaites"] += 1
        points1, points2 = 3, 0
    elif score1 < score2:
        equipe2["victoires"] += 1
        equipe1["defaites"] += 1
        points1, points2 = 0, 3
    else:
        equipe1["nuls"] += 1
        equipe2["nuls"] += 1
        points1, points2 = 1, 1
    equipe1["points"] += points1
    equipe2["points"] += points2

    print(f"\nMatch enregistré : {equipe1['nom']} {score1}-{score2} {equipe2['nom']}")
    print(f"- {equipe1['nom']} : +{accorder(points1, 'point', 'points')}, "
          f"+{accorder(score1, 'but marqué', 'buts marqués')}, "
          f"+{accorder(score2, 'but encaissé', 'buts encaissés')}")
    print(f"- {equipe2['nom']} : +{accorder(points2, 'point', 'points')}, "
          f"+{accorder(score2, 'but marqué', 'buts marqués')}, "
          f"+{accorder(score1, 'but encaissé', 'buts encaissés')}")
    return True


def demander_equipe(equipes, message):
    """Demande un nom d'équipe, renvoie l'équipe si elle existe, None sinon"""
    nom = input(message).strip()
    equipe = recherche_lineaire(equipes, nom)
    if equipe is None:
        print(f'Erreur : l\'équipe "{nom}" n\'existe pas.')
    return equipe


def saisir_match(equipes):
    """Demande les équipes et les scores à l'utilisateur, puis enregistre le match"""
    # on vérifie les équipes avant de demander les scores
    equipe1 = demander_equipe(equipes, "Équipe 1 : ")
    if equipe1 is None:
        return
    equipe2 = demander_equipe(equipes, "Équipe 2 : ")
    if equipe2 is None:
        return
    if equipe1 is equipe2:
        print("Erreur : une équipe ne peut pas jouer contre elle-même.")
        return
    score1 = demander_entier(f"Score {equipe1['nom']} : ")
    score2 = demander_entier(f"Score {equipe2['nom']} : ")
    enregistrer_match(equipes, equipe1["nom"], equipe2["nom"], score1, score2)


# ===== Classement et tri =====

def afficher_classement(equipes, tri_manuel=False):
    """Affiche le classement fait sur les points puis la différence de buts,
    avec sorted() ou avec le tri à bulle si tri_manuel vaut True"""
    if len(equipes) == 0:
        print("Aucune équipe enregistrée.")
        return

    if tri_manuel:
        equipes_triees = tri(equipes)
        print("\n=== CLASSEMENT (tri manuel) ===")
    else:
        # le "-" permet de trier en ordre décroissant
        equipes_triees = sorted(equipes, key=lambda e: (-e["points"], -difference_buts(e)))
        print("\n=== CLASSEMENT ===")
    for rang, equipe in enumerate(equipes_triees, start=1):
        print(f"{rang:>2}. {equipe['nom']:<15} | {formater_stats(equipe)}")


def passe_avant(a, b):
    """True si a doit être classé avant b (par points puis différence de buts)"""
    if a["points"] != b["points"]:
        return a["points"] > b["points"]
    return difference_buts(a) > difference_buts(b)


def tri(equipes):
    """Tri à bulle : renvoie une nouvelle liste triée sans modifier l'originale"""
    resultat = list(equipes)
    n = len(resultat)
    # parcourt la liste n-1 fois et échange 2 voisins s'ils sont mal rangés
    for i in range(n - 1):
        for j in range(n - 1 - i):
            # échange seulement si le second doit passer devant (égalité = pas d'échange)
            if passe_avant(resultat[j + 1], resultat[j]):
                resultat[j], resultat[j + 1] = resultat[j + 1], resultat[j]
    return resultat


# ===== Statistiques =====

def afficher_statistiques(equipes):
    """Affiche les statistiques globales des équipes"""
    if len(equipes) == 0:
        print("Aucune équipe enregistrée.")
        return

    # on ignore les équipes qui n'ont pas encore joué
    ont_joue = [e for e in equipes if matchs_joues(e) > 0]
    if len(ont_joue) == 0:
        print("Aucun match joué.")
        return

    plus_de_points = max(ont_joue, key=lambda e: e["points"])
    meilleure_attaque = max(ont_joue, key=lambda e: e["buts_marques"])
    meilleure_defense = min(ont_joue, key=lambda e: e["buts_encaisses"])
    total_buts = sum(e["buts_marques"] for e in equipes)
    moyenne_buts = total_buts / len(equipes)
    # chaque match est compté une fois par équipe
    nombre_matchs = sum(matchs_joues(e) for e in equipes) // 2

    print("\n=== STATISTIQUES ===")
    print(f"Plus de points             : {plus_de_points['nom']} ({plus_de_points['points']} pts)")
    print(f"Meilleure attaque          : {meilleure_attaque['nom']} ({meilleure_attaque['buts_marques']} buts)")
    print(f"Meilleure défense          : {meilleure_defense['nom']} ({meilleure_defense['buts_encaisses']} buts)")
    print(f"Moyenne de buts par équipe : {moyenne_buts:.2f}")
    print(f"Nombre de matchs joués     : {nombre_matchs}")


def compter_equipes_recursif(equipes, seuil_points, index=0):
    """Compte récursivement le nombre d'équipes qui ont plus de points que le seuil"""
    if index == len(equipes):
        return 0
    if equipes[index]["points"] > seuil_points:
        return compter_equipes_recursif(equipes, seuil_points, index + 1) + 1
    return compter_equipes_recursif(equipes, seuil_points, index + 1)


# ===== Génération des matchs =====

def generer_matchs(equipes):
    """Génère tous les matchs possibles sans doublons, renvoie une liste de tuples"""
    matchs = []
    n = len(equipes)
    for i in range(n - 1):
        # j commence après i : pas de match contre soi-même ni de doublon
        for j in range(i + 1, n):
            matchs.append((equipes[i]["nom"], equipes[j]["nom"]))
    return matchs


def afficher_matchs(equipes):
    """Affiche tous les matchs possibles, numérotés"""
    matchs = generer_matchs(equipes)
    if len(matchs) == 0:
        print("Il faut au moins 2 équipes pour générer des matchs.")
        return

    print(f"\n=== MATCHS À JOUER ({len(matchs)}) ===")
    for numero, (nom1, nom2) in enumerate(matchs, start=1):
        print(f"{numero:>2}. {nom1} vs {nom2}")


# ===== Recherche dichotomique =====

def recherche_dichotomique(equipes_triees, nom_recherche):
    """Recherche une équipe par nom dans une liste triée par nom (recherche binaire)
    Renvoie (equipe, nombre de comparaisons), equipe vaut None si elle n'existe pas"""
    nom_recherche = nom_recherche.strip().lower()
    debut = 0
    fin = len(equipes_triees) - 1
    comparaisons = 0
    while debut <= fin:
        milieu = (debut + fin) // 2
        nom_milieu = equipes_triees[milieu]["nom"].lower()
        comparaisons += 1
        if nom_milieu == nom_recherche:
            return equipes_triees[milieu], comparaisons
        # on garde la moitié où peut se trouver le nom
        if nom_milieu < nom_recherche:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return None, comparaisons


def recherche_lineaire_comptee(equipes, nom_recherche):
    """Même parcours que recherche_lineaire, mais compte les comparaisons
    Renvoie (equipe, nombre de comparaisons), equipe vaut None si elle n'existe pas"""
    nom_recherche = nom_recherche.strip().lower()
    comparaisons = 0
    for equipe in equipes:
        comparaisons += 1
        if equipe["nom"].lower() == nom_recherche:
            return equipe, comparaisons
    return None, comparaisons


def comparer_recherches(equipes, nom_recherche):
    """Cherche une équipe avec les deux recherches et compare leurs nombres de comparaisons"""
    # la recherche dichotomique a besoin d'une liste triée par nom
    equipes_triees = sorted(equipes, key=lambda e: e["nom"].lower())
    # "_" : l'équipe trouvée est la même, seul le nombre de comparaisons nous sert
    _, comparaisons_lin = recherche_lineaire_comptee(equipes, nom_recherche)
    equipe_dicho, comparaisons_dicho = recherche_dichotomique(equipes_triees, nom_recherche)

    if equipe_dicho is None:
        print("\nÉquipe introuvable.")
    else:
        print(f"\nRésultat : {equipe_dicho['nom']} | {formater_stats(equipe_dicho)}")
    print(f"Recherche linéaire     : {accorder(comparaisons_lin, 'comparaison', 'comparaisons')}")
    print(f"Recherche dichotomique : {accorder(comparaisons_dicho, 'comparaison', 'comparaisons')}")
