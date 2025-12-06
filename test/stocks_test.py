from pandas import DataFrame

from app.stocks import fetch_stocks_csv


def test_data_fetching():

    stocks_df = fetch_stocks_csv("GOOGL")

    assert isinstance(stocks_df, DataFrame)

    assert "timestamp" in stocks_df.columns
    assert "adjusted_close" in stocks_df.columns

    assert len(stocks_df) >= 100
