import pandas as pd
from sklearn.model_selection import train_test_split

excel_data = pd.read_excel('data/prolib.xlsx',  sheet_name=['app_test', 'oot'])

data_sample = excel_data['app_test'].sample(frac=0.1, random_state=42) 
oot_sample = excel_data['oot'].sample(frac=0.1, random_state=42)

train, test = train_test_split(data_sample, test_size=0.25, random_state=42)

with pd.ExcelWriter('data/samples.xlsx') as writer:
    train.to_excel(writer, sheet_name='train', index=False)
    test.to_excel(writer, sheet_name='test', index=False)
    oot_sample.to_excel(writer, sheet_name='oot', index=False)

