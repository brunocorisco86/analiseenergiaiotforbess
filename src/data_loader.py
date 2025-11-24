import os
import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataLoader:
    """
    This class is responsible for loading the data from the files.
    """

    def __init__(self, assets_path, data_path):
        """
        This is the constructor of the DataLoader class.
        """
        self.assets_path = assets_path
        self.data_path = data_path
        self.data = None

    def load_csv_data(self):
        """
        This method loads the data from the csv file.
        """
        logger.info(f"Loading data from {self.assets_path}")
        try:
            # The separator is a semicolon
            self.data = pd.read_csv(self.assets_path, sep=';')
            # Replace comma with dot for decimal values
            for col in self.data.columns:
                if self.data[col].dtype == 'object':
                    self.data[col] = self.data[col].str.replace(',', '.', regex=True)
            
            # Convert numeric columns to numeric types
            for col in ['Conversão Alimentar', 'GMD', 'IEP', 'Mortalidade', 'Idade Matriz']:
                self.data[col] = pd.to_numeric(self.data[col], errors='coerce')

        except FileNotFoundError:
            logger.error(f"File not found: {self.assets_path}")
            self.data = pd.DataFrame()

    def load_excel_data(self):
        """
        This method loads the data from the excel files.
        """
        logger.info(f"Loading data from {self.data_path}")
        all_files = []
        for root, dirs, files in os.walk(self.data_path):
            for file in files:
                if file.endswith(".xlsx"):
                    file_path = os.path.join(root, file)
                    logger.info(f"Reading file: {file_path}")
                    try:
                        df = pd.read_excel(file_path)
                        df['source_file'] = file
                        all_files.append(df)
                    except Exception as e:
                        logger.error(f"Error reading file {file_path}: {e}")
        
        if all_files:
            self.data = pd.concat(all_files, ignore_index=True)
        else:
            self.data = pd.DataFrame()

    def load_aviary_area(self, file_path):
        """
        This method loads the aviary area data from a markdown file.
        """
        logger.info(f"Loading aviary area data from {file_path}")
        try:
            # Read the markdown file as a CSV, skipping the first 2 lines and using '|' as separator
            df = pd.read_csv(file_path, sep='|', skiprows=2, header=None, skipinitialspace=True)
            # Drop the first and last columns which are empty
            df = df.drop(columns=[0, 3])
            # Set the column names
            df.columns = ['aviario', 'metros_quadrados']
            # trim whitespace from data
            df['aviario'] = df['aviario'].astype(str).str.strip()
            df['metros_quadrados'] = df['metros_quadrados'].astype(str).str.strip()
            # convert columns to numeric
            df['aviario'] = pd.to_numeric(df['aviario'])
            df['metros_quadrados'] = pd.to_numeric(df['metros_quadrados'])

            return df
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return pd.DataFrame()
        except Exception as e:
            logger.error(f"Error loading aviary area data: {e}")
            return pd.DataFrame()

    def get_data(self):
        """
        This method returns the loaded data.
        """
        return self.data

