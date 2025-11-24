import pandas as pd
import sqlite3
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataSaver:
    """
    This class is responsible for saving the data.
    """

    def __init__(self, data):
        """
        This is the constructor of the DataSaver class.
        """
        self.data = data

    def to_csv(self, file_path):
        """
        This method saves the data to a csv file.
        """
        if self.data.empty:
            logger.warning("Data is empty, cannot save to csv.")
            return
        logger.info(f"Saving data to {file_path}")
        try:
            self.data.to_csv(file_path, index=False)
            logger.info(f"Data saved successfully to {file_path}")
        except Exception as e:
            logger.error(f"Error saving data to csv: {e}")

    def to_sqlite(self, db_path, table_name):
        """
        This method saves the data to a sqlite database.
        """
        if self.data.empty:
            logger.warning("Data is empty, cannot save to sqlite.")
            return
        logger.info(f"Saving data to sqlite database {db_path} in table {table_name}")
        try:
            conn = sqlite3.connect(db_path)
            self.data.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            logger.info(f"Data saved successfully to sqlite database {db_path} in table {table_name}")
        except Exception as e:
            logger.error(f"Error saving data to sqlite: {e}")
