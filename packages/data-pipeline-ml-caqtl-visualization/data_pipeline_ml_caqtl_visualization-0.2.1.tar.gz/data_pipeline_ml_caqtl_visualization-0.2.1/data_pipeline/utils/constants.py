# constants.py
from pathlib import Path


# General field names
GENERAL_FIELDS = {
    'DATASET_FIELD': 'dataset',
    'MODEL_FIELD': 'model',
    'STAGES_FIELD': 'stages',
    'USE_CAQTL_FIELD': 'use_caQTL',
    'OUTPUT_DF_DIR_FIELD': 'output_df_dir',
    'OUTPUT_BASE_DIR_FIELD': 'output_base_dir',
    'CONFIG_FILE_FIELD': 'config_file',
    'TREATMENT_SUFFIXES_FIELD': 'treatment_suffixes',
    'LOSS_TYPE_FIELD': 'loss_type',
    'META_DATA_DIR_FIELD': 'meta_data_dir',
    'PLOT_RESULTS_DIR_FIELD': 'plot_results_dir',
}

# Stage-related field names
STAGE_FIELDS = {
    'OUTPUT_PATH_FIELD': 'output_path',
    'H5_FILE_PATH_FIELD': 'h5_file_path',
    'VAR_AWARE_OBS_PATH_FIELD': 'var_aware_obs_path',
    'VA_PREDS_PATH_FIELD': 'va_preds_path',
    'CHECKPOINT_PATH_FIELD': 'checkpoint_path',
}
