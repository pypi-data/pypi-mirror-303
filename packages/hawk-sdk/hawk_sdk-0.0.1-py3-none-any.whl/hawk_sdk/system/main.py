"""
@description: Datasource API for Hawk Global System data access and export functions.
@author: Rithwik Babu
"""
from typing import List

from google.cloud import bigquery

from hawk_sdk.common.constants import PROJECT_ID
from hawk_sdk.common.data_object import DataObject
from hawk_sdk.system.repository import SystemRepository
from hawk_sdk.system.service import SystemService


class System:
    """Datasource API for fetching System data."""

    def __init__(self, environment="production") -> None:
        """Initializes the System datasource with required configurations."""
        self.connector = bigquery.Client(project=PROJECT_ID)
        self.repository = SystemRepository(self.connector, environment=environment)
        self.service = SystemService(self.repository)

    def get_hawk_ids(self, tickers: List[str]) -> DataObject:
        """Fetch hawk_ids for the given list of tickers.

        :param tickers: A list of specific tickers to filter by.
        :return: A hawk DataObject containing the hawk ID data.
        """
        return DataObject(
            name="system_hawk_id_mappings",
            data=self.service.get_hawk_ids(tickers)
        )
