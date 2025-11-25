import pandas as pd
from src.data_loader import DataLoader
from src.data_analyzer import DataAnalyzer
from src.data_saver import DataSaver
from src.data_cleaner import DataCleaner
from src.utils.logger import get_logger

# Get logger
logger = get_logger(__name__)

def process_and_join_data(data_path, aviary_area_path, coordinates_path, bess_data_path):
    """
    This function processes the excel files and joins the different dataframes.
    """
    data_loader_excel = DataLoader(assets_path=None, data_path=data_path)
    data_loader_excel.load_excel_data()
    data_excel_raw = data_loader_excel.get_data()

    if data_excel_raw.empty:
        logger.warning("No data loaded from Excel files.")
        return pd.DataFrame()

    data_cleaner = DataCleaner(data_excel_raw)
    data_cleaner.filter_excel_data()
    data_cleaner.remove_unwanted_columns()
    data_cleaner.filter_energy_consumption()
    data_cleaner.rename_and_extract_day()
    data_cleaner.remove_xlsx_suffix()
    data_cleaner.merge_coordinates(coordinates_path)
    data_excel_processed = data_cleaner.get_data()

    aviary_loader = DataLoader(assets_path=None, data_path=None)
    aviary_area_data = aviary_loader.load_aviary_area(aviary_area_path)
    
    if not aviary_area_data.empty:
        aviary_area_data['aviario'] = aviary_area_data['aviario'].astype('int64')
        data_excel_processed = pd.merge(data_excel_processed, aviary_area_data, on='aviario', how='left')

    data_loader_bess = DataLoader(assets_path=bess_data_path, data_path=None)
    data_loader_bess.load_csv_data()
    data_bess = data_loader_bess.get_data()

    if not data_bess.empty:
        data_bess = data_bess.rename(columns={
            'Número Composto': 'lote_composto',
            'GMD': 'GMD_bess',
            'Mortalidade': 'Mortalidade_bess',
            'Conversão Alimentar': 'CA_bess',
            'Idade Matriz': 'Idade Matriz_bess',
            'Aves Alojadas': 'Aves Alojadas_bess',
            'Aves Abatidas': 'Aves Abatidas_bess',
            'Fazenda': 'Fazenda_bess',
            'Lote': 'Lote_bess',
            'IEP': 'IEP_bess'
        })
        data_excel_processed = pd.merge(data_excel_processed, data_bess, on='lote_composto', how='left')

    return data_excel_processed

def main():
    """
    This is the main function of the program.
    """
    logger.info("Starting the data processing and analysis process.")

    # Load and analyze data from the CSV file
    assets_path = 'assets/dados_lotes_filtrados_projeto_BESS.csv'
    data_loader_csv = DataLoader(assets_path=assets_path, data_path=None)
    data_loader_csv.load_csv_data()
    data_csv = data_loader_csv.get_data()

    if not data_csv.empty:
        # Analyze the data from the CSV file
        analyzer_csv = DataAnalyzer(data_csv)
        description_csv = analyzer_csv.get_description()
        correlation_csv = analyzer_csv.get_correlation()

        logger.info("Data description from CSV:")
        print(description_csv)

        logger.info("Correlation matrix from CSV:")
        print(correlation_csv)
    else:
        logger.warning("No data loaded from CSV file.")


    # Load, filter, and save data from the Excel files
    data_path = 'data/raw'
    processed_csv_path = 'data/processed/dados_processados.csv'
    processed_db_path = 'data/processed/dados_processados.db'
    aviary_area_path = 'assets/area_aviarios.md'
    coordinates_path = 'assets/coordenadas.csv'
    bess_data_path = 'assets/dados_lotes_filtrados_projeto_BESS.csv'

    final_data = process_and_join_data(data_path, aviary_area_path, coordinates_path, bess_data_path)

    if not final_data.empty:
        # Save the processed data
        data_saver = DataSaver(final_data)
        data_saver.to_csv(processed_csv_path)
        data_saver.to_sqlite(processed_db_path, table_name='dados_processados')
    else:
        logger.warning("No data loaded or left after filtering from Excel files.")

    logger.info("Data processing and analysis finished.")

if __name__ == "__main__":
    main()
