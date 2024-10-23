import math
import pandas as pd

from .shiller_header_constants import *

def extract_rolling_windows(df, length_of_window):
    subsets = []
    num_subsets = len(df) - length_of_window + 1

    for start in range(num_subsets):
        subset = df.iloc[start:start + length_of_window].copy()
        if pd.isna(subset.iloc[0][tbills_real_return_header]): continue
        subset.name = df.index[start]
        subset.reset_index(drop=True, inplace=True)
        subsets.append(subset)
        
    subsets = [rebase_column(subset, equities_real_total_return_header) for subset in subsets]
    subsets = [rebase_column(subset, bonds_real_total_return_header) for subset in subsets]
    subsets = [rebase_column(subset, tbills_real_return_header) for subset in subsets]
    
    return subsets

def rebase_column(df, column_name):
    """
    Rebase a DataFrame column by dividing every element by the first element of that column.

    Parameters:
    df (pd.DataFrame): The DataFrame containing the column to rebase.
    column_name (str): The name of the column to rebase.
    """
    # Check if the column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"The column '{column_name}' does not exist in the DataFrame.")
    
    first_value = df[column_name].iloc[0]
    
    if math.isnan(first_value):
        raise ValueError("Cannot rebase on the first value of NaN.")
    if first_value == 0:
        raise ValueError("Cannot rebase on the first value of zero to avoid division by zero.")

    # Rebase the column
    df[column_name] = df[column_name] / first_value

def get_filtered_and_rebased(df, start_date, end_date):
    filtered_df = df.loc[start_date:end_date].copy()

    rebase_column(filtered_df, equities_real_total_return_header)
    rebase_column(filtered_df, bonds_real_total_return_header)
    rebase_column(filtered_df, tbills_real_return_header)
    rebase_column(filtered_df, 'CPI')
    
    return filtered_df

