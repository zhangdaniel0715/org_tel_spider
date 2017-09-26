# -*- coding: utf-8 -*-
import scrapy
from org_tel_spider.items import OrgTelSpiderItem


class OrgTelSpider(scrapy.Spider):
    name = 'org_tel'
    allowed_domains = ['qu114.com']

    def __init__(self, *args, **kwargs):
        super(OrgTelSpider, self).__init__(*args, **kwargs)
        self.start_urls = []
        ## init crawl target pages
        for index in range(1, 48):
            url = 'http://b2b.qu114.com/jinrong/pn' + str(index) + '/'
            self.start_urls.append(url)

    def parse(self, response):
        for sel in response.xpath('//*[@id="w_960"]/div[4]/div[1]/div[@class="com_info"]'):
            link = sel.xpath('div/div[2]/p/a/@href').extract_first()
            if link:
                self.logger.info('crawler target page:' + link)
                yield scrapy.Request(link, callback=self.parse_organization)

    def parse_organization(self, response):
        self.logger.info('Start to crawl organization detail')
        organization = OrgTelSpiderItem()
        organization['name'] = response.xpath('//div[@class="d_left"]/p[1]/a/text()').extract_first()
        organization['tel_num'] = response.xpath('//div[@class="d_left"]/p[3]/strong/text()').extract_first()
        organization['link'] = response.url
        yield organization
