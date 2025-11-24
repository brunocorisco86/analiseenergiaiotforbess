import pandas as pd
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataCleaner:
    """
    This class is responsible for cleaning the data.
    """

    def __init__(self, data):
        """
        This is the constructor of the DataCleaner class.
        """
        self.data = data

    def filter_excel_data(self):
        """
        This method filters the data from the excel files.
        """
        if self.data is None or self.data.empty:
            logger.warning("No data to filter.")
            return

        logger.info("Filtering excel data.")
        # Filter out rows where 'Semanas' contains 'semana' (case-insensitive)
        if 'Semanas' in self.data.columns:
            self.data = self.data[~self.data['Semanas'].astype(str).str.contains('semana', case=False, na=False)]
        else:
            logger.warning("Column 'Semanas' not found in the data. Skipping this filter.")
        
        # Filter out rows where 'Energia (kWh)' is not a valid value
        if 'Energia (kWh)' in self.data.columns:
            self.data = self.data.dropna(subset=['Energia (kWh)'])
            self.data = self.data[pd.to_numeric(self.data['Energia (kWh)'], errors='coerce').notnull()]
        else:
            logger.warning("Column 'Energia (kWh)' not found in the data. Skipping this filter.")

    def remove_unwanted_columns(self):
        """
        This method removes columns containing 'Unnamed' and 'Ref.' from the data.
        """
        if self.data is None or self.data.empty:
            logger.warning("No data to clean (remove columns).")
            return

        logger.info("Removing unwanted columns.")
        columns_to_drop = [col for col in self.data.columns if 'Unnamed' in col or 'Ref.' in col]
        if columns_to_drop:
            self.data = self.data.drop(columns=columns_to_drop)
            logger.info(f"Dropped columns: {', '.join(columns_to_drop)}")
        else:
            logger.info("No 'Unnamed' or 'Ref.' columns found to drop.")

    def filter_energy_consumption(self):
        """
        This method filters the data to keep only rows where 'Energia (kWh)' is greater than 0.
        """
        if self.data is None or self.data.empty:
            logger.warning("No data to filter energy consumption.")
            return

        logger.info("Filtering data for 'Energia (kWh)' > 0.")
        if 'Energia (kWh)' in self.data.columns:
            # Ensure 'Energia (kWh)' is numeric before filtering
            self.data['Energia (kWh)'] = pd.to_numeric(self.data['Energia (kWh)'], errors='coerce')
            self.data = self.data[self.data['Energia (kWh)'] > 0]
        else:
            logger.warning("Column 'Energia (kWh)' not found in the data. Skipping energy consumption filter.")

    def rename_and_extract_day(self):
        """
        This method renames the 'Semanas' column to 'dia_criacao' and extracts the integer value from it.
        """
        if self.data is None or self.data.empty:
            logger.warning("No data to rename and extract day.")
            return

        logger.info("Renaming 'Semanas' to 'dia_criacao' and extracting day.")
        if 'Semanas' in self.data.columns:
            self.data = self.data.rename(columns={'Semanas': 'dia_criacao'})
            # Extract the integer part of the day
            self.data['dia_criacao'] = self.data['dia_criacao'].astype(str).str.extract('(\d+)').astype(float).astype('Int64')

        else:
            logger.warning("Column 'Semanas' not found in the data. Skipping rename and extract day.")

    def remove_xlsx_suffix(self):
        """
        This method removes the '.xlsx' suffix from the 'source_file' column.
        """
        if self.data is None or self.data.empty:
            logger.warning("No data to remove .xlsx suffix.")
            return

        logger.info("Removing '.xlsx' suffix from 'source_file' column.")
        if 'source_file' in self.data.columns:
            self.data['source_file'] = self.data['source_file'].astype(str).str.replace('.xlsx', '', regex=False)
        else:
            logger.warning("Column 'source_file' not found in the data. Skipping removing .xlsx suffix.")

    def get_data(self):
        """
        This method returns the cleaned data.
        """
        return self.data
