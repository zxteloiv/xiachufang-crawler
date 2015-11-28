# -*- coding: utf-8 -*-
import scrapy


class RecipeSpider(scrapy.Spider):
    name = "recipe"
    allowed_domains = ["xiachufang.com"]
    start_urls = (
        'http://www.xiachufang.com/category/',
    )

    def parse(self, response):
        pass
