import pandas as pd
from kline_timestamp import KlineTimestamp
from typing import List, Dict, Union, Tuple
from pathlib import Path


class Trade:
    REQUIRED_KEYS = {'id', 'price', 'qty', 'quoteQty', 'time', 'isBuyerMaker', 'isBestMatch'}
    INTERVALS = {'1m', '3m', '5m', '15m', '30m', '1h', '2h', '4h', '6h', '8h', '12h', '1d', '3d', '1w'}

    def __init__(self,
                 api_data: List[Dict],
                 interval: str = None,
                 symbol: str = "",
                 tzinfo: str = 'UTC'):
        """
        Initialize a Trade instance with data from Binance API.

        :param api_data: List of dictionaries containing API data.
        :param interval: Interval for KlineTimestamp (e.g., '1m', '5m', '1h'). Default is None.
        :param tzinfo: Timezone for KlineTimestamp (e.g., 'UTC', 'Europe/Madrid'). Default is 'UTC'.
        :param symbol: Symbol the data refers to (e.g., 'BTCUSDT'). Default is empty string.
        :raises ValueError: If data structure is invalid or the interval is invalid.
        """
        self._validate_api_data(api_data)
        if interval is not None and interval not in self.INTERVALS:
            raise ValueError(f"Invalid interval '{interval}'. Must be one of: {self.INTERVALS}")
        self.interval = interval
        self.symbol = symbol
        self.timezone = tzinfo
        self.data = self._create_dataframe(api_data=api_data,
                                           interval=interval,
                                           symbol=symbol,
                                           tzinfo=tzinfo)

    @classmethod
    def from_api_data(cls, api_data: List[Dict], interval: str, symbol: str = "", tzinfo: str = 'UTC') -> 'Trade':
        """
        Create a Trade instance from API data.

        :param api_data: List of dictionaries containing API data.
        :param interval: Interval for KlineTimestamp.
        :param symbol: Symbol the data refers to (e.g., 'BTCUSDT'). Default is empty string.
        :param tzinfo: Timezone for KlineTimestamp. Default is 'UTC'.
        :return: Instance of Trade.
        """
        return cls(api_data=api_data, interval=interval, symbol=symbol, tzinfo=tzinfo)

    @classmethod
    def _validate_api_data(cls, api_data: List[Dict]) -> None:
        """
        Validate the structure of the API data.

        :param api_data: List of dictionaries containing API data.
        :raises ValueError: If the data does not have the expected structure.
        """
        if not isinstance(api_data, list):
            raise ValueError("api_data must be a list of dictionaries.")

        for i, entry in enumerate(api_data):
            if not isinstance(entry, dict):
                raise ValueError(f"Entry {i} is not a dictionary.")
            missing_keys = cls.REQUIRED_KEYS - entry.keys()
            if missing_keys:
                raise ValueError(f"Entry {i} is missing keys: {missing_keys}")

    @classmethod
    def _create_dataframe(cls,
                          api_data: List[Dict],
                          interval: Union[str, None],
                          symbol: str,
                          tzinfo: str) -> pd.DataFrame:
        """
        Create a pandas DataFrame from API data.

        :param api_data: List of dictionaries containing API data.
        :param interval: Interval for KlineTimestamp.
        :param symbol: Symbol the data refers to (e.g., 'BTCUSDT').
        :param tzinfo: Timezone for KlineTimestamp.
        :return: DataFrame containing the trade data.
        """
        df = pd.DataFrame(api_data)

        # Ensure correct data types
        df = df.astype({
            'price': float,
            'qty': float,
            'quoteQty': float,
            'time': int,
            'id': int,
            'isBuyerMaker': bool,
            'isBestMatch': bool
        })
        # Sort by 'id' to guarantee order before setting it as index
        df.sort_values(by='id', inplace=True)

        # Add KlineTimestamp column
        df['timestamp'] = df['time'].apply(lambda ts: KlineTimestamp(ts, interval=interval, tzinfo=tzinfo))
        df.drop(columns=['time'], inplace=True)

        # Set 'id' as index, but keep it as a column for later use
        df.set_index('id', inplace=True, drop=False)
        df.index.name = f"{symbol} {tzinfo}" if symbol else "id"

        # Reorder columns and drop duplicates
        df = df[['timestamp', 'price', 'qty', 'quoteQty', 'isBuyerMaker', 'isBestMatch', 'id']]
        df.drop_duplicates(inplace=True)
        return df

    def to_csv(self, file_path: Union[str, Path] = None) -> None:
        """
        Export trade data to a CSV file.

        :param file_path: Path to save the CSV file. If not provided, a default name based on the symbol will be used.
        """
        # Prepare data for export by converting 'timestamp' to a serializable format
        data_to_save = self.data.copy().reset_index()
        data_to_save['timestamp'] = data_to_save['timestamp'].apply(lambda kt: kt.timestamp_ms)
        file_path = file_path or f"trades_{self.symbol.lower()}.csv"
        data_to_save.to_csv(file_path, index=False)

    @classmethod
    def from_csv(cls, file_path: Union[str, Path], interval: str = '1m', symbol: str = "", tzinfo: str = 'UTC') -> 'Trade':
        """
        Create a Trade instance from a CSV file.

        :param file_path: Path to the CSV file.
        :param interval: Interval for KlineTimestamp.
        :param symbol: Symbol the data refers to (e.g., 'BTCUSDT').
        :param tzinfo: Timezone for KlineTimestamp.
        :return: Instance of Trade.
        """
        df = pd.read_csv(file_path)

        # Ensure correct data types
        df['price'] = df['price'].astype(float)
        df['qty'] = df['qty'].astype(float)
        df['quoteQty'] = df['quoteQty'].astype(float)
        df['id'] = df['id'].astype(int)
        df['isBuyerMaker'] = df['isBuyerMaker'].astype(bool)
        df['isBestMatch'] = df['isBestMatch'].astype(bool)

        # Rebuild the 'timestamp' column as KlineTimestamp
        df['timestamp'] = df['timestamp'].apply(lambda ts: KlineTimestamp(int(ts), interval=interval, tzinfo=tzinfo))

        # Create the Trade instance
        return cls.from_dataframe(df, interval, symbol, tzinfo)

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame, interval: str, symbol: str, tzinfo: str) -> 'Trade':
        """
        Create a Trade instance from a pandas DataFrame.

        :param df: DataFrame containing trade data.
        :param interval: Interval for KlineTimestamp.
        :param symbol: Symbol the data refers to (e.g., 'BTCUSDT').
        :param tzinfo: Timezone for KlineTimestamp.
        :return: Instance of Trade.
        """
        # Ensure the DataFrame has 'id' column
        if 'id' not in df.columns:
            raise ValueError("The DataFrame must contain an 'id' column.")

        df.set_index('id', inplace=True)
        df.index.name = f"{symbol} {tzinfo}" if symbol else "id"

        # Reorder columns and drop duplicates
        df = df[['timestamp', 'price', 'qty', 'quoteQty', 'isBuyerMaker', 'isBestMatch']]
        df.drop_duplicates(inplace=True)
        df.sort_index(inplace=True)

        # Create the Trade instance
        instance = cls.__new__(cls)
        instance.data = df
        instance.interval = interval
        instance.symbol = symbol
        instance.timezone = tzinfo
        return instance

    def check_id_continuity(self) -> Union[bool, List[int]]:
        """
        Check if the 'id' index is continuous and return missing IDs if any.

        :return: True if the index is continuous. If not, returns a list of missing IDs.
        """
        ids = self.data.index
        if len(ids) == 0:
            return True

        expected_ids = set(range(ids.min(), ids.max() + 1))
        actual_ids = set(ids)

        missing_ids = sorted(expected_ids - actual_ids)

        # Log the range of IDs and any missing ones
        print(f"ID range: {ids.min()} to {ids.max()}")
        print(f"Missing IDs: {missing_ids}")

        if not missing_ids:
            return True
        else:
            return missing_ids

    def get_missing_ids(self) -> List[int]:
        """
        Get the missing IDs from the DataFrame index.

        :return: A list of missing IDs, or an empty list if there are none.
        """
        ids = self.data.index
        expected_ids = set(range(ids.min(), ids.max() + 1))
        actual_ids = set(ids)
        missing_ids = sorted(expected_ids - actual_ids)
        return missing_ids

    def get_first_and_last_timestamp(self) -> Union[None, Tuple[KlineTimestamp, KlineTimestamp]]:
        """
        Get the first and last timestamp in the DataFrame.

        :return: A tuple containing the first and last KlineTimestamp, or None if the DataFrame is empty.
        """
        if self.data.empty:
            return None
        first_timestamp = self.data['timestamp'].iloc[0]
        last_timestamp = self.data['timestamp'].iloc[-1]
        return first_timestamp, last_timestamp

    def __repr__(self):
        """
        Representation of the Trade instance for printing and debugging.
        Returns the first few rows of the DataFrame for a quick view.
        """
        return f"Trade(symbol={self.symbol}, interval={self.interval}, data=\n{self.data.head()})"

    def __str__(self):
        """
        String representation of the Trade instance. This returns the entire DataFrame.
        """
        return self.data.to_string()

