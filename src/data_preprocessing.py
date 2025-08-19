import pandas as pd

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values and basic cleaning.
    """
    # Example: fill numeric NaNs with median
    for col in df.select_dtypes(include='number').columns:
        df[col] = df[col].fillna(df[col].median())

    # Example: fill categorical NaNs with mode
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].fillna(df[col].mode()[0])

    return df
