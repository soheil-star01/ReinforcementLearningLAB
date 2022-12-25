import yfinance as yf
import pandas as pd
from app.core import configs


def get_hourly_price(ticker_name: str,
                     market: str,
                     store_as_file: bool = False) -> pd.DataFrame:
    ticker_obj = yf.Ticker(ticker=ticker_name if market == 'stock' else ticker_name+'-USD')
    df_price = ticker_obj.history(period='2mo',
                                  interval='1h')
    df_price = df_price[['Open', 'High', 'Low', 'Close', 'Volume']].reset_index()
    df_price['market'] = market
    df_price['ticker_name'] = ticker_name
    df_price['resolution'] = '1h'
    if store_as_file:
        df_price.to_pickle(f"{configs.configs_dict['core']['PRICE_DATA_PATH']}/{ticker_name}_{market}.pkl")
    return df_price


if __name__ == '__main__':
    get_hourly_price('BTC', 'crypto')
