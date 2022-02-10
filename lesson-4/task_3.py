import requests
from datetime import datetime


def currency_rates(url=None, code=None):
    response = requests.get(url)
    encodings = requests.utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    values = content.split('Valute')
    result = []
    date = response.headers["Date"]
    date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
    result.append(date)
    for v in values:
        if v.lower().find(code.lower()) != -1:
            start_idx = v.find('<Value>')
            end_idx = v.find('</Value>')
            result.append(v[start_idx + 7:end_idx])
            return(result)
    return None
# currency_rates(site, code='EUR')


print(currency_rates(url='http://www.cbr.ru/scripts/XML_daily.asp', code='eur'))
print(currency_rates(url='http://www.cbr.ru/scripts/XML_daily.asp', code='usd'))
