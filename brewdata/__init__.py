#!/usr/bin/env python

import os


def where():
    """
    Return the installation location of BrewData
    """
    f = os.path.split(__file__)[0]
    return os.path.abspath(f)


def cereals():
    return(os.path.join(where(), 'cereals'))


def hops():
    return(os.path.join(where(), 'hops'))


def yeast():
    return(os.path.join(where(), 'yeast'))


if __name__ == '__main__':
    print(where())
