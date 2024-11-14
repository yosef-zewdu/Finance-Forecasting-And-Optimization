import unittest
from unittest.mock import patch
import pandas as pd
import yfinance as yf
import pytest

import sys
import os

# # Add the parent directory to the system path
sys.path.append(os.path.abspath('../scripts'))
sys.path.append(os.path.abspath('../tests'))

from data_processing import load_data


class TestLoadData(unittest.TestCase):

    @patch('yfinance.download')
    def test_load_data(self, mock_download):
        # Sample data to return when yfinance.download is called
        mock_data = {
            'Open': [100, 101, 102],
            'High': [105, 106, 107],
            'Low': [95, 96, 97],
            'Close': [104, 105, 106],
            'Adj Close': [104, 105, 106],
            'Volume': [1000, 1100, 1200]
        }
        # Create a DataFrame from the sample data
        mock_download.return_value = pd.DataFrame(mock_data, index=pd.date_range(start='2015-01-01', periods=3))

        # Call the function with a sample ticker
        ticker = 'AAPL'
        df = load_data(ticker)

        # Assertions
        mock_download.assert_called_once_with(ticker, start='2015-01-01', end='2024-10-31')
        self.assertEqual(len(df), 3)  # Check if we got 3 rows
        self.assertTrue('Open' in df.columns)  # Check if 'Open' column is present
        self.assertTrue('Close' in df.columns)  # Check if 'Close' column is present

if __name__ == '__main__':
    unittest.main()