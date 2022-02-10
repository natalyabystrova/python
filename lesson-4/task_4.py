from requests import get
import requests.utils as utils


from utils import currency_rates
currency_rates(url='http://www.cbr.ru/scripts/XML_daily.asp', code='USD')