BrewData
========

Data for use with
`BrewDay <https://github.com/chrisgilmerproj/brewday>`__.

Usage
-----

To use BrewData in another project you can do the following:

.. code:: py

    >>> import brewdata
    >>> brewdata.where()
    '/usr/local/lib/python2.7/site-packages/brewdata/'

It may be more useful to find the specific location of data:

.. code:: py

    >>> from brewdata import cereals as cereals_data
    >>> cereals_data()
    '/usr/local/lib/python2.7/site-packages/brewdata/cereals'

Format
------

The beer data is split into four sections: Cereals, Hops, Water, and
Yeast. The data is provided in ``*.json`` files, one file per data item.

Scraper
-------

Using the python project Scrapy the data is collected from publicly
available websites where possible. Try to ensure that the source is
always listed in any files scraped from websites. Permission should
always be asked for to ensure there is no copyright problems.

Running the scraper
~~~~~~~~~~~~~~~~~~~

.. code:: sh

    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt
    $ scrapy runspider scraper/spiders/cereals_spider.py
    $ scrapy runspider scraper/spiders/hops_spider.py
    $ scrapy runspider scraper/spiders/yeast_spider.py

Shell commands
~~~~~~~~~~~~~~

.. code:: sh

    $ scrapy shell "http://www.hopslist.com/"

Sources
-------

Cereals
~~~~~~~

-  http://beersmith.com/grain-list/

Hops
~~~~

-  http://www.hopslist.com/

Yeast
~~~~~

-  http://www.brewersfriend.com/yeast/
