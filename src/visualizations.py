import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def correlation_heatmap(df: pd.DataFrame):
    """
    Plot a heatmap of correlations for numeric columns.
    """
    plt.figure(figsize=(10,8))
    corr = df.corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.show()
