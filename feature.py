def prix_moyen_zara(df_zara,categorie, collection, couleur, matiere):

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
        (df['matiere'] == matiere)
    )

    resultats = df[filtre]

    if len(resultats) > 0:
        print('niveau 1')
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
                return resultats['prix'].mean()
                
            else:
                return df[df['collection'] == collection]['prix'].mean()