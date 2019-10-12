##import scrapy
##from scrapy.crawler import CrawlerProcess
##from spiders.jandan_spider import Jandan
##
##process = CrawlerProcess()
##
##process.crawl(Jandan)
##process.start()
from scrapy import cmdline
cmdline.execute('scrapy crawl jandan'.split())
