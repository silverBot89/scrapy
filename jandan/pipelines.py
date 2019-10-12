# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html



import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


# class JandanPipeline(object):
#     def process_item(self, item, spider):
#     	print("do nothing...")
#         return item

class ImagePipeline(ImagesPipeline):
		#item = request.meta.get('item')#注意注意注意！！！，这里有坑，不能再使用request.meta['item']
		#index = request.meta.get('index')
		# print(request.url)
		# print(index)
		#image_name = item['name'][index] + '.' + request.url.split('/')[-1].split('.')[-1]
		#file_name = "{0}/{1}".format('jiandan',image_name)
		#return file_name
	def file_path(self, request, response=None, info=None):
		image_guid = request.url.split('/')[-1]  
		return 'full/%s' % (image_guid) 

	def get_media_requests(self, item, info):
		print("~~"*20+"downloading.......")
		for image_url in item['image_urls']:
			yield scrapy.Request(url=image_url,meta={'images': item['image_paths']})

	def item_completed(self, results, item, info):
		image_paths = [x['path'] for ok, x in results if ok]
		if not image_paths:
			raise DropItem("Item contains no images")
		item['image_paths'] = image_paths
		return item