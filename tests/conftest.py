import pytest
import pandas as pd

from src.data import load_and_save_titanic_df

@pytest.fixture(scope="session")
def titanic_df() -> pd.DataFrame:
    df = load_and_save_titanic_df()
    return df