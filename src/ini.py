import os
import pandas as pd

from data import load_and_save_titanic_df

def ini():
    if not os.path.exists('./titanic.csv'):
        print('Датафрейм не найден, загружаем..')        
        titanic_df = load_and_save_titanic_df()
        print('Датафрейм загружен!')
        return titanic_df
    
    titanic_df = pd.read_csv('./titanic.csv')
    return titanic_df