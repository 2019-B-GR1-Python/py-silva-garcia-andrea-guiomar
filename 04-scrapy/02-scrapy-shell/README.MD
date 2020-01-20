# Scrapy

## Scrapy instalacion

Ejecutar dentro del `anaconda prompt`

```
$pip instal scrapy

# Comando generales
```
$scrapy bench

Da las caracteristicas para poder hacer Web Scraping o web Crawling de ese computador
``````

```
$scrapy settings

visualizar configuraciones extras
``````

```
$scrapy version

visualizar configuraciones extras
``````

### scrapy view `url`

``````
$scrapy view https://www.pluralsight.com/authors
``````

se pudo ver el contenido

``````
$scrapy view https://srienlinea.sri.gob.ec/sri-en-linea/inicio/NAT


``````

``````
$scrapy shell http://quotes.toscrape.com/


``````
permite interactuar con la repsuesta se abre un interpretador de python

``````
$response.css('.row > div > div:nth-child(2) > .text::text').extract()

``````


``````
$ response.xpath('/html/head/title').extract()
$ response.xpath('//title').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath('/html/body/div/div[2]/div[2]/h2').extract()
$ response.xpath("//div[@class='quote']/span[@class='text']").extract_first()
$ response.xpath("//div[@class='quote']/span[@class='text']/text()").extract_first()
$ //div[@class='quote']/span/a/@href").extract_first()

```


## Scrapy startproject  `nombre_proyecto`
```
$scrapy startproject arania_basica
```

 









