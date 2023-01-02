import yfinance as yf
import pandas as pd
from app.core import configs
from app.core.database import price_collection
from app.core.utils.DataType import Market


def retrieve_from_db(ticker_name: str,
                     market: Market,
                     last_one: bool = False) -> pd.DataFrame:
    query = price_collection.find({
        "Ticker": ticker_name,
        "Market": market.value
    }).sort("Datetime", -1)
    df_ret_data = pd.DataFrame(query)
    if df_ret_data.empty:
        return df_ret_data
    if last_one:
        return df_ret_data.iloc[-1]
    return df_ret_data


def get_hourly_price(ticker_name: str,
                     market: Market,
                     store_as_file: bool = False) -> pd.DataFrame:
    ticker_obj = yf.Ticker(ticker=(ticker_name if market == Market.STOCK
                                   else ticker_name + '-USD'))
    df_price = ticker_obj.history(period='2mo',
                                  interval='1h')
    df_price = df_price[['Open', 'High',
                         'Low', 'Close',
                         'Volume']].reset_index()
    df_price['Market'] = market.value
    df_price['Ticker'] = ticker_name
    df_price['Resolution'] = '1h'
    last_price = retrieve_from_db(ticker_name,
                                  market,
                                  last_one=True)
    if not last_price.empty:
        price_collection.insert_many(
            df_price[df_price['Datetime'] > last_price['Datetime'].tz_localize('utc')].to_dict('records')
        )
    else:
        price_collection.insert_many(df_price.to_dict('records'))
    if store_as_file:
        df_price.to_pickle(
            f"{configs.configs_dict['core']['PRICE_DATA_PATH']}/{ticker_name}_{market.value}.pkl"
        )
    return df_price


if __name__ == '__main__':
    get_hourly_price('BTC', Market.CRYPTO)
