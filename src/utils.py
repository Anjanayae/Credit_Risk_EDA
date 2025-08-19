import pandas as pd

def summary_statistics(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return basic statistics (count, mean, std, etc.) for numeric columns.
    """
    return df.describe()

def missing_values_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Return a table of missing values.
    """
    mis_val = df.isnull().sum()
    mis_val_percent = 100 * mis_val / len(df)
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)
    mis_val_table = mis_val_table.rename(
        columns={0: 'Missing Values', 1: '% of Total Values'}
    )
    return mis_val_table[mis_val_table['Missing Values'] > 0].sort_values(
        '% of Total Values', ascending=False
    )
