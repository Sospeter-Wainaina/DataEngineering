from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.redshift import Redshift
from pandas import DataFrame
from os import path

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data_to_redshift(df: DataFrame, **kwargs) -> None:
    """
    Template for exporting data to a Redshift cluster.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#redshift
    """
    table_name = 'ny_taxi'
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'
    chunk_size=100000

    # Split DataFrame into smaller chunks
    for i in range(0, len(df), chunk_size):
        chunk = df[i:i+chunk_size]

        # Export each chunk to Redshift
        with Redshift.with_config(ConfigFileLoader(config_path, config_profile)) as loader:
            loader.export(
                chunk,
                table_name,
                if_exists='append',  # Append data to the table
            )
