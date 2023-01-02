from app.core.trade import TradingEnv
from app.core.utils import price_data
from app.core.utils.DataType import Market

price_btc = price_data.get_hourly_price('BTC', Market.CRYPTO)

market_obj = TradingEnv.Market(price_btc)
print('s')
