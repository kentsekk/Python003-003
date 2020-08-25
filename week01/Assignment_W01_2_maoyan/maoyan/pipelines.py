# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime

class MaoyanPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self, item, spider):
        film_name = item['film_name']
        film_cat = item['film_cat']
        film_releasedate = item['film_releasedate']
        output = f'{film_name},{film_cat},{film_releasedate}\n'
        with open('./maoyan_scrapy.csv', 'a', encoding='utf-8') as article:
            article.write(output)
        return item