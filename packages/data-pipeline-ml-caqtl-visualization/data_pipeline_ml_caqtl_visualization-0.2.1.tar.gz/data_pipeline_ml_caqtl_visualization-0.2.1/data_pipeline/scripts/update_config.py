from pathlib import Path
from importlib import resources
from data_pipeline.utils.constants import GENERAL_FIELDS
from data_pipeline.utils.config_utils import validate_config, replace_paths
import json
import click
from typing import Dict, Any, Union
@click.command()
@click.argument('config_file', type=click.Path(exists=True))
@click.option('--local-paths', is_flag=True, default=False, help='Use local paths (/iblm/netapp) instead of cluster paths.')
def update_config(config_file: str, local_paths: bool) -> Union[str, None]:
    config_path = Path(config_file)
    with config_path.open('r') as file:
        config_data: Dict[str, Any] = json.load(file)

    # Validate config
    validate_config(config_data)
    click.echo(f"Initial config data: {json.dumps(config_data, indent=2)}")
    click.echo(f"local_paths flag: {local_paths}")

  
    # Get the output_base_dir from the JSON using the constant
    output_base_dir = config_data.get(GENERAL_FIELDS['OUTPUT_BASE_DIR_FIELD'])
    print("OUPUT BASE DIR PRE", output_base_dir)
    # Use importlib.resources to find the package root
    # with resources.path(data_pipeline, '') as package_root:
    # Set the desired output paths dynamically based on package_root, dataset, model, and loss_type
    package_root = Path("/iblm/netapp/data4/Frazer_collab/project_repos/inference-branch/inference_pipeline/pipelines/data_pipeline")
    output_base_dir = config_data['output_dir']
    
    output_df_dir = str(Path(output_base_dir) / "dfs")
    meta_data_dir = str(Path(output_base_dir) / "meta_data")
    plot_results_dir = str(Path(output_base_dir) / "plot_results")
    print("OUPUT BASE DIR POST", output_base_dir)

    # Create the directories if they don't exist
    Path(output_base_dir).mkdir(parents=True, exist_ok=True)
    Path(output_df_dir).mkdir(parents=True, exist_ok=True)
    Path(meta_data_dir).mkdir(parents=True, exist_ok=True)
    Path(plot_results_dir).mkdir(parents=True, exist_ok=True)

    click.echo(f"Generated paths:")
    click.echo(f"  output_base_dir: {output_base_dir}")
    click.echo(f"  output_df_dir: {output_df_dir}")
    click.echo(f"  meta_data_dir: {meta_data_dir}")
    click.echo(f"  plot_results_dir: {plot_results_dir}")

    constant_fields = {
        GENERAL_FIELDS['USE_CAQTL_FIELD']: True,
        GENERAL_FIELDS['OUTPUT_DF_DIR_FIELD']: output_df_dir,
        GENERAL_FIELDS['OUTPUT_BASE_DIR_FIELD']: output_base_dir,
        GENERAL_FIELDS['META_DATA_DIR_FIELD']: meta_data_dir,
        GENERAL_FIELDS['PLOT_RESULTS_DIR_FIELD']: plot_results_dir,
        GENERAL_FIELDS['CONFIG_FILE_FIELD']: str(config_path)  # Keep the original config file path
    }

    config_data.update(constant_fields)
    print("local_paths:", local_paths)
    if not local_paths:
        config_data = replace_paths(config_data)
    else:
        click.echo("Using local paths.")

    # Write the updated config data to a new file in the same directory as the original config file
    updated_config_path = config_path.with_name(f"updated_{config_path.name}")
    with updated_config_path.open('w') as file:
        json.dump(config_data, file, indent=4)

    click.echo(f"Updated configuration saved to {updated_config_path}")
    return str(updated_config_path)


if __name__ == "__main__":
    update_config()
