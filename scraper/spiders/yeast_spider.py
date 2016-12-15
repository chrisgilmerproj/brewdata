# -*- coding: utf-8 -*-
import scrapy
from scraper.items import YeastItem


class YeastlistSpider(scrapy.Spider):
    name = u"yeastlist"
    allowed_domains = [u"brewersfriend.com"]
    start_urls = (
        u'http://www.brewersfriend.com/yeast-wyeast/',
        u'http://www.brewersfriend.com/yeast-whitelabs/',
        u'http://www.brewersfriend.com/yeast-fermentis/',
        u'http://www.brewersfriend.com/yeast-danstar/',
        u'http://www.brewersfriend.com/yeast-other/',
    )

    def parse(self, response):

        source = response.url
        manufacturer = response.xpath(u"//h2/text()").extract()[0]
        if u'by' in manufacturer:
            manufacturer = manufacturer.split(u' by ')[-1]
        elif u'By' in manufacturer:
            manufacturer = manufacturer.split(u' By ')[-1]
        elif u'Other' in manufacturer:
            manufacturer = u'Other'
        for entry in response.xpath(u"//div[@class='post']/table/tbody/tr"):
            data = entry.xpath(u"td/span/text()").extract()
            if len(data) and data[0] != u'\n':
                item = YeastItem()
                item[u'name'] = data[0]
                item[u'source'] = source
                item[u'manufacturer'] = manufacturer
                item[u'yeast_id'] = data[1]
                item[u'attenuation'] = data[2]
                item[u'flocculation'] = data[3]
                item[u'optimum_temp'] = data[4].split()[0]
                item[u'alcohol_tolerance'] = data[5]
                yield item
            elif len(data) == 0:
                data = entry.xpath(u"td/text()").extract()
                if len(data) and data[0] != u'\n':
                    item = YeastItem()
                    item[u'name'] = data[0]
                    item[u'source'] = source
                    item[u'manufacturer'] = manufacturer
                    item[u'attenuation'] = data[1]
                    item[u'flocculation'] = data[2]
                    item[u'optimum_temp'] = data[3].split()[0]
                    item[u'alcohol_tolerance'] = data[4]
                    yield item
