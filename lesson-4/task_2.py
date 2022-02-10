from requests import get
import requests.utils as utils


def currency_rates(url=None, code=None):
    response = get(url)
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    values = content.split('Valute')
    for v in values:
        if v.lower().find(code.lower()) != -1:
            start_idx = v.find('<Value>')
            end_idx = v.find('</Value>')
            return v[start_idx + 7:end_idx]
    return None


print(currency_rates(url='http://www.cbr.ru/scripts/XML_daily.asp', code='USD'))
