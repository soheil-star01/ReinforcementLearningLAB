import yfinance as yf
import pandas as pd
from init_config import configs


def get_hourly_price(ticker_name: str,
                     market: str,
                     store: bool = True) -> pd.DataFrame:
    ticker_obj = yf.Ticker(ticker=ticker_name if market == 'stock' else ticker_name+'-USD')
    df_price = ticker_obj.history(period='2mo',
                                  interval='1h')
    if store:
        df_price.to_pickle(f"{configs['core']['PRICE_DATA_PATH']}/{ticker_name}_{market}.pkl")
    return df_price


if __name__ == '__main__':
    get_hourly_price('BTC', 'crypto')