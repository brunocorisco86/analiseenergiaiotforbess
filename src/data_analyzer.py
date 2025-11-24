import pandas as pd
import numpy as np
from src.utils.logger import get_logger

logger = get_logger(__name__)

class DataAnalyzer:
    """
    This class is responsible for analyzing the data.
    """

    def __init__(self, data):
        """
        This is the constructor of the DataAnalyzer class.
        """
        self.data = data

    def get_description(self):
        """
        This method returns a description of the data.
        """
        if self.data.empty:
            logger.warning("Data is empty, cannot generate description.")
            return pd.DataFrame()
        logger.info("Generating data description.")
        return self.data.describe()

    def get_correlation(self):
        """
        This method returns the correlation matrix of the data.
        """
        if self.data.empty:
            logger.warning("Data is empty, cannot generate correlation matrix.")
            return pd.DataFrame()
        logger.info("Generating correlation matrix.")
        numeric_data = self.data.select_dtypes(include=[np.number])
        return numeric_data.corr()
