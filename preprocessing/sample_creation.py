import pandas as pd
from sklearn.model_selection import train_test_split

# Charger les données
excel_data = pd.read_excel('data/prolib.xlsx', sheet_name=['app_test', 'oot'])

# Accéder aux DataFrames
data = excel_data['app_test']
oot = excel_data['oot']

# Stratégie de stratification sur les colonnes 'DDefaut_NDB' et 'datdelhis'
# Combiner les deux colonnes dans une nouvelle colonne pour la stratification
stratify_data_column = data[['DDefaut_NDB', 'datdelhis']].astype(str).agg('-'.join, axis=1)
stratify_oot_column = oot[['DDefaut_NDB', 'datdelhis']].astype(str).agg('-'.join, axis=1)

# Sélectionner 10% des données de manière stratifiée pour 'data'
data_sample, _ = train_test_split(data, test_size=0.9, stratify=stratify_data_column, random_state=42)

# Sélectionner 10% des données de manière stratifiée pour 'oot'
oot_sample, _ = train_test_split(oot, test_size=0.9, stratify=stratify_oot_column, random_state=42)

# Créer la colonne de stratification pour 'oot_sample' (ceci pourrait aussi être nécessaire)
stratify_data_sample_column = data_sample[['DDefaut_NDB', 'datdelhis']].astype(str).agg('-'.join, axis=1)

# Diviser data_sample en 75% train et 25% test
train, test = train_test_split(data_sample, test_size=0.25, stratify=stratify_data_sample_column, random_state=42)

with pd.ExcelWriter('data/samples.xlsx') as writer:
    train.to_excel(writer, sheet_name='train', index=False)
    test.to_excel(writer, sheet_name='test', index=False)
    oot_sample.to_excel(writer, sheet_name='oot', index=False)