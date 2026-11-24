from functions import *


def afficher_menu():
    """Affiche les options du menu"""
    print("\n=== MENU TOURNOI ===")
    print(" 1. Ajouter une équipe")
    print(" 2. Afficher toutes les équipes")
    print(" 3. Saisir résultat d'un match")
    print(" 4. Rechercher une équipe")
    print(" 5. Afficher le classement")
    print(" 6. Afficher le classement (tri manuel)")
    print(" 7. Afficher les statistiques")
    print(" 8. Compter les équipes au-dessus d'un seuil")
    print(" 9. Générer tous les matchs")
    print("10. Comparer recherche linéaire et dichotomique")
    print("11. Quitter")


def creer_equipe_test(nom, victoires, nuls, defaites, buts_marques, buts_encaisses):
    """Crée une équipe de test, les points sont calculés à partir des résultats"""
    return {"nom": nom, "victoires": victoires, "nuls": nuls, "defaites": defaites,
            "buts_marques": buts_marques, "buts_encaisses": buts_encaisses,
            "points": 3 * victoires + nuls}


def donnees_test():
    """Renvoie une liste de 10 équipes de test"""
    # 20 matchs réellement joués (4 journées, chaque équipe a joué 4 fois) :
    # J1 : Paris-Lyon 2-1, Marseille-Nice 1-1, Lille-Lens 0-0, Rennes-Monaco 3-2, Nantes-Brest 1-2
    # J2 : Paris-Marseille 3-0, Lyon-Lille 2-2, Nice-Rennes 1-0, Lens-Nantes 2-1, Monaco-Brest 4-1
    # J3 : Paris-Nice 1-1, Lyon-Monaco 1-3, Marseille-Lens 2-0, Lille-Brest 3-1, Rennes-Nantes 2-2
    # J4 : Paris-Monaco 0-1, Lyon-Nantes 4-0, Marseille-Rennes 1-2, Nice-Lille 0-1, Lens-Brest 1-1
    return [
        #                 nom          V  N  D  BM BE
        creer_equipe_test("Paris SG",  2, 1, 1, 6, 3),
        creer_equipe_test("Lyon",      1, 1, 2, 8, 7),
        creer_equipe_test("Marseille", 1, 1, 2, 4, 6),
        creer_equipe_test("Nice",      1, 2, 1, 3, 3),
        creer_equipe_test("Lille",     2, 2, 0, 6, 3),
        creer_equipe_test("Lens",      1, 2, 1, 3, 4),
        creer_equipe_test("Rennes",    2, 1, 1, 7, 6),
        creer_equipe_test("Monaco",    3, 0, 1, 10, 5),
        creer_equipe_test("Nantes",    0, 1, 3, 4, 10),
        creer_equipe_test("Brest",     1, 1, 2, 5, 9),
    ]


def main():
    """Boucle principale du programme"""
    equipes = donnees_test()
    while True:
        afficher_menu()
        choix = input("Votre choix : ").strip()

        if choix == "1":
            nom = input("\nNom de l'équipe : ")
            ajouter_equipe(equipes, nom)

        elif choix == "2":
            afficher_equipes(equipes)

        elif choix == "3":
            saisir_match(equipes)

        elif choix == "4":
            nom = input("\nNom de l'équipe : ")
            equipe = recherche_lineaire(equipes, nom)
            if equipe is None:
                print("\nÉquipe introuvable.")
            else:
                print(f"\nRésultat : {equipe['nom']} | {formater_stats(equipe)}")

        elif choix == "5":
            afficher_classement(equipes, tri_manuel=False)

        elif choix == "6":
            afficher_classement(equipes, tri_manuel=True)

        elif choix == "7":
            afficher_statistiques(equipes)

        elif choix == "8":
            seuil = demander_entier("\nSeuil de points : ")
            nombre = compter_equipes_recursif(equipes, seuil)
            print(f"{nombre} équipe(s) ont plus de {seuil} points.")

        elif choix == "9":
            afficher_matchs(equipes)

        elif choix == "10":
            nom = input("\nNom de l'équipe : ")
            comparer_recherches(equipes, nom)

        elif choix == "11":
            print("Fin du programme")
            break

        else:
            print("Choix invalide, recommencez.")


if __name__ == "__main__":
    main()
