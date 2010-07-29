import urllib
import sys
from time import sleep

# ---------------------------------------------------------------------------- #

api_key = sys.stdin.readline().strip()

currencies = """
Eurozone Euro EUR
United States US Dollar USD
Japan Japanese Yen JPY
United Kingdom Pound Sterling GBP
Bulgaria Bulgarian Lev BGN
Czech Republic Czech Koruna CZK
Denmark Danish Krone DKK
Estonia Estonian Kroon EEK
Hungary Hungarian Forint HUF
Lithuania Lithuanian Litas LTL
Latvian Lats Latvia LVL
Poland Polish Zloty PLN
Romania New Romanian Leu RON
Sweden Swedish Krona SEK
Switzerland Swiss Franc CHF
Norway Norwegian Krone NOK
Croatian Croatia Kuna HRK
Russia Russian Rouble RUB
Turkey New Turkish Lira TRY
Australia Australian Dollar AUD
Brazil Brazilian Real BRL
Canada Canadian Dollar CAD
China Chinese Yuan CNY
Hong Kong Hong Kong Dollar HKD
Indonesia Indonesian rupiah IDR
Korea Korean Won KRW
Mexico Mexican Pesos MXN
Malasia Malasian Ringgit MYR
New Zealand New Zealand Dollar NZD
Philippines Philippine Peso PHP
Singapore Singapore Dollar SGD
Thailand Thai Baht THB
South Africa South African Rand ZAR
"""

def get_exchange_rate(src, dst, api_key):
    """
    how many Japanese Yen there are to the Dollar?
    http://www.exchangerate-api.com/USD/JPY?k=API_KEY
    """
    site = "http://www.exchangerate-api.com/%s/%s?k=%s"
    site = site % (src,dst,api_key)
    try:
        url = urllib.urlopen(site)
        result = url.read()
        return result.strip()
    except IOError,e:
        # print to stderr here
        return None

symbols = []
for line in currencies.split("\n"):
    elements = line.strip().split()
    if elements:
        symbols.append(elements[-1])

for a in symbols:
    for b in symbols:
        if a == b:
            continue
        rate = get_exchange_rate(a,b,api_key)
        if rate is not None:
            rate = float(rate)
            if rate != 0.0:
                print("%s, %s, %.6f" % (a,b,rate))
            else:
                continue
