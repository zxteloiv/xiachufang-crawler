# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class RecipeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    rating = scrapy.Field()
    rating_num = scrapy.Field()
    tried_num = scrapy.Field()

    desc = scrapy.Field()
    ingredients = scrapy.Field()
    steps = scrapy.Field()
    tips = scrapy.Field()

    url = scrapy.Field()
    crawl_date = scrapy.Field()
    recipe_id = scrapy.Field()


