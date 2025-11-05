import pytest
import pandas as pd

from src.data import get_passangers_count_by_pclass

@pytest.mark.parametrize("pclass, expected", [
    (1, pd.DataFrame({'Пол': ['female', 'male'], 'Количество': [94, 122]})),
    (2, pd.DataFrame({'Пол': ['female', 'male'], 'Количество': [76, 108]})),
    (3, pd.DataFrame({'Пол': ['female', 'male'], 'Количество': [144, 347]})),
])
def test_get_passangers_count_by_typical_pclasses(
    titanic_df: pd.DataFrame,
    pclass: int,
    expected: pd.DataFrame
):
    result = get_passangers_count_by_pclass(titanic_df, pclass)
    pd.testing.assert_frame_equal(result, expected)
    
@pytest.mark.parametrize("pclass", [
    (-1),
    (4),
    ('f')
])
def test_get_passangers_count_by_invalid_pclasses(
    titanic_df: pd.DataFrame,
    pclass: int,
):
    with pytest.raises(ValueError):
        result = get_passangers_count_by_pclass(titanic_df, pclass)
        
def test_get_passangers_count_with_empty_dataframe():
    empty_df = pd.DataFrame(columns=['Pclass', 'Sex'])
    with pytest.raises(ValueError):
        get_passangers_count_by_pclass(empty_df, 1)