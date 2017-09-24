#! /usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import json
import string

"""
Parse the BJCP 2015 Styles CSV file
"""


def main():
    categories = {}
    style_map = {}

    filename = '2015_Styles.csv'
    with open(filename, 'r') as fileobj:
        reader = csv.reader(fileobj)
        historical_subcat = 64
        for row in reader:
            rownum = row[0]
            category = row[1]
            style = row[2]
            og = row[3]
            fg = row[4]
            abv = row[5]
            ibu = row[6]
            color_srm = row[7]
            tags = row[8]
            strength = row[9]
            color_name = row[10]
            fermentation = row[11]
            conditioning = row[12]
            region_of_origin = row[13]
            style_family = row[14]
            specialty_beer = row[15]
            era = row[16]
            bitter_balance_malty = row[17]
            sour_hoppy_sweet = row[18]
            spice = row[19]
            smoke_roast_wood_fruit = row[20]
            cat_sub_2008 = row[22]

            historical = 'Historical Beer:'
            if style.startswith(historical):
                category = '27'
                # style = style[len(historical):]

            if rownum and category:
                # Split up specialty IPAs
                if not og and style and 'Specialty' not in style:
                    cat_num, cat_name = style.split('. ')
                    if cat_name == 'IPA':
                        cat_name = 'India Pale Ale'
                    if cat_num not in categories:
                        categories[cat_num] = string.capwords(cat_name)

                if og:
                    cat = ''
                    subcat = ''

                    if category[-2].isalpha():
                        subcat = category[-2:]
                        cat = category[:-2]
                    elif category[-1].isalpha():
                        subcat = category[-1:]
                        cat = category[:-1]

                    # Handle historical beers
                    if cat:
                        cat = int(cat)
                    else:
                        cat = category

                    if not subcat:
                        historical_subcat += 1
                        subcat = chr(historical_subcat)

                    # Create the dictionary
                    if cat not in style_map:
                        style_map[cat] = {}

                    style_name = ''
                    if '.' in style:
                        subcat, style_name = style.split('. ')
                        if not subcat and subcat == category[-1]:
                            cat = category[:-1]
                    if not style_name:
                        style_name = style

                    og_vals = og.split('-')
                    fg_vals = fg.split('-')
                    abv_vals = abv.split('-')
                    ibu_vals = ibu.split('-')
                    if '-' in color_srm:
                        color_vals = color_srm.split('-')
                    else:
                        # Gose
                        color_vals = color_srm.split('.')
                    if og_vals[0] == 'Varies':
                        og_vals = []
                        fg_vals = []
                        abv_vals = []
                        ibu_vals = []
                        color_vals = []
                    else:
                        og_vals[1] = str(1.0 + float(og_vals[1]) / 1000.)
                        if float(fg_vals[1]) > 1.015:
                            fg_vals[1] = str(1.0 + float(fg_vals[1]) / 1000.)
                    info = {
                        'category': cat,
                        'subcategory': subcat.strip(),
                        'style': style_name.strip(),
                        'og': [float(o) for o in og_vals],
                        'fg': [float(f) for f in fg_vals],
                        'abv': [round(float(a) / 100.0, 3) for a in abv_vals],
                        'ibu': [float(i) for i in ibu_vals],
                        'color': [float(c) for c in color_vals],
                        'tags': tags,
                        'strength': strength,
                        'color_name': color_name,
                        'fermentation': fermentation,
                        'conditioning': conditioning,
                        'region_of_origin': region_of_origin,
                        'style_family': style_family,
                        'specialty_beer': specialty_beer,
                        'era': era,
                        'bitter_balance_malty': bitter_balance_malty,
                        'sour_hoppy_sweet': sour_hoppy_sweet,
                        'spice': spice,
                        'smoke_roast_wood_fruit': smoke_roast_wood_fruit,
                        'cat_sub_2008': cat_sub_2008,
                    }
                    style_map[cat][subcat] = info

    with open('categories.json', 'w') as fileobj:
        fileobj.write(json.dumps(categories))

    with open('styles.json', 'w') as fileobj:
        fileobj.write(json.dumps(style_map))


if __name__ == "__main__":
    main()
