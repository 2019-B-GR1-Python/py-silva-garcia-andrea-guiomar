import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class AraniaCrowlOnu(CrawlSpider):
    name='crawl_onu' #heredado(override)

    allowed_domains=['un.org']

    start_urls=['https://www.un.org/en/sections/about-un/funds-programmes-specialized-agencies-and-others/']

    ##BUSQUETODO!
    regla_uno=(Rule(LinkExtractor(), callback='parse_page'),)
    url_segment_permitido=('funds-programmes-specialized-agencies-and-others/')

    ##Busca en estos dominios con estos segmentos
    regla_dos=(Rule(LinkExtractor(allow_domains=allowed_domains,allow=url_segment_permitido), callback='parse_page'),)

    url_segmento_restringido=('ar/sections','zh/sections','ru/secctions')

    ##Restringir segementos de la url

    regla_tres=(Rule(LinkExtractor(allow_domains=allowed_domains,
    allow=url_segment_permitido,deny=url_segmento_restringido),callback='parse_page'),)

    ##reglas que se van a guardar 
    rules=regla_uno #heredado
     
    #construir el parse_page

    def parse_page(self,response):
        lista_programa_onu=response.css('div.field-items > div.field-item > h4::text').extract()
        for agencia in lista_programa_onu:
            with open('onu_agencias.txt','a+',encoding='utf-8')as archivo:
                archivo.write(agencia +'\n')


