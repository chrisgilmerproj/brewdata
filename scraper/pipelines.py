# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os

from scraper.items import CerealsItem
from scraper.items import HopsItem
from scraper.items import YeastItem

from brewdata import cereals as cereals_data
from brewdata import hops as hops_data
from brewdata import yeast as yeast_data

# CEREALS_DIR = './brewdata/cereals'
# HOPS_DIR = './brewdata/hops'
# YEAST_DIR = './brewdata/yeast'

CEREALS_DIR = cereals_data()
HOPS_DIR = hops_data()
YEAST_DIR = yeast_data()


class CerealsPipeline(object):

    def process_item(self, item, spider):
        if not isinstance(item, CerealsItem):
            return item
        filename = item[u'name'].lower()
        filename = filename.replace(u" ", u"_")
        filename = filename.replace(u",", u"")
        filename = filename.replace(u"(", u"")
        filename = filename.replace(u")", u"")
        filename = filename.replace(u"/", u"_")
        filename = filename.replace(u"-", u"_")
        filename = filename.replace(u"___", u"_")
        filename = filename.replace(u"__", u"_")
        filename = filename.replace(u"_-", u"_")
        filename = u"{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(CEREALS_DIR), filename)
        item[u'color'] = float(item[u'color'][:-4])
        item[u'ppg'] = round((float(item[u'potential'][:-3]) - 1.0) * 1000, 1)
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item


class HopsPipeline(object):

    def process_item(self, item, spider):
        if not isinstance(item, HopsItem):
            return item
        filename = item[u'source_id'].lower().replace(u" ", u"_")
        filename = filename.replace(u"(", u"")
        filename = filename.replace(u")", u"")
        filename = filename.replace(u"'", u"")
        filename = filename.replace(u"-", u"_")
        filename = u"{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(HOPS_DIR), filename)
        if item[u'alpha_acid_composition']:
            item[u'percent_alpha_acids'] = round(float(item[u'alpha_acid_composition'].split(u'-')[0].split(u'%')[0]) / 100., 3)  # noqa
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item


class YeastPipeline(object):
    ATTENUATION = {
        u'NA': u'0%',
        u'-': u'0%',
        u'Low': u'72%',
        u'Medium': u'75%',
        u'Med-High': u'76-77%',
        u'Medium-High': u'76-77%',
        u'High': u'78%',
        u'Very High': u'80%',
    }

    def process_item(self, item, spider):
        if not isinstance(item, YeastItem):
            return item
        if item[u'attenuation'] in self.ATTENUATION:
            item[u'attenuation'] = self.ATTENUATION[item[u'attenuation']]
        item[u'attenuation'] = item[u'attenuation'].replace(u"<", u"")
        item[u'attenuation'] = item[u'attenuation'].replace(u">", u"")
        item[u'attenuation'] = item[u'attenuation'].replace(u"%", u"")
        item[u'attenuation'] = item[u'attenuation'].split(u'-')
        item[u'attenuation'] = [float(att) / 100. for att in item[u'attenuation']]  # noqa
        item[u'percent_attenuation'] = sum(item[u'attenuation']) / len(item[u'attenuation'])  # noqa

        # Remove en dash
        item[u'name'] = item[u'name'].replace('\u2013', '-')

        if u'yeast_id' in item:
            identifier = item[u'yeast_id'].lower()
        else:
            identifier = item[u'name'].lower()
        filename = u'{}_{}'.format(item[u'manufacturer'].lower(),
                                   identifier)
        filename = filename.replace(u" ", u"_")
        filename = filename.replace(u"-", u"_")
        filename = filename.replace(u"/", u"_")
        filename = u"{}.json".format(filename)
        filepath = os.path.join(os.path.abspath(YEAST_DIR), filename)
        with open(filepath, 'wb') as f:
            line = json.dumps(dict(item))
            f.write(line)
        return item
