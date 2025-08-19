from src.data_preprocessing import load_data, clean_data
from src.eda_univariate import plot_distribution, plot_categorical_counts
from src.eda_bivariate import plot_scatter, plot_box
from src.visualization import correlation_heatmap
from src.utils import summary_statistics, missing_values_table

def run_analysis(file_path: str):
    # Load & clean
    df = load_data(file_path)
    df = clean_data(df)

    # Print summary
    print("Summary Statistics:")
    print(summary_statistics(df))

    print("\nMissing Values:")
    print(missing_values_table(df))

    # Example plots
    numeric_cols = df.select_dtypes(include='number').columns
    cat_cols = df.select_dtypes(include='object').columns

    if len(numeric_cols) > 0:
        plot_distribution(df, numeric_cols[0])
    if len(cat_cols) > 0:
        plot_categorical_counts(df, cat_cols[0])
    if len(numeric_cols) > 1:
        plot_scatter(df, numeric_cols[0], numeric_cols[1])
        plot_box(df, cat_cols[0], numeric_cols[0])
    correlation_heatmap(df)

if __name__ == "__main__":
    # Replace with your dataset path
    run_analysis("data/application_data.csv")
