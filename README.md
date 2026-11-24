# Gestionnaire de tournoi sportif (Python)

Application console en Python pour gérer un tournoi : saisie des équipes et des résultats, classement, statistiques et génération des matchs. Projet individuel réalisé en cours à l'ECE (Bachelor Intelligence Artificielle).

## Fonctionnalités

- Ajout d'équipes et affichage de la liste
- Saisie du résultat d'un match (victoires, nuls, défaites, buts, points)
- Classement : tri avec `sorted`, ou tri écrit à la main
- Statistiques du tournoi
- Comptage récursif des équipes au-dessus d'un seuil de points
- Génération de tous les matchs
- Comparaison d'une recherche linéaire et d'une recherche dichotomique sur le nombre de comparaisons

## Structure

| Fichier | Rôle |
|---|---|
| `main.py` | Menu interactif et jeu de données de test (10 équipes, 20 matchs) |
| `functions.py` | Fonctions du programme : gestion des équipes, matchs, tris, recherches, récursivité |

## Lancer le programme

Python 3 est nécessaire, sans bibliothèque externe.

```bash
python main.py
```

Le menu propose 11 options (ajout d'équipe, classement, statistiques, recherche, etc.).

## Notions mises en pratique

Dictionnaires et listes, fonctions, tri manuel, recherche linéaire et dichotomique, récursivité, saisies utilisateur contrôlées.

## Auteur

Grégoire Moncet, étudiant en 3e année de Bachelor Intelligence Artificielle à l'ECE.
