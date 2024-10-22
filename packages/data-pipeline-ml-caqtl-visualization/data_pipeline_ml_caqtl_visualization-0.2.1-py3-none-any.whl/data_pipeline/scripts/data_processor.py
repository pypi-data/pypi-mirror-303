import numpy as np
import h5py
import polars as pl
from typing import Optional, List, Dict
import logging
from .file_handler import FileHandler
import click

class DataProcessor:
    """
    A class for processing genetic data stored in HDF5 files and NumPy arrays.
    """

    # Class-level constants for caQTL index types
    LEAD_SNP = 'lead-snp'
    PEAK_REGION = 'peak-region'

    def __init__(self, h5_file_path: str, output_path: Optional[str] = None, use_caQTL: bool = False,
                 modeling_data: Optional[str] = None, asoc_pseudocount: float = 0.75):
        """
        Initialize the DataProcessor with the given file paths and configuration.

        Args:
            h5_file_path (str): Path to the HDF5 file.
            output_path (Optional[str]): Path to save the processed output.
            use_caQTL (bool): Whether to use caQTL indices in processing.
            modeling_data (Optional[str]): Optional modeling data path.
            asoc_pseudocount (float): Pseudocount used in ASOC calculations.
        """
        self.h5_file_path = h5_file_path
        self.output_path = output_path
        self.use_caQTL = use_caQTL
        self.asoc_pseudocount = asoc_pseudocount
        self.caQTL_indices = None
        self.modeling_data = modeling_data
        logging.basicConfig(level=logging.INFO)  # Configuring basic logging

    def load_and_check_data(self, h5_file, sample: str, data_type: str) -> Optional[np.ndarray]:
        """
        Load data from HDF5 and check if it's present.

        Args:
            h5_file: The opened HDF5 file.
            sample (str): The sample identifier.
            data_type (str): The type of data to load (e.g., 'TN5', 'caQTL', 'ASOC').

        Returns:
            Optional[np.ndarray]: Loaded data or None if not found.
        """
        data = FileHandler.load_data(h5_file, sample, data_type)
        if data is not None:
            return data
        else:
            logging.warning(f"No data found for {data_type} in sample {sample}")
            return None

    def load_numpy_array(self, file_path: str) -> Optional[np.ndarray]:
        """
        Load a NumPy array from a .npy file.

        Args:
            file_path (str): Path to the .npy file.

        Returns:
            Optional[np.ndarray]: Loaded NumPy array or None if the file is not found.
        """
        try:
            data = np.load(file_path, allow_pickle=True)
            return data
        except FileNotFoundError:
            logging.warning(f"File not found: {file_path}")
            return None

    def load_additional_data(self, var_aware_obs_path: str, va_preds_path: str) -> None:
        """
        Load additional observed and predicted data from NumPy files.

        Args:
            var_aware_obs_path (str): Path to the variant-aware observed data file.
            va_preds_path (str): Path to the variant-aware predictions file.
        """
        try:
            self.var_obs = self.load_numpy_array(var_aware_obs_path)
            self.va_preds = self.load_numpy_array(va_preds_path)
            
            if self.var_obs is not None:
                logging.info(f"var_obs data type: {type(self.var_obs)}, content keys: {list(self.var_obs.keys()) if isinstance(self.var_obs, dict) else 'N/A'}")
            if self.va_preds is not None:
                logging.info(f"va_preds data type: {type(self.va_preds)}, content keys: {list(self.va_preds.keys()) if isinstance(self.va_preds, dict) else 'N/A'}")

        except Exception as e:
            logging.error(f"Error loading additional data: {str(e)}")

    def extract_data(self, data: np.ndarray) -> Optional[dict]:
        """
        Extract data from a NumPy array, handling various possible structures.

        Args:
            data (np.ndarray): The NumPy array to extract data from.

        Returns:
            Optional[dict]: Extracted data as a dictionary or the original array if extraction fails.
        """
        if isinstance(data, np.ndarray):
            extracted_data = data.item()
            if isinstance(extracted_data, (dict, tuple)):
                return extracted_data
        return data

    def calculate_log2_fold_change(self, x: np.ndarray, y: np.ndarray, pseudo_count: float) -> np.ndarray:
        """
        Calculate the log2 fold change between two arrays with a pseudocount to avoid division by zero.

        Args:
            x (np.ndarray): The numerator array.
            y (np.ndarray): The denominator array.
            pseudo_count (float): The pseudocount to avoid division by zero.

        Returns:
            np.ndarray: The log2 fold change values.
        """
        x = np.where(x <= 0, pseudo_count, x)
        y = np.where(y <= 0, pseudo_count, y)
        fold_change = x / y
        return np.log2(fold_change)

    def process_data(self, caqtl_index_type: Optional[str] = None) -> None:
        """
        Process the data by loading the required datasets, calculating ASOC, and handling caQTL indices.

        Args:
            caqtl_index_type (Optional[str]): Type of caQTL index to process ('lead-snp' or 'peak-region').
        """
        obs_data_dict = {
            'sample_names': [],
            'peak_idxs': [],
            'chromosomes': [],
            'obs_hap_1': [],
            'obs_hap_2': [],
            'obs_tn5': [],
            'obs_allelic_imbalance': [],
            'fdr_pval': [],
            'caqtl_indices': []
        }
        with h5py.File(self.h5_file_path, 'r') as h5_file:
            for sample in h5_file.keys():
                sample_group = h5_file[sample]
                # Load caQTL data for the sample if needed
                caqtl_indices_sample = None
                if self.use_caQTL:
                    caqtl_data = self.load_and_check_data(h5_file, sample, 'caQTL')
                    if caqtl_data is not None:
                        logging.debug(f"caQTL data for {sample}: shape {caqtl_data.shape}, unique values: {np.unique(caqtl_data)}")
                        try:
                            index_key = 0 if caqtl_index_type == DataProcessor.LEAD_SNP else 1
                            caqtl_indices_sample = caqtl_data[:, index_key].astype(bool)
                        except IndexError:
                            logging.warning(f"Index error when processing caQTL data for {sample}. Expected index {index_key} not found.")
                    else:
                        logging.warning(f"No caQTL data found for sample {sample}.")

                for chrom in sample_group.keys():
                    chrom_group = sample_group[chrom]

                    # Load TN5 data
                    try:
                        tn5_data = chrom_group['TN5'][:]
                    except KeyError:
                        logging.warning(f"TN5 data not found for sample {sample}, chromosome {chrom}.")
                        continue  # Skip this sample and chromosome

                    num_peaks = len(tn5_data)
                    if num_peaks == 0:
                        logging.warning(f"No TN5 data for sample {sample}, chromosome {chrom}.")
                        continue  # Skip if no TN5 data

                    # Load ASOC data if available
                    if 'ASOC' in chrom_group:
                        asoc_data = chrom_group['ASOC'][:]

                        # Handle singleton dimensions
                        if asoc_data.ndim == 3 and asoc_data.shape[1] == 1:
                            asoc_data = np.squeeze(asoc_data, axis=1)
                        elif asoc_data.ndim > 2:
                            logging.warning(f"ASOC data has unexpected shape {asoc_data.shape} for sample {sample}, chromosome {chrom}.")
                            continue  # Skip this sample and chromosome

                        if asoc_data.size == 0:
                            logging.warning(f"ASOC data is empty for sample {sample}, chromosome {chrom}.")
                            continue  # Skip this sample and chromosome
                        elif asoc_data.ndim != 2 or asoc_data.shape[1] < 3:
                            logging.warning(f"ASOC data has unexpected shape {asoc_data.shape} after squeezing for sample {sample}, chromosome {chrom}.")
                            continue  # Skip this sample and chromosome
                        else:
                            # Ensure TN5 data and ASOC data lengths match
                            if len(asoc_data) != num_peaks:
                                logging.warning(f"Mismatch in TN5 and ASOC data lengths for sample {sample}, chromosome {chrom}.")
                                continue  # Skip this sample and chromosome

                            hap1 = asoc_data[:, 0]
                            hap2 = asoc_data[:, 1]
                            fdr_pval_data = asoc_data[:, 2]
                            obs_asoc = self.calculate_log2_fold_change(hap1, hap2, self.asoc_pseudocount)

                            # Prepare identifiers
                            peak_indices = np.arange(num_peaks)
                            sample_names = np.array([sample] * num_peaks)
                            chromosomes = np.array([chrom] * num_peaks)

                            # Append data to obs_data_dict
                            obs_data_dict['sample_names'].append(sample_names)
                            obs_data_dict['peak_idxs'].append(peak_indices)
                            obs_data_dict['chromosomes'].append(chromosomes)
                            obs_data_dict['obs_tn5'].append(tn5_data)
                            obs_data_dict['obs_hap_1'].append(hap1)
                            obs_data_dict['obs_hap_2'].append(hap2)
                            obs_data_dict['obs_allelic_imbalance'].append(obs_asoc)
                            obs_data_dict['fdr_pval'].append(fdr_pval_data)

                            # Append caQTL indices if available
                            if caqtl_indices_sample is not None:
                                # Assuming caQTL indices per sample per peak
                                if len(caqtl_indices_sample) == num_peaks:
                                    obs_data_dict['caqtl_indices'].append(caqtl_indices_sample)
                                else:
                                    logging.warning(f"Mismatch in caQTL indices and data lengths for sample {sample}, chromosome {chrom}.")
                                    obs_data_dict['caqtl_indices'].append(np.array([False] * num_peaks))
                            else:
                                obs_data_dict['caqtl_indices'].append(np.array([False] * num_peaks))
                    else:
                        logging.warning(f"ASOC data not found for sample {sample}, chromosome {chrom}.")
                        continue  # Skip this sample and chromosome

        # Concatenate all arrays in observation dictionary
        for key in obs_data_dict:
            if obs_data_dict[key]:  # Check if the list is not empty
                obs_data_dict[key] = np.concatenate(obs_data_dict[key], axis=0)
            else:
                obs_data_dict[key] = np.array([])  # Assign an empty array if no data

        # Check if caQTL indices should be used
        if self.use_caQTL and 'caqtl_indices' in obs_data_dict and obs_data_dict['caqtl_indices'].size > 0:
            self.caQTL_indices = obs_data_dict['caqtl_indices']
            logging.info(f"caQTL indices shape: {self.caQTL_indices.shape}, values: {self.caQTL_indices[:10]}")
        else:
            self.caQTL_indices = None

        # Save processed data
        np.save(self.output_path, obs_data_dict)
        logging.info('Observed data and caQTL indices saved.')


    
    def process_and_check_data(self, stage_name: str, create_df: bool = True, df_path: Optional[str] = None) -> pl.DataFrame:
        """
        Process observed and predicted data, checking for consistency, and optionally save the results to CSV.

        Args:
            stage_name (str): The name of the current processing stage.
            create_df (bool): Whether to create and save a DataFrame.
            df_path (Optional[str]): The directory path to save the DataFrame.

        Returns:
            pl.DataFrame: The processed data as a Polars DataFrame.
        """
        va_preds_dict = self.extract_data(self.va_preds)
        var_obs_dict = self.extract_data(self.var_obs)

        if va_preds_dict is None or var_obs_dict is None:
            raise ValueError("Failed to extract observed or predicted data.")

        # Obs
        hap1_obs = np.squeeze(var_obs_dict['obs_hap_1'])
        hap2_obs = np.squeeze(var_obs_dict['obs_hap_2'])
        tn5_obs = np.squeeze(var_obs_dict['obs_tn5'])
        sample_names_obs = var_obs_dict['sample_names']
        fdr_pval = np.squeeze(var_obs_dict['fdr_pval'])

        # Generate indexes for filtering downstream(ASOC and caQTL)
        asoc_idx = ((hap1_obs + hap2_obs) > 2) if hap1_obs.ndim == 1 else ((hap1_obs + hap2_obs) > 2).any(axis=1)
        caqtl_indices = self.caQTL_indices if self.use_caQTL else None

        #Preds
        hap1_preds = np.squeeze(va_preds_dict['pred_hap_1'])
        hap2_preds = np.squeeze(va_preds_dict['pred_hap_2'])
        tn5_preds = np.squeeze(va_preds_dict['pred_tn5'])
        sample_names_pred = va_preds_dict['sample_names']
        peak_idxs = va_preds_dict['peak_idxs']
        chromosomes = va_preds_dict['chromosomes']


        #Calculated obs and pred allelic imbalance
        obs_allelic_imbalance = np.squeeze(var_obs_dict['obs_allelic_imbalance'])
        pred_allelic_imbalance = self.calculate_log2_fold_change(hap1_preds, hap2_preds, self.asoc_pseudocount)

        # Create the data dictionary for the DataFrame
        data_dict = {
            "Observed Sample Names": sample_names_obs,
            "Predicted Sample Names": sample_names_pred,
            "Peak Indexes": peak_idxs,
            "Chromosomes": chromosomes,
            "caQTL Indices": caqtl_indices,
            "ASOC Index": asoc_idx,
            "Observed ASOC fdr_pval": fdr_pval,
            "Observed Hap1": hap1_obs,
            "Observed Hap2": hap2_obs,
            "Observed TN5": tn5_obs,
            "Predicted Hap1": hap1_preds,
            "Predicted Hap2": hap2_preds,
            "Predicted Allelic Imbalance": pred_allelic_imbalance,
            "Observed Allelic Imbalance": obs_allelic_imbalance,
            "Predicted TN5": tn5_preds,
        }

        data_df = pl.DataFrame(data_dict)

        if create_df and df_path:
            # Save to a single file
            FileHandler.save_dataframe_to_csv(data_df, df_path, suffix=f"{stage_name}_obs_preds")  
            click.echo(f"DataFrame for stage {stage_name} saved to {df_path}/{stage_name}_obs_preds.csv")
        
        return data_df
