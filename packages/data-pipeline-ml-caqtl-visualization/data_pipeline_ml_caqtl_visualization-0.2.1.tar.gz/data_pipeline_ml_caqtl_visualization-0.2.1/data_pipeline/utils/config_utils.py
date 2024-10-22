from typing import Dict, Any
from data_pipeline.utils.constants import GENERAL_FIELDS, STAGE_FIELDS

def validate_config(config_data: Dict[str, Any]) -> None:
    required_fields = [
        GENERAL_FIELDS['DATASET_FIELD'], 
        GENERAL_FIELDS['MODEL_FIELD'], 
        GENERAL_FIELDS['TREATMENT_SUFFIXES_FIELD'], 
        GENERAL_FIELDS['LOSS_TYPE_FIELD'], 
        GENERAL_FIELDS['STAGES_FIELD']
    ]
    for field in required_fields:
        if field not in config_data:
            raise ValueError(f"Required field '{field}' is missing from the config file.")
    
    if not config_data[GENERAL_FIELDS['STAGES_FIELD']] or len(config_data[GENERAL_FIELDS['STAGES_FIELD']]) < 1:
        raise ValueError("At least one stage must be defined in the config file.")
    
    # Validate stage fields
    required_stage_fields = [
        STAGE_FIELDS['OUTPUT_PATH_FIELD'], 
        STAGE_FIELDS['H5_FILE_PATH_FIELD'], 
        STAGE_FIELDS['VAR_AWARE_OBS_PATH_FIELD'], 
        STAGE_FIELDS['VA_PREDS_PATH_FIELD'], 
        STAGE_FIELDS['CHECKPOINT_PATH_FIELD']
    ]
    for stage, stage_data in config_data[GENERAL_FIELDS['STAGES_FIELD']].items():
        for field in required_stage_fields:
            if field not in stage_data:
                raise ValueError(f"Required field '{field}' is missing from stage '{stage}' in the config file.")
            
def replace_paths(data: Any) -> Any:
    """Recursively replace '/iblm/netapp' with '/home/jovyan' in all string values."""
    if isinstance(data, dict):
        return {k: replace_paths(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [replace_paths(i) for i in data]
    elif isinstance(data, str):
        return data.replace('/iblm/netapp', '/home/jovyan')
    else:
        return data
