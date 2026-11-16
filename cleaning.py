#!/usr/bin/env python3
import pandas as pd
import unicodedata
import warnings
warnings.filterwarnings('ignore')

mapping_zara = {
    # fibres naturelles végétales
    "coton": "fibre naturelle végétale",
    "lin": "fibre naturelle végétale",

    # fibres naturelles animales
    "laine": "fibre naturelle animale",
    "soie (de mûrier)": "fibre naturelle animale",

    # fibres artificielles
    "viscose": "fibre artificielle",
    "lyocell": "fibre artificielle",
    "modal": "fibre artificielle",
    "acétate": "fibre artificielle",
    "diacétate de cellulose": "fibre artificielle",
    "pâte de cellulose": "fibre artificielle",

    # fibres synthétiques
    "polyester": "fibre synthétique",
    "polyamide": "fibre synthétique",
    "acrylique": "fibre synthétique",
    "polyuréthane": "fibre synthétique",
    "polyéthylène": "fibre synthétique",
    "élastomultiester": "fibre synthétique",
    "acétate de vinyle d éthylène": "fibre synthétique",

    # cuir
    "cuir de vache": "cuir",
    "cuir de chèvre": "cuir",
    "cuir de vachette": "cuir",
    "cuir de porc": "cuir",
    "cuir de mouton": "cuir",

    # autres
    "bois de manguier": "autres",
    "papier": "autres",
    "acier inoxydable": "autres",
    "pierre": "autres",
    "verre": "autres",
    "caoutchouc": "autres",
    "fer": "autres",
    "PCTG": "autres",
    "plastique-acrylique": "autres",
    "plastique": "autres",
    "cuivre": "autres",
}


mapping_categories_zara = {
    "hauts et t-shirts": [
        "t-shirt",
        "top",
        "haut",
        "débardeur",
        "chemise",
        "polo",
        "pull",
        "gilet"
    ],

    "pantalons et leggings": [
        "pantalon",
        "legging"
    ],

    "blazers et tailleurs": [
        "blazer"
    ],

    "costumes et tenues particulières": [
        "ensemble",
        "déguisement"
    ],

    "jupe-short": [
        "jupe-short"
    ],

    "combinaisons et combishorts": [
        "combi-short",
        "salopette"
    ],

    "jupes": [
        "jupe"
    ],

    "manteaux et vestes": [
        "veste",
        "blouson",
        "surchemise",
        "poncho",
        "ciré",
        "cape"
    ],

    "accessoires": [
        "bonnet",
        "lunettes",
        "bandana",
        "ceinture",
        "chaussettes",
        "collier",
        "chapeau",
        "porte-clés",
        "casquette",
        "portefeuille",
        "gants"
    ],

    "sweats et sweats à capuche": [
        "sweat"
    ],

    "jeans": [
        "jean"
    ],

    "chaussures": [
        "sandales",
        "mocassins",
        "espadrille",
        "sabots",
        "baskets",
        "ballerines",
        "tennis",
        "basket",
        "claquettes"
    ],

    "robes": [
        "robe"
    ],

    "autres": [
        "lot",
        "frisbee",
        "grande",
        "6-14"
    ],

    "shorts": [
        "short",
        "bermuda",
        "jort"
    ],

    "maillots de bain": [
        "maillot",
        "paréo"
    ],

    "lingerie et pyjamas": [
        
    ],

    "sacs": [
        "sac"
    ]
}

mapping_vinted = {
    "fibres naturelles végétales": [
        "coton",
        "coton, polyester",
        "coton, élasthanne",
        "coton, lin",
        "coton, polyester, laine",
        "coton, polyester, élasthanne",
        "coton, viscose, élasthanne",
        "coton, lin, dentelle",
        "coton, denim",
        "coton, polyester, nylon",
        "lin"
    ],

    "fibres naturelles animales": [
        "laine",
        "polyester, soie, élasthanne"
    ],

    "fibres artificielles": [
        "viscose",
        "viscose, lin, carton",
        "viscose, élasthanne, acrylique",
        "viscose, nylon",
        "viscose, élasthanne",
        "viscose, lin"
    ],

    "fibres synthétiques": [
        "polyester",
        "polyester, élasthanne",
        "polyester, viscose, élasthanne",
        "polyester, viscose",
        "polyester, viscose, nylon",
        "élasthanne",
        "élasthanne, jute"
        
    ],

    "cuir": [
        "cuir",
        "cuir, cuir verni",
        "cuir, cuir synthétique",
        "cuir, daim",
        "daim"
    ],

    "autres": [
        "cuir synthétique",
        "Non précisée"
    ]
}

# Fonction de nettoyage pour les couleurs
def nettoyer_texte(x):
    if pd.isna(x):
        return ""
    x = str(x).lower().strip()
    x = unicodedata.normalize("NFKD", x)
    x = "".join(c for c in x if not unicodedata.combining(c))
    return x

# Appliquer la fonction de nettoyage à la colonne "couleur"
def categoriser_couleur(couleur):
    couleur = nettoyer_texte(couleur)

    if any(mot in couleur for mot in [",","multicolore","rayures", "ecaille", "imprimee", "fleuri", "raye", "leopard", "zebre", "python", "/", "-"]):
        return "motif/multicolore"
    
    elif any(mot in couleur for mot in ["noir", "gris", "anthracite", "argente", "argent", "grisatre", "charbon"]):
        return "noir/gris"

    elif any(mot in couleur for mot in ["blanc", "beige", "écru", "ivoire", "creme"]):
        return "blanc/beige"

    elif any(mot in couleur for mot in ["marron", "camel", "taupe", "chocolat", "brown", "sable"]):
        return "marron"

    elif any(mot in couleur for mot in ["bleu", "marine", "turquoise", "denim", "jean", "indigo"]):
        return "bleu"

    elif any(mot in couleur for mot in ["vert", "kaki", "olive","menthe", "sauge"]):
        return "vert"

    elif any(mot in couleur for mot in ["rouge", "bordeaux", "corail", "brique", "tuile", "pourpre", "grenat"]):
        return "rouge"

    elif any(mot in couleur for mot in ["rose", "violet", "lilas", "fuchsia", "mauve", "vin"]):
        return "rose/violet"

    elif any(mot in couleur for mot in ["jaune", "orange", "ocre", "moutarde", "dore","abricot"]):
        return "jaune/orange"

    else:
        return "autres"

    
def zara_clean_data(Dataset):

    # Mettre tout le texte du dataframe en minuscules
    cols_obj = Dataset.select_dtypes(include="object").columns

    Dataset[cols_obj] = Dataset[cols_obj].apply(
        lambda col: col.str.lower().str.strip()
    )

    # Supprimer les lignes contenant des valeurs manquantes
    Dataset= Dataset.dropna()
    Dataset = Dataset.reset_index(drop=True)

    # Convertir les colonnes "likes", "prix" et "prix_total" en numérique, en remplaçant les valeurs non convertibles par NaN
    Dataset["prix"] = (
        Dataset["prix"]
        .astype(str)
        .str.replace("eur", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )

    Dataset["prix"] = pd.to_numeric(Dataset["prix"], errors="coerce")

    Dataset["couleur"] = Dataset["couleur"].str.replace("|", "", regex=False).str.strip()

    Dataset["couleur"] = Dataset["couleur"].apply(categoriser_couleur)

    # Nettoyage de la colonne "matiere"
    Dataset[["A", "B"]] = (
        Dataset["matiere"]
        .str.extract(r"(\d+)%\s*(.*)")
    )

    Dataset["matiere"] = (
        Dataset["B"]
        .str.split(",")
        .str[0]
        .str.strip()
    )
    Dataset = Dataset.drop(columns=["A", "B"])

    Dataset["matiere"] = (
        Dataset["matiere"]
        .str.strip()
        .str.lower()
        .map(mapping_zara)
        .fillna("autres")
    )

    mapping_categories_inverse = {
        categorie.strip().lower(): famille
        for famille, liste_categories in mapping_categories_zara.items()
        for categorie in liste_categories
    }

    Dataset["categorie"] = (
        Dataset["categorie"]
        .str.strip()
        .str.lower()
        .map(mapping_categories_inverse)
        .fillna("autres")
    )

    return Dataset

def vinted_clean_data(Dataset):
    # Mettre tout le texte du dataframe en minuscules
    cols_obj = Dataset.select_dtypes(include="object").columns

    Dataset[cols_obj] = Dataset[cols_obj].apply(
        lambda col: col.str.lower().str.strip()
    )

    # Remplacer les valeurs manquantes de la colonne "matiere" par "Non précisée"
    Dataset["matiere"] = Dataset["matiere"].fillna("Non précisée")


    mapping_inverse = {
        matiere.strip().lower(): groupe
        for groupe, liste_matieres in mapping_vinted.items()
        for matiere in liste_matieres
    }

    Dataset["matiere"] = (
        Dataset["matiere"]
        .str.strip()
        .str.lower()
        .map(mapping_inverse)
        .fillna("autres")
    )

    Dataset["couleur"] = Dataset["couleur"].apply(categoriser_couleur)

    # Remplacer les valeurs manquantes de la colonne "likes" par 0
    Dataset["likes"] = Dataset["likes"].fillna(0)

    # Supprimer les lignes où la conversion a échoué (valeurs NaN)
    Dataset.drop(columns=["url"], inplace=True)

    # Convertir les colonnes "likes", "prix" et "prix_total" en numérique, en remplaçant les valeurs non convertibles par NaN
    Dataset["prix"] = (
        Dataset["prix"]
        .astype(str)
        .str.replace("\u202f", "", regex=False)
        .str.replace("\xa0", "", regex=False)
        .str.replace("€", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )

    Dataset["prix"] = pd.to_numeric(Dataset["prix"], errors="coerce")
    Dataset["prix_total"] = (
        Dataset["prix_total"]
        .astype(str)
        .str.replace("\u202f", "", regex=False)
        .str.replace("\xa0", "", regex=False)
        .str.replace("€", "", regex=False)
        .str.replace(",", ".", regex=False)
        .str.strip()
    )

    Dataset["prix_total"] = pd.to_numeric(Dataset["prix_total"], errors="coerce")

    return Dataset

