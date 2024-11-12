import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('data/samples.xlsx',  sheet_name=None)


train = data[list(data.keys())[0]]
test = data[list(data.keys())[1]]
oot = data[list(data.keys())[2]]

taux_defaut = (
    train.groupby('datdelhis')['DDefaut_NDB']
    .mean()
    .reset_index()
    .rename(columns={'DDefaut_NDB': 'Taux_de_defaut'})
)

plt.figure(figsize=(10, 6))
plt.plot(taux_defaut['datdelhis'], taux_defaut['Taux_de_defaut'], marker='o', linestyle='-', color='b')
plt.title("Taux de défaut en fonction de datdelhis")
plt.xlabel("Date de l'historique (datdelhis)")
plt.ylabel("Taux de défaut")
plt.xticks(rotation=45)  
plt.grid()
plt.tight_layout()
plt.show()
