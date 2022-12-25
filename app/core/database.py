from pymongo import MongoClient
from .configs import configs_dict

# Connect to database
db = MongoClient(
    host=configs_dict['mongodb']['HOST'],
    port=configs_dict['mongodb']['PORT']
)[configs_dict['mongodb']['DB']]

# collections
price_collection = db['historical_price']
