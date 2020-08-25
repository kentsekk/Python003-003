# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass
    # def start_requests(self):
        
    def parse(self, response):
        print(response.url)
        items = []
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')[:10]
            
        for movie in movies:
            item = MaoyanItem()
            film_name = movie.xpath('div[1]/span/text()')[0].extract().strip()
            film_cat = movie.xpath('div[2]/text()')[1].extract().strip()
            film_releasedate = movie.xpath('div[4]/text()')[1].extract().strip()
            item['film_name'] = film_name
            item['film_cat'] = film_cat
            item['film_releasedate'] = film_releasedate
            items.append(item)
        return items
    