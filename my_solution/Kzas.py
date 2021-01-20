import pandas as pd
import json
import glob

states = {
    'AC': 'Acre',
    'AL': 'Alagoas',
    'AP': 'Amapá',
    'AM': 'Amazonas',
    'BA': 'Bahia',
    'CE': 'Ceará',
    'DF': 'Distrito Federal',
    'ES': 'Espírito Santo',
    'GO': 'Goiás',
    'MA': 'Maranhão',
    'MT': 'Mato Grosso',
    'MS': 'Mato Grosso do Sul',
    'MG': 'Minas Gerais',
    'PA': 'Pará',
    'PB': 'Paraíba',
    'PR': 'Paraná',
    'PE': 'Pernambuco',
    'PI': 'Piauí',
    'RJ': 'Rio de Janeiro',
    'RN': 'Rio Grande do Norte',
    'RS': 'Rio Grande do Sul',
    'RO': 'Rondônia',
    'RR': 'Roraima',
    'SC': 'Santa Catarina',
    'SP': 'São Paulo',
    'SE': 'Sergipe',
    'TO': 'Tocantins'
} 

# Import data from .csv file
buildings = pd.read_csv('C:/Users/eloah.noguchi/Documents/GitHub\DataEngTest/raw_data/buildings/buildings.csv', low_memory=False)

# Import data from json file
ads_list = []
for x in glob.glob('C:/Users/eloah.noguchi/Documents/GitHub/DataEngTest/raw_data/ads/*.json'):
    with open(f'C:/Users/eloah.noguchi/Documents/GitHub/DataEngTest/raw_data/ads/{x}.json', 'r') as f:
        data = json.load(f)
    df = pd.DataFrame({'value': data})
    ads_list.append(df.transpose())  

ads = pd.concat(ads_list)

# Normalize states
ads['state_normalized'] = ads.state.apply(lambda x: states[x])
buildings['state_normalized'] = buildings.state.apply(lambda x: states[x] if x in states else x)

df_merge = 

buildings.head(10)
ads.head(2).transpose()

ads.lat.value_counts(dropna=False, normalize=True)
ads.state_normalized.unique()
buildings.state_normalized.unique()
