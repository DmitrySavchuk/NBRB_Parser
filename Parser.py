from Crawler import Crawler
from Extractor import Extractor
from Loader import Loader
import sys

url = sys.argv[1]
csv_file = sys.argv[2]
data_base = sys.argv[3]

cr = Crawler(url)
rates = cr.get_response()

ex = Extractor(rates, csv_file)
ex.extraction()

ld = Loader('rates.csv', data_base)
ld.save_to_db()
