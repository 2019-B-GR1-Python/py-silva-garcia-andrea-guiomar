# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class  SoloCapsulaPipeline(object):
    def process_item(self, item, spider):
        titulo= item['titulo'][0]
        if('capsula' not in titulo):
            raise DropItem('No tiene capsula')
        else:
            return item

class TransformarTituloAMinuscula(object):
    def process_item(self, item, spider):
        titulo= item['titulo'][0]
        item['titulo'][0]=titulo.lower()
        return item


class AraniaFybecaPipeline(object):
    def process_item(self, item, spider):
        return item
