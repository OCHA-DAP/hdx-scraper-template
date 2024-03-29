#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
SCRAPERNAME:
------------

Reads ScraperName JSON and creates datasets.

"""

import logging

from hdx.data.dataset import Dataset
from hdx.data.resource import Resource
from hdx.data.hdxobject import HDXError
from hdx.data.showcase import Showcase
from hdx.location.country import Country
from slugify import slugify

logger = logging.getLogger(__name__)


def get_countries(base_url, downloader):
    downloader.download(f"{base_url}folder/folder/xxx.xxx")
    jsonresponse = downloader.get_json()
    return jsonresponse["countries_key"]


def generate_dataset_and_showcase(base_url, downloader, folder, country):
    """Parse json of the form:
    {
    },
    """
    countryname = country["name"]
    title = "%s - Economic and Social Indicators" % countryname #  Example title. Include country, but not organisation name in title!
    logger.info("Creating dataset: %s" % title)
    name = "Organisation indicators for %s" % countryname  #  Example name which should be unique so can include organisation name and country
    slugified_name = slugify(name).lower()
    ...
    dataset = Dataset({
        "name": slugified_name,
        "title": title,
        ...
    })
    dataset.set_maintainer()
    dataset.set_organization()
    dataset.set_reference_period()
    dataset.set_expected_update_frequency()
    dataset.set_subnational()
    dataset.add_country_location()
    dataset.add_tags([])

    resource = Resource({
        "name": title,
        "url": ,
        "description":
    })
    resource.set_file_type("csv")  # set the file type to eg. csv
    dataset.add_update_resource(resource)

    showcase = Showcase({
        "name": "%s-showcase" % slugified_name,
        "title":
        "notes":
        "url":
        "image_url":
    })
    showcase.add_tags([])
    return dataset, showcase
