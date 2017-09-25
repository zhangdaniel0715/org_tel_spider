# -*- coding: utf-8 -*-
import scrapy


class OrgTelSpider(scrapy.Spider):
    name = 'org_tel'
    allowed_domains = ['qu114.com']
    start_urls = ['http://b2b.qu114.com/jinrong/pn1/']

    def parse(self, response):
        for sel in response.xpath('//*[@id="w_960"]/div[4]/div[1]/div[@class="com_info"]'):
        	link = sel.xpath('div/div[2]/p/a/@href').extract()
        	name = sel.xpath('div/div[2]/p[1]/a/text()').extract()
        	desc = sel.xpath('div/div[2]/p[2]/text()').extract()
        	content = sel.xpath('div/div[2]/p[3]/text()').extract()
