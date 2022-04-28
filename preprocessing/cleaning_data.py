import pandas as pd

def preprocess():
    pass

def csv_cleaner():
    df = pd.read_csv('/Users/wvdvijve/Documents/GitHub/becode-projects/Immo-Eliza-deployment/data/property_loft.csv')
    df_simple = df[['Price', 'Area']]
    df_simple = df_simple.dropna()
    df_simple = df_simple[df_simple['Price'].apply(lambda x: x.isnumeric())==True]
    df_simple = df_simple[df_simple['Area'].apply(lambda x: x.isnumeric())==True]
    df_simple['Price'] = df_simple['Price'].apply(float)
    df_simple['Area'] = df_simple['Area'].apply(float)
    df_simple.to_csv('CleanData.csv')

  

csv_cleaner()