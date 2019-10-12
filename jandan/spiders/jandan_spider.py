import scrapy 
import sys
sys.path.append("..")
from jandan.items import JandanItem
import re
class Jandan(scrapy.Spider):
	name = "jandan"
	start_urls = ['http://jandan.net/top',]
	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		##extract top all img source url 
		##there is no http suffix 

		src_list = response.xpath('//div[@class="text"]/p/img/@src').extract()
		
		for src in src_list:
			if(src.split('.')[-1]!='jpg'):
				continue
			item = JandanItem()	
			##replace gif thubom to large size...
			src = re.sub(r'thumb\d+|mw\d+','large',src)
			item['image_urls']=['http:'+src]
			item['image_paths'] = src[-10:]
			yield item
