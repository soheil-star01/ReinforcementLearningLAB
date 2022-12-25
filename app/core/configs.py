import yaml
from pymongo import MongoClient

configs_dict = yaml.safe_load(open('config.yml'))

db = MongoClient(host=configs_dict['mongodb']['HOST'],
                 port=configs_dict['mongodb']['PORT'])[configs_dict['mongodb']['DB']]
price_collection = db['historical_price']
