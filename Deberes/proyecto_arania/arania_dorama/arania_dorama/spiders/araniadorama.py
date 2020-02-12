import scrapy 

class AraniaSpider(scrapy.Spider):
    name='dorama'
    
    titulos_favoritos='.media-body > div.txt-size-16::text'
    ranking=('.rating_value .rating_full::attr(style)')
    nuevos_capitulos='.media-body > div.font-weight-500 ::text'
    catalogo=".nav-item > a.nav-link::attr(href)"
    filtro=".custom-control-label::attr(for)"

    dramas_generales=".p-2 >div.text-white ::text"
    año_dramas=".p-2 >div.txt-gray-200 ::text"
    urls_dramas="a.shadow-sm::attr(href)"
    titulo_final=".text-white ::text"
    descripcion='.col-md-8 > p.txt-size-16 ::text'
    filtro_dorama="span.mr-2 > a::text"
    

    urls = ['https://www7.doramasmp4.com/'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    

    def parse(self, response):
        titulos_ranking =response.css(self.titulos_favoritos).extract()
        popular=response.css(self.ranking).extract()
        nuevos_capitulos_generales=response.css(self.nuevos_capitulos).extract()
        link_catalogo=response.css(self.catalogo).extract()

        for link in link_catalogo:
            
            if link =='https://www7.doramasmp4.com/catalogue':
                yield scrapy.Request(url=link)
                dramas=response.css(self.dramas_generales).extract()
                año_dramas=response.css(self.año_dramas).extract()
                urls_drama_coreano=response.css(self.urls_dramas).extract()
                print(urls_drama_coreano)
                for url_corea in urls_drama_coreano:
                    yield scrapy.Request(url= url_corea, callback =self.hacer_eso)
        with open('dramas.txt', 'a+') as file:
            for i in range(len(titulos_ranking)):
                
                linea = 'Titutlo_drama: ' + titulos_ranking[i] + '\n'
                file.write(linea)
            for i in range(len(popular)):
                linea2= 'Ranking: ' + popular[i] +'\n'
                file.write(linea2)
            for i in range(len(nuevos_capitulos_generales)):
                linea3=  'Nuevos capitulos: ' + nuevos_capitulos_generales[i] + '\n'
                file.write(linea3)
        with open('dramas2.txt', 'a+') as file:
            for i in range(len(dramas)):
                linea = 'DRAMA: ' + dramas[i] + ' AÑO: ' + año_dramas[i] +'\n'
                file.write(linea)
       
    def hacer_eso(self, response):
        print('Haciendo esto...')
        titulo_drama=response.css(self.titulo_final).extract()
        describir=response.css(self.descripcion).extract()
        filtro=response.css(self.filtro_dorama).extract()
           
    

               
            
    

        with open('dramas3.txt', 'a+') as file:
            for i in range(len(titulo_drama)):
                linea = 'TITULO: ' + titulo_drama[i] + ' DESCRIPCION: ' + describir[i]+'FILTRO: '+filtro[i] +'\n'
                file.write(linea)
    

        
        
      
   
        
        


                 
               
                

 

        
       

           
    