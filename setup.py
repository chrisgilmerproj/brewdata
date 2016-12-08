from setuptools import find_packages
from setuptools import setup


VERSION = '0.0.1'

setup(
    name='brewdata',
    version=VERSION,
    author='Chris Gilmer',
    author_email='chris.gilmer@gmail.com',
    maintainer='Chris Gilmer',
    maintainer_email='chris.gilmer@gmail.com',
    license="MIT",
    description='Brew Data',
    url='https://github.com/chrisgilmerproj/brewdata',
    download_url='https://github.com/chrisgilmerproj/brewdata/tarball/{}'.format(VERSION),  # nopep8
    packages=find_packages(exclude=["scraper*",
                                    "*.tests",
                                    "*.tests.*",
                                    "tests.*",
                                    "tests"]),
    package_data={
        'brewdata': ['*/*.json'],
    },
    include_package_data=True,
    zip_safe=True,
    keywords='brew brewing beer grain hops yeast',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
