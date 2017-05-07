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

    filename = b'2015_Styles.csv'
    with open(filename, b'rb') as fileobj:
        reader = csv.reader(fileobj)
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

            if rownum and category:
                # Split up specialty IPAs
                if not og and style and b'Specialty' not in style:
                    cat_num, cat_name = style.split(b'. ')
                    if cat_name == b'IPA':
                        cat_name = b'India Pale Ale'
                    if cat_num not in categories:
                        categories[cat_num] = string.capwords(cat_name)

                if og:
                    cat = b''
                    subcat = b''

                    if category[-2].isalpha():
                        subcat = category[-2:]
                        cat = category[:-2]
                    elif category[-1].isalpha():
                        subcat = category[-1:]
                        cat = category[:-1]
                    cat = int(cat)

                    # Create the dictionary
                    if cat not in style_map:
                        style_map[cat] = {}

                    style_name = b''
                    if b'.' in style:
                        subcat, style_name = style.split(b'. ')
                        if not subcat and subcat == category[-1]:
                            cat = category[:-1]

                    og_vals = og.split(b'-')
                    fg_vals = fg.split(b'-')
                    abv_vals = abv.split(b'-')
                    ibu_vals = ibu.split(b'-')
                    color_vals = color_srm.split(b'-')
                    if og_vals[0] == b'Varies':
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
                        b'category': cat,
                        b'subcategory': subcat.strip(),
                        b'style': style_name.strip(),
                        b'og': [float(o) for o in og_vals],
                        b'fg': [float(f) for f in fg_vals],
                        b'abv': [round(float(a) / 100.0, 3) for a in abv_vals],
                        b'ibu': [float(i) for i in ibu_vals],
                        b'color': [float(c) for c in color_vals],
                        b'tags': tags,
                        b'strength': strength,
                        b'color_name': color_name,
                        b'fermentation': fermentation,
                        b'conditioning': conditioning,
                        b'region_of_origin': region_of_origin,
                        b'style_family': style_family,
                        b'specialty_beer': specialty_beer,
                        b'era': era,
                        b'bitter_balance_malty': bitter_balance_malty,
                        b'sour_hoppy_sweet': sour_hoppy_sweet,
                        b'spice': spice,
                        b'smoke_roast_wood_fruit': smoke_roast_wood_fruit,
                        b'cat_sub_2008': cat_sub_2008,
                    }
                    style_map[cat][subcat] = info

    with open(b'categories.json', b'w') as fileobj:
        fileobj.write(json.dumps(categories))

    with open(b'styles.json', b'w') as fileobj:
        fileobj.write(json.dumps(style_map))


if __name__ == "__main__":
    main()
