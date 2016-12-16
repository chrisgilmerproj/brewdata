# BrewData

Data for use with [BrewDay](https://github.com/chrisgilmerproj/brewday).

## Usage

To use BrewData in another project you can do the following:

```py
>>> import brewdata
>>> brewdata.where()
'/usr/local/lib/python2.7/site-packages/brewdata/'
```

It may be more useful to find the specific location of data:

```py
>>> from brewdata import cereals as cereals_data
>>> cereals_data()
'/usr/local/lib/python2.7/site-packages/brewdata/cereals'
```

## Format

The beer data is split into four sections: Cereals, Hops, Water, and Yeast.
The data is provided in `*.json` files, one file per data item.

## Scraper

Using the python project Scrapy the data is collected from publicly available
websites where possible.  Try to ensure that the source is always listed in
any files scraped from websites.  Permission should always be asked for to
ensure there is no copyright problems.

### Running the scraper

The scrapers for each data type are easy to run:

```sh
make scrape_cereals
...
make scrape_hops
...
make scrape_yeast
...
```

### Shell commands

```sh
$ scrapy shell "http://www.hopslist.com/"
```

## Sources

The data comes from several scraped websites.  Additional data can be found in
other listed sources.  Scraped sources have "(scraped)" next to them.

### Cereals

- http://beersmith.com/grain-list/ (scraped)

### Hops

- http://www.hopslist.com/ (scraped)
- http://cropandsoil.oregonstate.edu/hopcultivars/

### Yeast

- http://www.brewersfriend.com/yeast/ (scraped)
