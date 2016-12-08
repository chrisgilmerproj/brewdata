#!/usr/bin/env python

import os


def where():
    """
    Return the installation location of BrewData
    """
    f = os.path.split(__file__)[0]
    return os.path.abspath(os.path.join(f, '..'))


if __name__ == '__main__':
    print(where())
