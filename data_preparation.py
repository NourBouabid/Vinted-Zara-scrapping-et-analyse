import pandas as pd
from pathlib import Path
from cleaning import zara_clean_data, vinted_clean_data
from feature import prix_moyen_zara

try:
    BASEDIR = Path(__file__).resolve().parent.parent
except NameError:
    BASEDIR = Path.cwd()

data_dir=BASEDIR/'data'
data_dir.mkdir(parents=True, exist_ok=True)

def run_data_preparation():

    df_vinted_brute=pd.read_csv(data_dir/'vinted_data.csv')
    df_zara_brute=pd.read_csv(data_dir/'zara_data.csv')

    df_vinted=vinted_clean_data(df_vinted_brute)
    df_zara=zara_clean_data(df_zara_brute)

    df_vinted['prix_moyen_zara'] = df_vinted.apply(
    lambda ligne: prix_moyen_zara( df_zara,
        ligne['categorie'],
        ligne['collection'],
        ligne['couleur'],
        ligne['matiere']
    ),
    axis=1
    )

    df_vinted['decote'] = 1 - df_vinted['prix'] / df_vinted['prix_moyen_zara']

    df_vinted.to_csv(data_dir/"data_final.csv", index=False, encoding="utf-8-sig")