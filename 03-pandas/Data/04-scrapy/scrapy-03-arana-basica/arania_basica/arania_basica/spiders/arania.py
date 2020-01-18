import scrapy

class IntroSpider(scrapy.Spider):
    name='introduccio_spider'
    
    titulos='article.product_pod>h3 > a::text'
    precio_libro='article.product_pod>div.product_price>p.price_color::text'
    url_imagen='div.image_container>a>img.thumbnail::attr(src)'
    

    urls = ['http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    'http://books.toscrape.com/catalogue/category/books/mystery_3/index.html',
'http://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html',
'http://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html',
'http://books.toscrape.com/catalogue/category/books/classics_6/index.html',
'http://books.toscrape.com/catalogue/category/books/philosophy_7/index.html',
'http://books.toscrape.com/catalogue/category/books/romance_8/index.html',
'http://books.toscrape.com/catalogue/category/books/womens-fiction_9/index.html',
'http://books.toscrape.com/catalogue/category/books/fiction_10/index.html',
'http://books.toscrape.com/catalogue/category/books/childrens_11/index.html',
'http://books.toscrape.com/catalogue/category/books/religion_12/index.html',
'http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html',
'http://books.toscrape.com/catalogue/category/books/music_14/index.html',
'http://books.toscrape.com/catalogue/category/books/default_15/index.html',
'http://books.toscrape.com/catalogue/category/books/science-fiction_16/index.html',
'http://books.toscrape.com/catalogue/category/books/sports-and-games_17/index.html',
'http://books.toscrape.com/catalogue/category/books/add-a-comment_18/index.html',
'http://books.toscrape.com/catalogue/category/books/fantasy_19/index.html',
'http://books.toscrape.com/catalogue/category/books/new-adult_20/index.html',
'http://books.toscrape.com/catalogue/category/books/young-adult_21/index.html',
'http://books.toscrape.com/catalogue/category/books/science_22/index.html',
'http://books.toscrape.com/catalogue/category/books/poetry_23/index.html',
'http://books.toscrape.com/catalogue/category/books/paranormal_24/index.html',
'http://books.toscrape.com/catalogue/category/books/art_25/index.html',
'http://books.toscrape.com/catalogue/category/books/psychology_26/index.html',
'http://books.toscrape.com/catalogue/category/books/autobiography_27/index.html',
'http://books.toscrape.com/catalogue/category/books/parenting_28/index.html',
'http://books.toscrape.com/catalogue/category/books/adult-fiction_29/index.html',
'http://books.toscrape.com/catalogue/category/books/humor_30/index.html',
'http://books.toscrape.com/catalogue/category/books/horror_31/index.html',
'http://books.toscrape.com/catalogue/category/books/history_32/index.html',
'http://books.toscrape.com/catalogue/category/books/food-and-drink_33/index.html',
'http://books.toscrape.com/catalogue/category/books/christian-fiction_34/index.html',
'http://books.toscrape.com/catalogue/category/books/business_35/index.html',
'http://books.toscrape.com/catalogue/category/books/biography_36/index.html',
'http://books.toscrape.com/catalogue/category/books/thriller_37/index.html',
'http://books.toscrape.com/catalogue/category/books/contemporary_38/index.html',
'http://books.toscrape.com/catalogue/category/books/spirituality_39/index.html',
'http://books.toscrape.com/catalogue/category/books/academic_40/index.html',
'http://books.toscrape.com/catalogue/category/books/self-help_41/index.html',
'http://books.toscrape.com/catalogue/category/books/historical_42/index.html',
'http://books.toscrape.com/catalogue/category/books/christian_43/index.html',
'http://books.toscrape.com/catalogue/category/books/suspense_44/index.html',
'http://books.toscrape.com/catalogue/category/books/short-stories_45/index.html',
'http://books.toscrape.com/catalogue/category/books/novels_46/index.html',
'http://books.toscrape.com/catalogue/category/books/health_47/index.html',
'http://books.toscrape.com/catalogue/category/books/politics_48/index.html',
'http://books.toscrape.com/catalogue/category/books/cultural_49/index.html',
'http://books.toscrape.com/catalogue/category/books/erotica_50/index.html',
'http://books.toscrape.com/catalogue/category/books/crime_51/index.html']

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)
    nuevo_path_libros=[]
    def parse(self, response):
        link_libros =response.css('div.side_categories>ul>li>ul>li>a::attr(href)').extract()
        path_link_libros = 'http://books.toscrape.com/catalogue/category/books'
        path_link_libros_reemplazar = '..'
        completo=self.completar_path(link_libros, path_link_libros, path_link_libros_reemplazar)
        
        self.nuevo_path_libros=completo[1:]
         
        titulos_extr =  response.css(self.titulos).extract()
        precios_str =  response.css(self.precio_libro).extract()
        precio_flotante=self.cambio_float(precios_str)
        url_imagen_categoria = response.css(self.url_imagen).extract() 
        path_imagenes = 'http://books.toscrape.com/'
        path_imagenes_reemplazar = '../../../../'
        nuevo_path_imagen=self.completar_path(url_imagen_categoria, path_imagenes, path_imagenes_reemplazar)
        with open('categorias.txt', 'a+') as file:
            for i in range(len(titulos_extr)):
                linea = 'Title: ' + titulos_extr[i] + ' ,Price: ' + str(precio_flotante[i]) + ' , Image URL: ' + nuevo_path_imagen[i] + '\n'
                file.write(linea) 
       # for url in self.nuevo_path_libros:
       #     yield scrapy.Request(url = url,callback = self.parse)
 
    def cambio_float(self, precios):
        nuevo_precio=[]
        for precio in precios:
            n_precio=precio[1:]
            numero=float(n_precio)
            nuevo_precio.append(numero)
        return nuevo_precio

    def completar_path(self,lista ,original, reemplazar):
            for cambio in range(len(lista)):
                lista[cambio] = lista[cambio].replace(reemplazar, original)
            return lista

   



        
    
    



