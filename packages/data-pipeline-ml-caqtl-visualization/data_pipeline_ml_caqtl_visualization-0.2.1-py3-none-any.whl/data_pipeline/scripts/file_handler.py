import h5py
import numpy as np
import polars as pl
import os
from typing import Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileHandler:
    """
    A utility class for handling file operations such as loading data from HDF5 and NumPy files,
    and saving data to files. This class provides static methods to perform these operations,
    making it reusable and easy to integrate into other classes or scripts.
    """
    @staticmethod
    def load_data(h5_file, sample, data_type):
        path = f"{sample}/chr2/{data_type}"
        if path in h5_file:
            return np.array(h5_file[path])
        else:
            print(f"Warning: {data_type} data not found for sample {sample}")
            return None
    @staticmethod
    def load_h5_data(file_path: str, dataset_path: str) -> Optional[np.ndarray]:
        """
        Loads a dataset from an HDF5 file.

        Parameters:
        file_path (str): The path to the HDF5 file.
        dataset_path (str): The internal path within the HDF5 file to the dataset.

        Returns:
        Optional[numpy.ndarray]: The dataset as a NumPy array, or None if the dataset is not found.

        Raises:
        IOError: If the HDF5 file cannot be opened.
        KeyError: If the dataset path is not found in the HDF5 file.
        """
        try:
            with h5py.File(file_path, 'r') as h5_file:
                if dataset_path in h5_file:
                    data = np.array(h5_file[dataset_path])
                    # logging.info(f"Loaded dataset '{dataset_path}' from HDF5 file '{file_path}', data shape: {data.shape}")
                    return data
                else:
                    logging.warning(f"Dataset path '{dataset_path}' not found in HDF5 file '{file_path}'")
                    return None
        except IOError as e:
            logging.error(f"Error opening HDF5 file '{file_path}': {e}")
            raise
        except KeyError as e:
            logging.error(f"Error accessing dataset '{dataset_path}' in HDF5 file '{file_path}': {e}")
            raise

 
    @staticmethod
    def save_numpy_file(file_path: str, data: np.ndarray) -> None:
        """
        Saves a NumPy array to a .npy file.

        Parameters:
        file_path (str): The path where the file will be saved.
        data (numpy.ndarray): The data to save.

        Raises:
        IOError: If the file cannot be written.
        """
        try:
            np.save(file_path, data)
            logging.info(f"Data saved to {file_path}")
        except IOError as e:
            logging.error(f"Error saving NumPy file '{file_path}': {e}")
            raise

    @staticmethod
    def save_dataframe_to_csv(df: pl.DataFrame, output_dir: str, suffix: str) -> None:
        """
        Saves a Polars DataFrame to a CSV file.

        Parameters:
        df (pl.DataFrame): The DataFrame to save.
        output_dir (str): The directory where the CSV file will be saved.
        suffix (str): A suffix to add to the CSV file name.

        Raises:
        IOError: If the directory cannot be created or the file cannot be written.
        """
        try:
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            output_file = os.path.join(output_dir, f"{suffix.replace(' ', '_')}.csv")
            df.write_csv(output_file)
            logging.info(f"DataFrame for {suffix} saved to {output_file}")
        except IOError as e:
            logging.error(f"Error saving CSV file '{output_file}': {e}")
            raise
