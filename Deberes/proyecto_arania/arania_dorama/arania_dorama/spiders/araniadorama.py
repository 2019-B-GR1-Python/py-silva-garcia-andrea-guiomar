import scrapy 
import csv
import pandas as pd 

class AraniaSpider(scrapy.Spider):
    name='dorama'
    
    titulos_favoritos='.mosts-today > a.media >div.media-body > div.txt-size-16::text'
    ranking='.rating_value .rating_full::attr(style)'
    vistas='.media-body >div.txt-gray-800 > span.txt-size-13::text'
    nuevos_capitulos='.media-body > div.font-weight-500 ::text'
    catalogo=".nav-item > a.nav-link::attr(href)"
    filtro=".custom-control-label::attr(for)"

    #dramas_generales=".p-2 >div.text-white ::text"
    dramas_generales='.position-relative > div::text'
    #año_dramas=".p-2 >div.txt-gray-200 ::text"
    anio_mas_dramas='.col > span.txt-size-20::text'
    parte_link_siguiente='.page-item > a.page-link ::attr(href)'
    urls_dramas='.col-lg-2 > a.shadow-sm::attr(href)'
    titulo_final=".container >h1.text-white ::text"
    estrellas='.mr-2>span.rt-value ::text'
    filtro_dorama="span.mr-2 > a::text"

    

    urls = ['https://www7.doramasmp4.com/'
    ]

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url)

    

    def parse(self, response):
        titulos_ranking =response.css(self.titulos_favoritos).extract()
        visitas=response.css(self.vistas).extract()
        for i in range(len(visitas)):
            visitas[i]=visitas[i].replace(",",".")
        popular=response.css(self.ranking).extract()
        for j in range(len(popular)):
            popular2=popular[j]
            popular3=popular2[6:10]
            print(popular2)
            print(popular3)
            favoritos={'Titulo': titulos_ranking,'visitas': visitas,'popularidad': float(popular3)}
            df=pd.DataFrame(favoritos,columns= ['Titulo','visitas','popularidad'])
            pasar_csv=df.to_csv(r'C://Users//Asus//Documents//GitHub//py-silva-garcia-andrea-guiomar//Deberes//proyecto_arania//arania_dorama//arania_dorama//spiders//drama.csv',index = None, header=True)
            print(df)

        #nuevos_capitulos_generales=response.css(self.nuevos_capitulos).extract()
        link_catalogo=response.css(self.catalogo).extract()
        print(link_catalogo)
        for link in link_catalogo:
            if link =='https://www8.doramasmp4.com/catalogue':
                print("ingresa a ifff.........")
                yield scrapy.Request(url=link,callback =self.catalogo_dorama)
            

    def catalogo_dorama(self, response):
        print("entra a catalogo.............")
        link_catalogo='https://www8.doramasmp4.com/catalogue'

        link_siguiente_pagina=response.css(self.parte_link_siguiente).extract()
        print(link_siguiente_pagina)
        for i in range(len(link_siguiente_pagina)):
            link_contruido=link_catalogo+link_siguiente_pagina[i]
            print(link_contruido)
            yield scrapy.Request(url= link_contruido, callback =self.todo)


        
        
        
        
    def todo(self,response):
        print("entra a todo....")
        dramas=response.css(self.dramas_generales).extract()
        año_mas_capitulos=response.css(self.anio_mas_dramas).extract()
        general={'drama_filtro':dramas,'anio_capitulos':año_mas_capitulos}
        df=pd.DataFrame(general,columns=['drama_filtro','anio_capitulos'])
        df.to_csv('drama2.1.csv')
        urls_drama_coreano=response.css(self.urls_dramas).extract()
        print(urls_drama_coreano)
        for url_corea in urls_drama_coreano:
            yield scrapy.Request(url= url_corea, callback =self.hacer_eso)

    
    def hacer_eso(self, response):
        print('Haciendo esto...')
        for i in range(len(response.css(self.urls_dramas).extract())):
            titulo_drama=response.css(self.titulo_final).extract()
            estrellas=response.css(self.estrellas).extract()
            filtro=response.css(self.filtro_dorama).extract()
            for i in range(len(filtro)):
                cada_dorama={'titulo':titulo_drama,'estrellas':estrellas,'filtro':filtro[i]}
                df=pd.DataFrame(cada_dorama,columns=['titulo','estrellas','filtro'])
                df.to_csv('drama3.csv', mode='a')
            print(titulo_drama)
            print(estrellas)
            print(filtro)
        


           
    

               
            
  
    

        
        
      
   
        
        


                 
               
                

 

        
       

           
    