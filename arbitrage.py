"""
http://shriphani.com/blog/2010/07/02/bellman-ford-algorithms-applications-triangular-arbitrage/
"""

from bellman_ford import bellman_ford
from math import log
import urllib
import sys

api_key = "RjV5i-dRQLT-7WXLH"
site = "http://www.exchangerate-api.com/%s/%s/%f?k=%s"

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

symbols = []
for line in currencies.split("\n"):
    elements = line.strip().split()
    if elements:
        symbols.append(elements[-1])

print symbols

sys.exit()

from_c = "usd"
to_c = "gbp"
amount = 12.50
url = urllib.urlopen(site % (from_c,to_c,amount,api_key))
result = url.read()
print result
