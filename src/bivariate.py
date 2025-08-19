import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_scatter(df: pd.DataFrame, col1: str, col2: str):
    """
    Scatter plot between two numeric variables.
    """
    plt.figure(figsize=(7,5))
    sns.scatterplot(x=df[col1], y=df[col2])
    plt.title(f"{col1} vs {col2}")
    plt.show()

def plot_box(df: pd.DataFrame, cat_col: str, num_col: str):
    """
    Boxplot of a numeric variable grouped by a categorical variable.
    """
    plt.figure(figsize=(8,5))
    sns.boxplot(x=cat_col, y=num_col, data=df)
    plt.title(f"{num_col} by {cat_col}")
    plt.xticks(rotation=45)
    plt.show()
