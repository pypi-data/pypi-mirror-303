import click
import json
from data_pipeline.scripts.update_config import update_config
from data_pipeline.scripts.data_pipeline import run_pipeline
from data_pipeline.data_visualization.scripts.plot_tn5 import create_tn5_plot
from data_pipeline.data_visualization.scripts.plot_allelic_imbalance import create_allelic_imbalance_plot  
from data_pipeline.data_visualization.scripts.plot_caqtl import create_caqtl_plots
from pathlib import Path
from typing import Optional, Dict, Any
from data_pipeline.utils.constants import GENERAL_FIELDS, STAGE_FIELDS
from data_pipeline.utils.config_utils import replace_paths
from data_pipeline.data_visualization.scripts.load_dfs import load_dfs

class OrderedGroup(click.Group):
    def __init__(self, *args, **kwargs):
        self.order = kwargs.pop('order', None)
        super(OrderedGroup, self).__init__(*args, **kwargs)

    def list_commands(self, ctx):
        return self.order if self.order else super(OrderedGroup, self).list_commands(ctx)

    def get_help(self, ctx):
        help_text = super(OrderedGroup, self).get_help(ctx)
        for i, command in enumerate(self.list_commands(ctx), 1):
            command_info = f"{i}) {command}"
            help_text = help_text.replace(f"  {command}", f"  {command_info}")
        return help_text


@click.group(cls=OrderedGroup, order=[
    'run-data', 
    'run-vis', 
    'run-full'
])
def cli():
    """CLI tool for managing the data processing and visualization pipeline."""
    pass

@cli.command(name="run-data")
@click.option('--config-file', type=click.Path(exists=True), help="Path to the configuration file.")
@click.option('--log-level', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), default='INFO', help="Set the logging level.")
@click.option('--local-paths', is_flag=True, default=False, help='Use local paths (/iblm/netapp) instead of cluster paths.')
@click.pass_context
def run_data_command(ctx: click.Context, config_file: Optional[str], log_level: str, local_paths: bool) -> None:
    """Run the data processing pipeline."""
    
    # If config_file is not provided, use a hardcoded default config path
    if not config_file:
        config_file = str(Path(const.CONFIG_BASE_PATH) / "default_config.json")

    click.echo(f"Using configuration file: {config_file}")
    config_name = Path(config_file).name

    # Extract the config name using basic string operations
    click.echo(f"Extracted config name: {config_name}")
    
    # Invoke the update_config command using ctx.invoke, passing the local_paths flag
    updated_config_file = ctx.invoke(update_config, config_file=config_file, local_paths=local_paths)
    
    # Use the updated config file for the pipeline
    ctx.invoke(run_pipeline, config_file=updated_config_file, log_level=log_level)


@cli.command(name="run-vis")
@click.option('--config-file', type=click.Path(exists=True), required=True, help="Path to the configuration file used in the main pipeline.")
@click.option('--local-paths', is_flag=True, default=False, help='Use local paths (/iblm/netapp) instead of cluster paths.')
@click.option('--input-dir', type=click.Path(exists=True), required=True, help="Base directory containing subdirectories with CSV files.")
def run_vis_command(config_file, local_paths, input_dir):
    """Run the data visualization pipeline."""
    
    # Load and validate the configuration file
    config_path = Path(config_file)
    with config_path.open('r') as file:
        config_data: Dict[str, Any] = json.load(file)
    
    # Optionally replace paths if not using local paths
    if not local_paths:
        config_data = replace_paths(config_data)
    
    # Extract output directory, model name, and loss type from config
    output_dir = config_data[GENERAL_FIELDS['PLOT_RESULTS_DIR_FIELD']]
    model_name = config_data[GENERAL_FIELDS['MODEL_FIELD']]
    loss_type = config_data[GENERAL_FIELDS['LOSS_TYPE_FIELD']]

    print(f"Running visualization for: input_dir={input_dir}, output_dir={output_dir}, model_name={model_name}, loss_type={loss_type}")
    
    # Load DataFrames
    dfs = load_dfs(input_dir)
    
    # Create TN5 plots
    create_tn5_plot(dfs, model_name, loss_type, plot_caqtl_only=False, base_output_dir=output_dir)
    create_tn5_plot(dfs, model_name, loss_type, plot_caqtl_only=True, base_output_dir=output_dir)
    
    # Create allelic imbalance plot 
    create_allelic_imbalance_plot(dfs, model_name, loss_type, base_output_dir=output_dir, plot_caqtl_only = False)
    create_allelic_imbalance_plot(dfs, model_name, loss_type, base_output_dir=output_dir, plot_caqtl_only = True)

    # Create caQTL plots
    create_caqtl_plots(dfs, model_name, loss_type, base_output_dir=output_dir)

@cli.command(name="run-full")
@click.option('--config-file', type=click.Path(exists=True), required=True, help="Path to the configuration file used in the main pipeline.")
@click.option('--local-paths', is_flag=True, default=False, help='Use local paths (/iblm/netapp) instead of cluster paths.')
@click.option('--log-level', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), default='INFO', help="Set the logging level.")  
@click.pass_context
def run_full_command(ctx, config_file, local_paths, log_level):
    """Run the full data and visualization pipeline."""
    # Update the configuration file
    updated_config_file = ctx.invoke(update_config, config_file=config_file, local_paths=local_paths)
    
    # Run the data pipeline
    ctx.invoke(run_pipeline, config_file=updated_config_file, log_level=log_level)
    
    # Load and validate the updated configuration file
    config_path = Path(updated_config_file)
    with config_path.open('r') as file:
        config_data: Dict[str, Any] = json.load(file)
    
   
    input_dir = config_data[GENERAL_FIELDS["OUTPUT_DF_DIR_FIELD"]]
    # Run the visualization pipeline
    ctx.invoke(run_vis_command, config_file=updated_config_file, local_paths=local_paths, input_dir=input_dir)
if __name__ == "__main__":
    cli()