import os
import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import pearsonr, t
from statsmodels.stats.multitest import multipletests
from data_pipeline.data_visualization.scripts.load_dfs import load_dfs
import click

# Helper functions for correlation analysis and plotting
def calculate_critical_r(n, alpha=0.05):
    df = n - 2
    t_critical = t.ppf(1 - alpha / 2, df)
    r_critical = np.sqrt(t_critical**2 / (t_critical**2 + df))
    return r_critical

def prepare_nested_data_for_dictionary(df):
    donor_data = {}
    for _, row in df.iterrows():
        donor = row['Observed Sample Names']
        if donor not in donor_data:
            donor_data[donor] = []
        donor_data[donor].append(row.to_dict())
    
    return donor_data

def calculate_caqtl_correlations_per_donor(donor_data):
    caqtl_r_values = []
    caqtl_p_values = []

    num_caqtls = len(next(iter(donor_data.values())))  # Get the number of caQTLs

    for caqtl_index in range(num_caqtls):
        observed_values = []
        predicted_values = []
        for donor, data_points in donor_data.items():
            try:
                data_point = data_points[caqtl_index]
                observed_value = data_point['Observed TN5']
                predicted_value = data_point['Predicted TN5']

                if not np.isnan(observed_value) and not np.isnan(predicted_value):
                    observed_values.append(observed_value)
                    predicted_values.append(predicted_value)
            except IndexError:
                continue

        if len(observed_values) > 1 and len(predicted_values) > 1:
            r, p = pearsonr(observed_values, predicted_values)
            caqtl_r_values.append(r)
            caqtl_p_values.append(p)
        else:
            caqtl_r_values.append(np.nan)
            caqtl_p_values.append(np.nan)

    valid_indices = [i for i, (r, p) in enumerate(zip(caqtl_r_values, caqtl_p_values)) if not np.isnan(r) and not np.isnan(p)]
    caqtl_r_values = [caqtl_r_values[i] for i in valid_indices]
    caqtl_p_values = [caqtl_p_values[i] for i in valid_indices]

    return caqtl_r_values, caqtl_p_values

# Plotting functions
def create_caQTL_plots(dfs, model_name, base_output_dir="output/plot_results", significance_threshold=0.05):
    output_dir = base_output_dir


    fig, axs = plt.subplots(2, 2, figsize=(16, 16))
    axs = axs.flatten()

    all_p_values = []

    for i, (key, df) in enumerate(dfs.items()):
        ax = axs[i]
        modeling_data = key.split('_')[0]

        # Filter the DataFrame for caQTL regions
        caqtl_index = df['caQTL Indices'] == True
        caqtl_df = df.loc[caqtl_index]
        
        # Prepare nested data for dictionary
        donor_data = prepare_nested_data_for_dictionary(caqtl_df)

        # Calculate r-values and p-values based on the specified correlation type
        r_values, p_values = calculate_caqtl_correlations_per_donor(donor_data)
        all_p_values.extend(p_values)

        # Plot the distribution of Pearson correlation coefficients for caQTLs
        ax.hist(r_values, bins=20, range=(-1.0, 1.0), color='#3182bd', edgecolor='black', alpha=0.5, label='caQTL r-values')

        # Calculate critical r-values for the significance threshold
        critical_r = calculate_critical_r(n=len(donor_data), alpha=significance_threshold)
        
        # Plot the red line for significant p-values
        ax.axvline(-critical_r, color='red', linestyle='--', linewidth=2, label=f'Significant p-value (±{critical_r:.3f})')
        ax.axvline(critical_r, color='red', linestyle='--', linewidth=2)

        ax.set_title(f"{modeling_data} - Pearson Correlation Coefficients", fontsize=16, fontweight='bold')
        ax.set_xlabel('Pearson Correlation Coefficient (r)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Number of caQTLs', fontsize=14, fontweight='bold')
        ax.grid(alpha=0.2)
        ax.legend()

        median_caqtl_r = np.median(r_values)
        percent_caqtl_positive = np.mean(np.array(r_values) > 0) * 100
        percent_significant_p = np.mean(np.array(p_values) < significance_threshold) * 100

        ax.annotate(f'caQTL - Median r: {median_caqtl_r:.2f}\ncaQTL - %>0: {percent_caqtl_positive:.1f}%\ncaQTL - %p<{significance_threshold}: {percent_significant_p:.1f}%',
                    xy=(0.05, 0.95), xycoords='axes fraction', verticalalignment='top', fontsize=10, fontweight='bold',
                    bbox=dict(boxstyle="square,pad=0.3", fc="white", ec="black", lw=2))

    fig.suptitle(f'{model_name} - caQTL Analysis', fontsize=20, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    os.makedirs(output_dir, exist_ok=True)
    filename_pdf = os.path.join(output_dir, 'caQTL_analysis.pdf')
    filename_png = os.path.join(output_dir, '_caQTL_analysis.png')
    plt.savefig(filename_pdf, dpi=300, bbox_inches='tight')
    plt.savefig(filename_png, dpi=300, bbox_inches='tight')
    
    plt.show()

    # Echo the file paths
    click.echo(f"Plots have been generated for caQTL:")
    click.echo(f"PDF: {filename_pdf}")
    click.echo(f"PNG: {filename_png}")

    return all_p_values

def plot_correlation_vs_pvalue(dfs, model_name,loss_type, alpha=0.05, output_dir="output/plot_results"):
    output_dir = output_dir
    
    fig, axs = plt.subplots(2, 2, figsize=(20, 18))
    axs = axs.flatten()

    for idx, (key, df) in enumerate(dfs.items()):
        ax = axs[idx]
        modeling_data = key.split('_')[0]

        caqtl_index = df['caQTL Indices'] == True
        caqtl_df = df.loc[caqtl_index]

        donor_data = prepare_nested_data_for_dictionary(caqtl_df)
        r_values, p_values = calculate_caqtl_correlations_per_donor(donor_data)

        r_values = np.array(r_values)
        p_values = np.array(p_values)

        valid_indices = ~np.isnan(r_values) & ~np.isnan(p_values)
        r_values = r_values[valid_indices]
        p_values = p_values[valid_indices]

        rejected, pvals_corrected, _, _ = multipletests(p_values, alpha=alpha, method='fdr_bh')

        significant_pos = np.sum((r_values > 0) & rejected)
        significant_neg = np.sum((r_values < 0) & rejected)

        total_rejected = np.sum(rejected)
        percent_significant_pos = (significant_pos / total_rejected) * 100 if total_rejected > 0 else 0
        percent_significant_neg = (significant_neg / total_rejected) * 100 if total_rejected > 0 else 0

        ax.hist(r_values, bins=20, range=(-1.0, 1.0), color='#3182bd', edgecolor='black', alpha=0.5)

        critical_r = calculate_critical_r(n=len(donor_data), alpha=alpha)
        ax.axvline(-critical_r, color='red', linestyle='--', linewidth=2)
        ax.axvline(critical_r, color='red', linestyle='--', linewidth=2)

        ax.set_xlabel('Pearson Correlation Coefficient (r)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Number of caQTLs', fontsize=14, fontweight='bold')
        ax.set_title(f'{modeling_data} - caQTL Analysis', fontsize=16, fontweight='bold')
        ax.grid(alpha=0.2)

        # Add boxed annotations for significant positive and negative counts with percentages
        ax.annotate(f'{significant_pos} sig pos\n({percent_significant_pos:.1f}%)', xy=(0.75, 0.9), xycoords='axes fraction',
                    fontsize=12, color='green', ha='center', va='center',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="green", lw=2))
        ax.annotate(f'{significant_neg} sig neg\n({percent_significant_neg:.1f}%)', xy                    =(0.75, 0.8), xycoords='axes fraction',
                    fontsize=12, color='purple', ha='center', va='center',
                    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="purple", lw=2))

    fig.suptitle(f'{model_name} - caQTL Analysis', fontsize=20, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    os.makedirs(output_dir, exist_ok=True)
    filename_pdf = os.path.join(output_dir,'correlation_vs_pvalue.pdf')
    filename_png = os.path.join(output_dir,'correlation_vs_pvalue.png')
    plt.savefig(filename_pdf, dpi=300, bbox_inches='tight')
    plt.savefig(filename_png, dpi=300, bbox_inches='tight')
    
    plt.show()

    # Echo the file paths
    click.echo(f"Plots have been generated for correlation vs p-value:")
    click.echo(f"PDF: {filename_pdf}")
    click.echo(f"PNG: {filename_png}")

def analyze_p_values_with_bh(all_p_values, alpha=0.05, output_dir="output/plot_results", model_name="model"):
    p_values = np.array(all_p_values)
    p_values = p_values[~np.isnan(p_values)]  # Remove NaN values

    # Apply Benjamini-Hochberg correction
    rejected, pvals_corrected, _, _ = multipletests(p_values, alpha=alpha, method='fdr_bh')

    # Plot p-value distribution with BH threshold
    plt.figure(figsize=(10, 6))
    plt.hist(p_values, bins=50, color='skyblue', edgecolor='black')
    plt.axvline(alpha, color='red', linestyle='--', linewidth=2, label=f'p-value threshold (α={alpha})')
    plt.xlabel('p-value')
    plt.ylabel('Frequency')
    plt.title('Distribution of p-values')
    plt.legend()

    os.makedirs(output_dir, exist_ok=True)
    filename_pdf = os.path.join(output_dir, 'p_value_distribution.pdf')
    filename_png = os.path.join(output_dir, 'p_value_distribution.png')
    plt.savefig(filename_pdf, dpi=300, bbox_inches='tight')
    plt.savefig(filename_png, dpi=300, bbox_inches='tight')
    
    plt.show()

    # Echo the file paths
    click.echo(f"Plots have been generated for p-value distribution:")
    click.echo(f"PDF: {filename_pdf}")
    click.echo(f"PNG: {filename_png}")

    percent_significant_bh = (np.sum(rejected) / len(p_values)) * 100
    click.echo(f"Percentage of significant p-values after Benjamini-Hochberg correction: {percent_significant_bh:.1f}%")

def plot_volcano_plot(dfs, model_name,loss_type, alpha=0.05, output_dir="output/plot_results"):
    output_dir = output_dir

    fig, axs = plt.subplots(2, 2, figsize=(20, 18))
    axs = axs.flatten()

    for idx, (key, df) in enumerate(dfs.items()):
        ax = axs[idx]
        modeling_data = key.split('_')[0]

        caqtl_index = df['caQTL Indices'] == True
        caqtl_df = df.loc[caqtl_index]

        donor_data = prepare_nested_data_for_dictionary(caqtl_df)
        r_values, p_values = calculate_caqtl_correlations_per_donor(donor_data)

        r_values = np.array(r_values)
        p_values = np.array(p_values)

        valid_indices = ~np.isnan(r_values) & ~np.isnan(p_values)
        r_values = r_values[valid_indices]
        p_values = p_values[valid_indices]

        # Apply Benjamini-Hochberg correction
        rejected, pvals_corrected, _, _ = multipletests(p_values, alpha=alpha, method='fdr_bh')

        significant_pos = np.sum((r_values > 0) & rejected)
        significant_neg = np.sum((r_values < 0) & rejected)

        total_rejected = np.sum(rejected)
        percent_significant_pos = (significant_pos / total_rejected) * 100 if total_rejected > 0 else 0
        percent_significant_neg = (significant_neg / total_rejected) * 100 if total_rejected > 0 else 0

        # Plot the scatter plot
        scatter = ax.scatter(-np.log10(p_values), r_values, c=-np.log10(p_values), cmap='plasma', alpha=0.7)
        cbar = plt.colorbar(scatter, ax=ax)
        cbar.set_label('TN5 Fragment Count', rotation=270, labelpad=15)

        # Plot the BH threshold line
        bh_threshold = -np.log10(alpha)
        ax.axvline(x=bh_threshold, color='red', linestyle='--', linewidth=2, label=f'FDR BH = {alpha}')

        # Plot the dashed line in the middle
        ax.axhline(y=0, color='gray', linestyle='--', linewidth=1)

        # Add annotations for significant positive and negative counts with percentages
        ax.annotate(f'{significant_pos} sig pos\n({percent_significant_pos:.1f}%)', xy=(5, 0.3),
                    fontsize=12, color='green', ha='center', va='center')
        ax.annotate(f'{significant_neg} sig neg\n({percent_significant_neg:.1f}%)', xy=(5, -0.3),
                    fontsize=12, color='purple', ha='center', va='center')

        ax.set_xlabel('-Log10(p-value)', fontsize=14, fontweight='bold')
        ax.set_ylabel('Pearson R', fontsize=14, fontweight='bold')
        ax.set_title(f'{modeling_data} - caQTL Analysis', fontsize=16, fontweight='bold')
        ax.legend()

    fig.suptitle(f'{model_name} - caQTL Volcano Plot Analysis', fontsize=20, fontweight='bold')
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    os.makedirs(output_dir, exist_ok=True)
    filename_pdf = os.path.join(output_dir, 'volcano_plot_analysis.pdf')
    filename_png = os.path.join(output_dir, 'volcano_plot_analysis.png')
    plt.savefig(filename_pdf, dpi=300, bbox_inches='tight')
    plt.savefig(filename_png, dpi=300, bbox_inches='tight')
    
    plt.show()

    # Echo the file paths
    click.echo(f"Plots have been generated for volcano plot:")
    click.echo(f"PDF: {filename_pdf}")
    click.echo(f"PNG: {filename_png}")
def create_caqtl_plots(dfs, model_name,loss_type, base_output_dir="output/plot_results"):
    all_p_values = create_caQTL_plots(dfs, model_name, base_output_dir=base_output_dir)
    
    # analyze_p_values_with_bh(all_p_values, output_dir=base_output_dir, model_name=model_name)
    plot_correlation_vs_pvalue(dfs, model_name,loss_type, output_dir=base_output_dir)
    plot_volcano_plot(dfs, model_name,loss_type, output_dir=base_output_dir)
@click.command()
@click.option('--input-dir', type=click.Path(exists=True), required=True, help="Base directory containing subdirectories with CSV files.")
@click.option('--output-dir', type=click.Path(), required=True, help="Base directory to save plots.")
@click.option('--model-name', type=str, required=True, help="Model name to include in plot titles and filenames.")
@click.option('--loss-type', type=str, required=True, help="Loss type to include in the output directory.")
def main(input_dir, output_dir, model_name, loss_type):
    print(f"Creating caQTL plots: input_dir={input_dir}, output_dir={output_dir}, model_name={model_name}, loss_type={loss_type}")
    dfs = load_dfs(input_dir)
    create_caqtl_plots(dfs, model_name, base_output_dir=output_dir)

if __name__ == "__main__":
    main()