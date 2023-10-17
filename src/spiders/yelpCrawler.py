'''
Author: Alex Shi
Date: 2023-10-16 19:37:38
LastEditTime: 2023-10-16 19:38:16
LastEditors: Alex Shi
Description: 
FilePath: /retail-sales-dashboard/src/spiders/yelpCrawler.py
'''
import scrapy

class yelpCrawler(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/',
    )

    def parse(self, response):
        pass