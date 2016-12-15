# -*- coding: utf-8 -*-
import scrapy
from scraper.items import CerealsItem


class BeerSmithSpider(scrapy.Spider):
    name = u"beersmith"
    allowed_domains = [u"beersmith.com"]
    start_urls = (
        u'http://beersmith.com/grain-list/',
    )

    def parse(self, response):
        for href in response.xpath(u'//table[@class="ms-list4-main"]/tbody/tr/td/a/@href').extract():  # noqa
            url = response.urljoin(href)
            yield scrapy.Request(url, callback=self.parse_cereals_contents)

    def parse_cereals_contents(self, response):
        item = CerealsItem()

        item[u'source'] = response.url
        source_id = item[u'source'].split(u'/')[-1].split(u'.')[0].split(u'_')[-1]  # noqa
        item[u'source_id'] = source_id

        name = response.xpath(u'//h2/text()').extract()[0]
        item[u'name'] = name
        notes = response.xpath(u"//body/center/table/tbody/tr/td/text()").extract()  # noqa
        item[u'notes'] = u' '.join(notes).strip()

        for entry in response.xpath(u'//table/tbody/tr/td/table/tbody/tr/td'):
            category = entry.xpath(u'b/text()').extract()
            data = entry.xpath(u'text()').extract()
            cat_safe = u' '.join([c.strip() for c in category]).lower().strip()
            data_safe = u' '.join([d.strip() for d in data])
            if cat_safe:
                cat_safe = cat_safe[:-1]
                cat_safe = cat_safe.replace(u'/', u'_')
                cat_safe = cat_safe.replace(u' ', u'_')
                if cat_safe == u'type':
                    cat_safe = u'cereal_type'
                item[cat_safe] = data_safe
        yield item
