import json
import os
import click
import logging
from typing import Dict, Any
from data_pipeline.scripts.data_processor import DataProcessor
from data_pipeline.utils.constants import GENERAL_FIELDS, STAGE_FIELDS
from pathlib import Path

@click.command()
@click.option('--config_file', default="/iblm/netapp/data4/Frazer_collab/project_repos/inference-branch/inference_pipeline/pipelines/data_pipeline/configs/experiment/ipscs/basset/config.json", help='Path to the config file to use.')
@click.option('--log_level', default='INFO', type=click.Choice(['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']), help='Set the logging level.')
def run_pipeline(config_file: str, log_level: str) -> None:
    """
    Run the data processing pipeline based on the provided configuration.

    Args:
        config_file (str): Path to the configuration file.
        log_level (str): Logging level.
    """
    # Configure logging
    logging.basicConfig(level=log_level, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Load the configuration from the provided JSON file
        logging.debug(f"Attempting to load configuration from {config_file}")
        config = load_config(config_file)
        logging.debug(f"Configuration loaded: {config}")
    except Exception as e:
        logging.error(f"Error loading configuration: {e}")
        click.echo(f"Error loading configuration: {e}")
        return

    # Ensure output directory for DataFrame CSVs is specified
    output_df_dir = config.get(GENERAL_FIELDS['OUTPUT_DF_DIR_FIELD'])
    if not output_df_dir:
        logging.error(f"Error: '{GENERAL_FIELDS['OUTPUT_DF_DIR_FIELD']}' not specified in the configuration file.")
        click.echo(f"Error: '{GENERAL_FIELDS['OUTPUT_DF_DIR_FIELD']}' not specified in the configuration file.")
        return

    # Loop through each stage defined in the configuration file
    stages = config.get(GENERAL_FIELDS['STAGES_FIELD'], {})
    for stage_name, stage_data in stages.items():
        logging.info(f"Processing stage: {stage_name}")
        click.echo(f"Processing stage: {stage_name}")

        try:
            stage_fields = [
                STAGE_FIELDS['OUTPUT_PATH_FIELD'], 
                STAGE_FIELDS['H5_FILE_PATH_FIELD'], 
                STAGE_FIELDS['VAR_AWARE_OBS_PATH_FIELD'], 
                STAGE_FIELDS['VA_PREDS_PATH_FIELD']
            ]
            stage_data_values = [stage_data.get(field) for field in stage_fields]
            output_path, h5_file_path, var_aware_obs_path, va_preds_path = stage_data_values

            # Check if all required fields are available
            if not all(stage_data_values):
                logging.warning(f"Warning: Missing file paths in stage '{stage_name}' configuration. Skipping this stage.")
                click.echo(f"Error: Missing file paths in stage '{stage_name}' configuration.")
                continue

            # Construct the output directory path for DataFrame CSVs
            # Construct the output directory path for DataFrame CSVs
            df_path = Path(output_df_dir)

# Create an instance of DataProcessor
            processor = DataProcessor(h5_file_path, output_path, use_caQTL=config.get(GENERAL_FIELDS['USE_CAQTL_FIELD'], False))

            # Process the data
            logging.debug(f"Starting data processing for stage: {stage_name}")
            processor.process_data(caqtl_index_type=DataProcessor.PEAK_REGION)
            processor.load_additional_data(var_aware_obs_path, va_preds_path)

            # Process and save the DataFrame
            data_df = processor.process_and_check_data(stage_name=stage_name, create_df=True, df_path=df_path)

            # Log and output the success message
            logging.info(f"Stage {stage_name} completed successfully.")
            click.echo(f"Stage {stage_name} completed. DataFrame columns: {data_df.columns}")

        except Exception as e:
            logging.error(f"Error processing stage '{stage_name}': {e}")
            click.echo(f"Error processing stage '{stage_name}': {e}")

def load_config(config_file: str) -> Dict[str, Any]:
    """
    Load configuration from a JSON file.

    Args:
        config_file (str): Path to the configuration file.

    Returns:  
        Dict[str, Any]: The configuration as a dictionary.

    Raises:
        FileNotFoundError: If the config file does not exist.
        json.JSONDecodeError: If the config file contains invalid JSON.
    """
    try:
        logging.debug(f"Opening configuration file: {config_file}")
        with open(config_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"Error: Configuration file '{config_file}' not found.")
        click.echo(f"Error: Configuration file '{config_file}' not found.")
        raise  
    except json.JSONDecodeError as e:
        logging.error(f"Error: Failed to parse JSON in configuration file '{config_file}': {e}")
        click.echo(f"Error: Failed to parse JSON in configuration file '{config_file}': {e}")
        raise

# Entry point for the script when run from the command line
if __name__ == "__main__":
    run_pipeline()
