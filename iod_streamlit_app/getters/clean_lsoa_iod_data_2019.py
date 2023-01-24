from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).parents[1]


def get_lsoa_iod_2019() -> pd.DataFrame:
    """Pulling in the Lower Super Output Area (LSOA) IoD data for 2019; with the England regions, LA codes/names, 
    LSOA codes/names and IoD deciles. The lower the decile, the 
    higher the deprivation. 

    Returns:
        pd.DataFrame: Pandas dataframe.
    """    
    return pd.read_csv(f'{BASE_DIR}/inputs/data/lsoa_clean_iod_2019.csv')