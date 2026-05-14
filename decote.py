import pandas as pd

df_vinted=pd.read_csv('vinted_data_clean.csv')
df_zara=pd.read_csv('zara_data_clean.csv')

def prix_moyen_zara(categorie, collection, couleur, matiere):

    """
    Renvoie le prix moyen Zara neuf correspondant aux critères donnés.
    
    niveaux de filtrage :
    1. catégorie + collection + couleur + matière
    2. catégorie + collection + couleur
    3. catégorie + collection
    4. catégorie
    """
    df = df_zara.copy()

    # Niveau 1 : tous les critères
    filtre = (
        (df['categorie'] == categorie) &
        (df['collection'] == collection) &
        (df['couleur'] == couleur) &
        (df['matiere'] == matiere)
    )

    resultats = df[filtre]

    if len(resultats) > 0:
        return resultats['prix'].mean()
    else:

        # Niveau 2 : sans la matière
        filtre = (
            (df['categorie'] == categorie) &
            (df['collection'] == collection) &
            (df['couleur'] == couleur)
        )

        resultats = df[filtre]

        if len(resultats) > 0:
            return resultats['prix'].mean()
        else:
            # Niveau 3 : sans la matière ni la couleur
            filtre = (
                (df['categorie'] == categorie) &
                (df['collection'] == collection)
            )

            resultats = df[filtre]

            if len(resultats) > 0:
                return df[df['collection'] == collection]['prix'].mean()

df_vinted['prix_moyen_zara'] = df_vinted.apply(
    lambda ligne: prix_moyen_zara(
        ligne['categorie'],
        ligne['collection'],
        ligne['couleur'],
        ligne['matiere']
    ),
    axis=1
)

df_vinted['decote'] = 1 - df_vinted['prix'] / df_vinted['prix_moyen_zara']