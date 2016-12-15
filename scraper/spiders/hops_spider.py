# -*- coding: utf-8 -*-
import scrapy
from scraper.items import HopsItem


class HopslistSpider(scrapy.Spider):
    name = u"hopslist"
    allowed_domains = [u"hopslist.com"]
    start_urls = (
        u'http://www.hopslist.com/hops/',
    )

    def parse(self, response):
        # for href in response.xpath(u"//ul[@class='category-module']/li/h6/a/@href").extract():  # noqa
        for href in response.xpath(u"//ul[@class='display-posts-listing']/li/a/@href").extract():  # noqa
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_hops_contents)

    def parse_hops_contents(self, response):
        item = HopsItem()

        item[u'source'] = response.url
        item[u'source_id'] = item[u'source'].split(u'/')[-2]

        item[u'component'] = item[u'source'].split(u'/')[-3]
        name = response.xpath(u"//h1[@class='entry-title']/text()").extract()  # noqa
        item[u'name'] = u'_'.join(name)
        for entry in response.xpath(u'//table/tbody/tr'):
            category = entry.xpath(u'td[1]/text()').extract()
            data = entry.xpath(u'td[2]/text()').extract()
            cat_safe = u' '.join([c.strip() for c in category]).lower().strip()
            data_safe = u' '.join([d.strip() for d in data])
            if cat_safe:
                cat_safe = cat_safe.replace(u'?', u'')
                cat_safe = cat_safe.replace(u' ', u'_')
                cat_safe = cat_safe.replace(u' ', u'-')
                if u'humulone' in cat_safe:
                    cat_safe = u'co_humulone_composition'
                if cat_safe == u'east_of_harvest':
                    cat_safe = u'ease_of_harvest'
                if cat_safe == u'alpha_acid\xa0composition':
                    cat_safe = u'alpha_acid_composition'
                item[cat_safe] = data_safe
        yield item
