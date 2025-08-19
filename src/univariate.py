import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_distribution(df: pd.DataFrame, column: str):
    """
    Plot distribution of a single numeric column.
    """
    plt.figure(figsize=(8,5))
    sns.histplot(df[column], kde=True, bins=30)
    plt.title(f"Distribution of {column}")
    plt.show()

def plot_categorical_counts(df: pd.DataFrame, column: str):
    """
    Plot bar chart of counts for a categorical variable.
    """
    plt.figure(figsize=(8,5))
    sns.countplot(x=column, data=df)
    plt.title(f"Count of {column}")
    plt.xticks(rotation=45)
    plt.show()
