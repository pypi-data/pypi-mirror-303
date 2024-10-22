import os
import click
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr
from data_pipeline.data_visualization.scripts.load_dfs import load_dfs

def multi_plot(model_name, preds, obs, x_label, y_label, title, metric_type, ax, x_min=None, x_max=None, y_min=None, y_max=None):
    mask = ~(np.isnan(preds) | np.isnan(obs))
    preds = preds[mask]
    obs = obs[mask]

    if np.unique(preds).size == 1 or np.unique(obs).size == 1:
        print(f"Warning: Constant data detected for {title}. Skipping plot.")
        ax.text(0.5, 0.5, "Constant data detected\nSkipping plot", ha='center', va='center', fontsize=12)
        ax.set_axis_off()
        return

    ax.scatter(preds, obs, s=5, alpha=0.40, marker='o', edgecolor='black', facecolor='white')
    ax.grid(alpha=0.2)

    x_buffer = (preds.max() - preds.min()) * 0.05
    y_buffer = (obs.max() - obs.min()) * 0.05

    if x_min is None or x_max is None:
        x_min, x_max = preds.min() - x_buffer, preds.max() + x_buffer
    if y_min is None or y_max is None:
        y_min, y_max = obs.min() - y_buffer, obs.max() + y_buffer

    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    pearson_r, _ = pearsonr(preds, obs)

    ax.set_xlabel(x_label, fontsize=12, fontweight='bold')
    ax.set_ylabel(y_label, fontsize=12, fontweight='bold')
    ax.set_title(title, fontsize=14, fontweight='bold')

    annotation_text = f"Pearson r = {pearson_r:.2f}"
    ax.text(0.05, 0.92, annotation_text, fontsize=10, fontweight='bold', verticalalignment='top', transform=ax.transAxes, bbox=dict(boxstyle="square,pad=0.5", facecolor="#F0F0F0", edgecolor="#636363"))

    ax.axhline(y=0, color='red', linestyle='-', linewidth=1)
    ax.axvline(x=0, color='red', linestyle='-', linewidth=1)

def create_tn5_plot(dfs, model_name, loss_type, plot_caqtl_only=False, base_output_dir="output/plot_results"):
    # Use the base_output_dir as is, assuming it already includes model_name and loss_type
    output_dir = base_output_dir
    
    fig, axs = plt.subplots(2, 2, figsize=(16, 16))
    axs = axs.flatten()

    for i, (key, df) in enumerate(dfs.items()):
        ax = axs[i]
        modeling_data = key.split('_')[0]

        if plot_caqtl_only and "caQTL Indices" in df.columns:
            df = df[df["caQTL Indices"] == True]

        x = df["Predicted TN5"]
        y = df["Observed TN5"]

        xlabel = "Predicted Tn5"
        ylabel = "Observed Tn5"
        x_lim = (0, 700)
        y_lim = (0, 1600)

        multi_plot(model_name, x, y, xlabel, ylabel, f"{modeling_data} -ipscs-", "Tn5", ax, x_min=x_lim[0], x_max=x_lim[1], y_min=y_lim[0], y_max=y_lim[1])

    suptitle = f'{model_name} - TN5 Comparison'
    if plot_caqtl_only:
        suptitle += ' (caQTL Regions Only)'

    fig.suptitle(suptitle, fontsize=20, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    os.makedirs(output_dir, exist_ok=True)

    suffix = '_caqtl_only' if plot_caqtl_only else '_no_caqtl'
    filename_pdf = os.path.join(output_dir, f'tn5{suffix}.pdf')
    filename_png = os.path.join(output_dir, f'tn5{suffix}.png')

    plt.savefig(filename_pdf, dpi=300, bbox_inches='tight')
    plt.savefig(filename_png, dpi=300, bbox_inches='tight')
    plt.show()

    click.echo(f"Plots have been generated for TN5:")
    click.echo(f"PDF: {filename_pdf}")
    click.echo(f"PNG: {filename_png}")

@click.command()
@click.option('--input-dir', type=click.Path(exists=True), required=True, help="Base directory containing subdirectories with CSV files.")
@click.option('--output-dir', type=click.Path(), required=True, help="Base directory to save plots.")
@click.option('--model-name', type=str, required=True, help="Model name to include in plot titles and filenames.")
@click.option('--loss-type', type=str, required=True, help="Loss type to include in the output directory.")
def main(input_dir, output_dir, model_name, loss_type):
    print(f"Received arguments: input_dir={input_dir}, output_dir={output_dir}, model_name={model_name}, loss_type={loss_type}")
    
    dfs = load_dfs(input_dir)
    
    # Create plot without caQTL filter
    create_tn5_plot(dfs, model_name, loss_type, plot_caqtl_only=False, base_output_dir=output_dir)
    
    # Create plot with caQTL filter
    create_tn5_plot(dfs, model_name, loss_type, plot_caqtl_only=True, base_output_dir=output_dir)

    click.echo("Both plots (with and without caQTL filter) have been generated.")

if __name__ == "__main__":
    main()