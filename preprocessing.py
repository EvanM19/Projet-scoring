import pandas as pd
from sklearn.model_selection import train_test_split

excel_data = pd.read_excel('data/prolib.xlsx',  sheet_name=['app_test', 'oot'])

data_sample = excel_data['app_test'].sample(frac=0.1, random_state=42) 
oot_sample = excel_data['oot'].sample(frac=0.1, random_state=42)

train, test = train_test_split(data_sample, test_size=0.25, random_state=42)

print("Taille de l'échantillon data (10%) :", data_sample.shape)
print("Taille de l'échantillon OOT (10%) :", oot_sample.shape)
print("Taille de l'ensemble d'entraînement :", train.shape)
print("Taille de l'ensemble de test :", test.shape)

# Vérifier le taux de défault ! 