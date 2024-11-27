# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlPipeline:
    def process_item(self, item, spider):
        return item



import json

class SaveToJsonPipeline:
    def open_spider(self, spider):
        self.file = open('questionDATA3.json', 'w')  # Create and open the JSON file
        self.file.write('[')  # Start the JSON array

    def close_spider(self, spider):
        self.file.write(']')  # End the JSON array
        self.file.close()  # Close the file

    def process_item(self, item, spider):
        # Write the item to the file in JSON format
        json.dump(item, self.file, indent=4)
        self.file.write(',\n')  # Separate items with commas
        return item

