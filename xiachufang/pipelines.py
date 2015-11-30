# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class RecipePipeline(object):
    def __init__(self, name):
        self.file = open(name, 'wb')

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            name=crawler.settings.get('PIPELINE_SAVE_FILENAME', default='items.json')
        )

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.file.flush()

    def close_spider(self, spider):
        self.file.close()
