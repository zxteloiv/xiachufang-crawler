# -*- coding: utf-8 -*-
import scrapy
import re
import datetime

from itertools import izip
from xiachufang.items import RecipeItem

class RecipeSpider(scrapy.Spider):
    name = "recipe"
    allowed_domains = ["xiachufang.com"]
    start_urls = (
        'http://www.xiachufang.com/category/',
    )

    def parse(self, response):
        if re.search('/recipe/', response.url):
            yield self.parse_recipe(response)

        # follow links
        for href in response.xpath("//a[@href]/@href").extract():
            if not re.match('^http|^/', href):
                continue

            url = response.urljoin(href)
            yield scrapy.Request(url, callback = self.parse)

    def parse_recipe(self, response):
        item = RecipeItem()
        # use the max length text with the attribute *itemprop*
        name_xpath = '//*[@itemprop="name"]/text()'
        item["name"] = max(response.xpath(name_xpath).extract(), key = len).strip()

        # the rating value for this recipe
        rating_xpath = '//*[@itemprop="ratingValue"]/text()'
        item["rating"] = float(response.xpath(rating_xpath).extract()[0])

        # how many users have rated this recipe
        rating_num_xpath = '//*[@itemprop="ratingCount"]/text()'
        item["rating_num"] = int(response.xpath(rating_num_xpath).extract()[0])

        # how many users have used this recipe to cook
        tried_num_xpath = '//*[@class="cooked"]//*[@class="number"]/text()'
        item["tried_num"] = int(response.xpath(tried_num_xpath).extract()[0])

        # description for this recipe
        desc_xpath = '//*[@itemprop="description"]/text()'
        item["desc"] = "\n".join(x.strip() for x in response.xpath(desc_xpath).extract())

        # ingredients in this recipe
        for sel in response.xpath('//*[@itemprop="ingredients"]'):
            # ingredient name may be here or inside an <a>
            name_sel = sel.xpath('*[contains(@class,"name")]')
            unit_sel = sel.xpath('*[contains(@class,"unit")]')
            
            item["ingredients"] = dict(izip(
                (re.sub('<[^>]*>', '', x).strip() for x in name_sel.extract()),
                (re.sub('<[^>]*>', '', x).strip() for x in unit_sel.extract()),
                ))

        # steps to cook
        step_xpath = '//div[@class="steps"]/descendant::p[@class="text"]/text()'
        item["steps"] = [x.strip() for x in response.xpath(step_xpath).extract()]

        # tips content
        tips_xpath = '//div[@class="tip"]/text()'
        if tips_xpath:
            item["tips"] = "\n".join(x.strip() for x in response.xpath(tips_xpath).extract())

        item["url"] = response.url
        item["crawl_date"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        item["recipe_id"] = re.search('(\d+)', response.url).groups(0)[0]

        return item

