import pandas as pd

def load_and_save_titanic_df():
    titanic = pd.read_csv('https://huggingface.co/datasets/ankislyakov/titanic/resolve/main/titanic_train.csv', index_col='PassengerId')
    titanic.to_csv('titanic.csv', index=False)
    return titanic
    
def get_passangers_count_by_pclass(titanic_df: pd.DataFrame, pclass_value: int):
    if len(titanic_df) == 0:
        raise ValueError(f'Dataframe must be not empty!')
    
    if not isinstance(pclass_value, int):
        raise ValueError(f'{pclass_value} must by int type!')
    
    unique_pclasses = list(titanic_df['Pclass'].value_counts().index)
    if pclass_value not in unique_pclasses:
        raise ValueError(f'{pclass_value} is not in current dataframe!')
    
    result = titanic_df.groupby(['Pclass', 'Sex']).size().loc[pclass_value].reset_index().rename(columns={'Sex': 'Пол', 0: 'Количество'})
    return result