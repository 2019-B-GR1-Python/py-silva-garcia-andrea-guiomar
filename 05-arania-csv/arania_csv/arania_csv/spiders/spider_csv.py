#spider_csv.py

#spider
#crawlspider
#csvfeedspider

from scrapy.spiders import CSVFeedSpider

class VinosBlancosArania(CSVFeedSpider):
    name= "vinos"
    start_urls=['https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv']

    delimiter=';'
    quotechar='"'
    headers = [
        'fixed density',
        'volatile acidity',
        'citric acid',
        'residual sugar',
        'chlorides',
        'free sulfur dioxide',
        'total sulfur dioxide',
        'density',
        'pH',
        'sulphates',
        'alcohol',
        'quality'
    ]
    def parse_row(self, reponse, row):
        print('ph=',row['pH'])
        print('citric acid=',row['citric acid'])
       # with open('vinos.txt','a+',encoding='utf8'):
       #     archivo.writw(row['fixed densty']+'\n')