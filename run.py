#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Top level script. Calls other functions that generate datasets that this script then creates in HDX.

"""
import logging
from os.path import join, expanduser

from hdx.hdx_configuration import Configuration
from hdx.utilities.downloader import Download
from hdx.utilities.path import temp_dir, progress_storing_tempdir

from scrapername import generate_dataset_and_showcase, get_countries

from hdx.facades.simple import facade

logger = logging.getLogger(__name__)


# HDX only
# lookup = "hdx-scraper-scrapername"


def main():
    """Generate dataset and create it in HDX"""

    # Get temporary folder for any intermediate files
    # (uses either where TEMP_DIR env var points if it exists or os.gettempdir() and appends scrapername)
    # with temp_dir("scrapername") as folder:
    # If website being scraped requires username and password, you can supply one in a file in your home directory.
    # The file should contain username:password based64 encoded. Remember to create it on the server eg. ScraperWiki box!
    # If you need to add extra parameters to every url, you can use extra_params_yaml and point to a YAML file with
    # key value pairs. Remember to create it on the server!
    with Download(basic_auth_file=join(expanduser("~"), ".scrapernamefile"),
                  extra_params_yaml=join(expanduser("~"), "scrapernamefile.yaml")) as downloader:
        base_url = Configuration.read()["base_url"]
        countries = get_countries(base_url, downloader)
        logger.info(f"Number of datasets to upload: {len(countries)}")
        # Loops storing state in folder for resuming broken runs. Also creates batch code for the set of datasets
        # and temporary folder.
        for info, country in progress_storing_tempdir("scrapername", countries, "iso3"):
        # A simple loop can be used instead
        # for country in countries:
            dataset, showcase = generate_dataset_and_showcase(base_url, downloader, info["folder"], country)
            if dataset:
                dataset.update_from_yaml()
                dataset.create_in_hdx(remove_additional_resources=True, hxl_update=False, updated_by_script="HDX Scraper: ScraperName", batch=info["batch"])
                dataset.generate_resource_view()
                showcase.create_in_hdx()
                showcase.add_dataset(dataset)


if __name__ == "__main__":
    facade(main, hdx_site="stage", hdx_key="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx", user_agent="myorgandproject", project_config_yaml=join("config", "project_configuration.yaml"))
    # HDX: Remember to create .hdx_configuration.yaml on your server eg. the ScraperWiki box!
    # HDX: Use facade below creating or adding to .useragents.yaml a key (hdxscraper-scrapername) with a Dict as
    # a value, the Dict containing user agent entries.
    # HDX: It is best to use the HDX Data Team bot"s key (https://data.humdata.org/user/luiscape) rather than your own.
    # HDX: That file should have a user_agent parameter and an additional one identifying the scraper as internal to HDX.
    # facade(main, user_agent_config_yaml=join(expanduser("~"), ".useragents.yaml"), user_agent_lookup=lookup, project_config_yaml=join("config", "project_configuration.yaml"))


