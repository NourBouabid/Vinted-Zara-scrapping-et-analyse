# Analyse de la décote des vêtements d’occasion — Vinted et Zara

Projet réalisé par **Marya Khelifa et Nour Bouabid**.

## Objectif

Étudier la **décote d’articles d’occasion** à partir de caractéristiques des annonces Vinted et d’une variable de prix de référence Zara. Le prix Vinted représente le prix d'occasion tandis que le prix Zara représente le prix neuf. Les données sont issues de scrapping des sites https://www.zara.com/fr/ et https://www.vinted.fr/. L’analyse comporte une exploration descriptive, une segmentation non supervisée et une modélisation supervisée de la décote.

## Données

Le notebook d’analyse appelle `run_data_preparation()` depuis le module **`data_preparation.py`**, puis charge **`data_final.csv`**. Ce dataset final contient **384 articles** et **10 variables** :

| Variables | Contenu utilisé dans le notebook |
|---|---|
| `etat`, `matiere`, `couleur`, `categorie`, `collection` | Caractéristiques catégorielles des articles |
| `likes` | Nombre de favoris |
| `prix`, `prix_total` | Variables de prix des annonces |
| `prix_moyen_zara` | Prix moyen de référence Zara |
| `decote` | Variable analysée et prédite |

Le calcul exact de `decote` et le détail des opérations de nettoyage sont gérés en amont dans les modules `cleaning.py`, `feature.py` et `data_preparation.py`. Quand au code de scrapping il est réalisé dans des notebooks situés dans le dossier `scrapping_code`.

## Démarche

### Analyse exploratoire

- Statistiques descriptives sur les prix, les favoris et la décote ; répartition des caractéristiques des articles.
- Histogrammes, nuages de points et comparaison de la décote selon l’état, la catégorie, la matière, la couleur et la collection.
- Pour certaines visualisations descriptives, filtrage des modalités de catégorie et de matière disposant d’au moins dix observations (**336 articles conservés**).

### Segmentation non supervisée

- Standardisation des variables numériques et encodage *one-hot* des variables catégorielles.
- Comparaison de plusieurs valeurs de `k` au moyen de l’inertie et du score de silhouette.
- Application de **K-means**, puis visualisation des groupes par **ACP à deux composantes**.

### Modélisation supervisée

- Prédiction de `decote` à partir de `likes`, `etat`, `categorie`, `collection`, `matiere` et `couleur`.
- Découpage aléatoire **75 % entraînement / 25 % test** (`random_state=42`).
- Prétraitement numérique/catégoriel et **régression Ridge**.
- Évaluation par `R²` et `RMSE` ; examen des coefficients du modèle et des modalités associées.
