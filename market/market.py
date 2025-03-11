import pandas as pd
from typing import Union

def clean_numeric(x):
    """Helper function to clean numeric values"""
    if pd.isna(x):
        return np.nan
    if isinstance(x, str):
        x = x.replace(',', '').replace(' ', '')
        if x in ['*', '**', '-', 'S', 'N']:
            return np.nan
    try:
        return int(float(x))  # Convert to float first, then to int
    except:
        return np.nan


def calc_hhi(df: pd.DataFrame,
             naics_code: Union[int, str],
             naics_var: str,
             empl_var: str) -> float:
    """
    Calculates the Herfindahl-Hirschman Index (HHI) for a given NAICS code.

    Args:
        df (pd.DataFrame): Input dataframe
        naics_code (int or str): 6-digit NAICS code
        naics_var (str): Name of NAICS column
        empl_var (str): Name of employment column

    Returns:
        float: HHI index value
    """

    # Make sure employment is numeric
    df = df.copy()
    df[empl_var] = df[empl_var].apply(clean_numeric)

    # Convert NAICS code to string for comparison
    naics_code = str(naics_code)
    df[naics_var] = df[naics_var].astype(str)

    # Subset data for specific NAICS code
    subset = df[df[naics_var] == naics_code].copy()

    # Sort by employment and keep top 50
    subset = subset.nlargest(50, empl_var)

    # Calculate total employment
    total_empl = subset[empl_var].sum()

    # Calculate market shares and HHI
    subset['share'] = subset[empl_var] / total_empl
    hhi = (subset['share'] ** 2).sum()

    return hhi