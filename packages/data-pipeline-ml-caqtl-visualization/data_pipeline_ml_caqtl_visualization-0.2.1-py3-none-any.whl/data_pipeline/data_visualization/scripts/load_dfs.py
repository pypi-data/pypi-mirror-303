import os
import pandas as pd
import click

def load_dfs(base_path):
    """Load DataFrames from all CSV files in the given directory."""
    dfs = {}
    csv_files = [f for f in os.listdir(base_path) if f.endswith('.csv')]
    for csv_file in csv_files:
        treatment = os.path.splitext(csv_file)[0]
        df_path = os.path.join(base_path, csv_file)
        dfs[treatment] = pd.read_csv(df_path)
    return dfs

@click.command()
@click.option('--input-dir', type=click.Path(exists=True), required=True, help="Directory containing CSV files.")
def cli(input_dir):
    dfs = load_dfs(input_dir)
    # You could save dfs or pass it to another function/script here if needed.
    click.echo(f"Loaded {len(dfs)} dataframes.")

if __name__ == "__main__":
    cli()
