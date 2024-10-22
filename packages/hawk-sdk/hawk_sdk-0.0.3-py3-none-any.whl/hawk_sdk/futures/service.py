"""
@description: Service layer for processing and normalizing Futures data.
@author: Rithwik Babu
"""
from datetime import datetime, timedelta
from typing import List, Iterator

import pandas as pd

from hawk_sdk.futures.repository import FuturesRepository


class FuturesService:
    """Service class for Futures business logic."""

    def __init__(self, repository: FuturesRepository) -> None:
        """Initializes the service with a repository.

        :param repository: An instance of FuturesRepository for data access.
        """
        self.repository = repository

    def get_ohlcvo(self, start_date: str, end_date: str, interval: str, hawk_ids: List[int]) -> pd.DataFrame:
        """Fetches and normalizes data into a pandas DataFrame.

        :param start_date: The start date for the data query (YYYY-MM-DD).
        :param end_date: The end date for the data query (YYYY-MM-DD).
        :param interval: The interval for the data query (e.g., '1d', '1h', '1m').
        :param hawk_ids: A list of specific hawk_ids to filter by.
        :return: A pandas DataFrame containing the normalized data.
        """
        raw_data = self.repository.fetch_ohlcvo(start_date, end_date, interval, hawk_ids)
        return self._normalize_data(raw_data)

    def get_hgf_model_state(
            self, start_date: str, end_date: str, short_ema: int, long_ema: int
    ) -> pd.DataFrame:
        """Fetches and normalizes data into a pandas DataFrame.

        :param start_date: The start date for the data query.
        :param end_date: The end date for the data query.
        :param short_ema: The short exponential moving average period.
        :param long_ema: The long exponential moving average period.
        :return: A pandas DataFrame containing the model state data.
        """
        adjusted_start_date = (
                datetime.strptime(start_date, "%Y-%m-%d") - timedelta(days=long_ema)
        ).strftime("%Y-%m-%d")

        raw_data = self.repository.fetch_ohlcvo(
            start_date=adjusted_start_date,
            end_date=end_date,
            interval="1d",
            hawk_ids=list(range(20000, 20023))
        )

        raw_df = self._normalize_data(raw_data)

        raw_df[f'EMA_{short_ema}'] = raw_df['close'].ewm(span=short_ema, adjust=False).mean()
        raw_df[f'EMA_{long_ema}'] = raw_df['close'].ewm(span=long_ema, adjust=False).mean()

        raw_df = raw_df[raw_df['date'] >= start_date]

        return raw_df

    @staticmethod
    def _normalize_data(data: Iterator[dict]) -> pd.DataFrame:
        """Converts raw data into a normalized pandas DataFrame.

        :param data: An iterator over raw data rows.
        :return: A pandas DataFrame containing normalized data.
        """
        return pd.DataFrame([dict(row) for row in data])
