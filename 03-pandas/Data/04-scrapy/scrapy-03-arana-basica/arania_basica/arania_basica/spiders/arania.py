import scrapy

class IntroSpider(scrapy.Spider):
    name='introduccio_spider'

    urls=['http://books.toscrape.com/catalogue/category/books/travel_2/index.html']
    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
        
    def parse(self, response):
        etiqueta_contenedora =response.css('article.product_pod')
        titulos=etiqueta_contenedora.css('h3 > a::text').extract()
        ##URL COMPLETO PRECIO EN FLOTANTE
        precio_libro=etiqueta_contenedora.css('div.product_price>p.price_color::text').extract()
        for i in precio_libro:
            i=i[1:]
        print(i)
        url_imagen=etiqueta_contenedora.css('div.image_container>a::attr(href)').extract()
        print("INICIANDO...")
        print(titulos)
        print(precio_libro)
        print(url_imagen)



