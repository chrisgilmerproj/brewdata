#!/usr/bin/env python

import os


def where():
    """
    Return the installation location of BrewData
    """
    f = os.path.split(__file__)[0]
    return os.path.abspath(f)


def cereals():
    return(os.path.join(where(), b'cereals'))


def hops():
    return(os.path.join(where(), b'hops'))


def yeast():
    return(os.path.join(where(), b'yeast'))


if __name__ == '__main__':
    print(where())
