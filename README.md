# Template Usage

Replace scrapername everywhere with your scraper's name eg. worldbank
Replace ScraperName everywhere with your scraper's name eg. World Bank
Look for xxx and ... and replace add text accordingly.

## Testing

Scrapers can be tested locally in a Python virtualenv which can be set up by running
./setup.sh and run with ./run.sh. It is recommended to set up 
[Travis](https://travis-ci.com/) for running tests on check in (using the Travis website's
simple UI) and to set up [coveralls](https://coveralls.io/) for ensuring that tests
cover the majority of your code.

## Deployment

Scrapers can either be installed on GitHub Actions or Jenkins. In either case, they can be 
set up to run on a schedule. For scripts that run for more than 6 hours and/or for which
resuming failed runs in important, Jenkins must be used.

### GitHub Actions 
Uses the .github/workflows/python-package.yml file. Set up the environment variables to be 
passed to your script in that file mapping them from secrets configured in the GitHub 
repository's UI. You can also set up the cron schedule.
(The files listed under Jenkins below are not used.)

### Jenkins
docker-compose.yml, docker-requirements.yml, Dockerfile, run-dev.sh, run-once-dev.sh and run_env
are only needed for Jenkins. (.github/workflows/python-package.yml is not used.) 

For a full scraper following this template for GitHub Actions see:
[OAD](https://github.com/OCHA-DAP/hdx-scraper-covid-viz)

For full scrapers following this template for Jenkins see:
[ACLED](https://github.com/OCHA-DAP/hdx-scraper-acled-africa),
[FTS](https://github.com/OCHA-DAP/hdx-scraper-fts),
[WHO](https://github.com/OCHA-DAP/hdx-scraper-who),
[World Bank](https://github.com/OCHA-DAP/hdx-scraper-worldbank),
[WorldPop](https://github.com/OCHA-DAP/hdx-scraper-worldpop)

For a scraper that also creates datasets disaggregated by indicator (not just country) and
reads metadata from a Google spreadsheet exported as csv, see:
[IDMC](https://github.com/OCHA-DAP/hdxscraper-idmc)

## Text for Scraper's README.md below

### Collector for ScraperName's Datasets
[![Build Status](https://travis-ci.org/OCHA-DAP/hdxscraper-scrapername.svg?branch=master&ts=1)](https://travis-ci.org/OCHA-DAP/hdxscraper-scrapername) [![Coverage Status](https://coveralls.io/repos/github/OCHA-DAP/hdxscraper-scrapername/badge.svg?branch=master&ts=1)](https://coveralls.io/github/OCHA-DAP/hdxscraper-scrapername?branch=master)

Collector designed to collect ScraperName datasets from the [ScraperName](http://) website 
and to automatically register datasets on the 
[Humanitarian Data Exchange](http://data.humdata.org/) project.

### Usage
python run.py

For the script to run, you will need to either pass in your HDX API key as a parameter or have a file called .hdx_configuration.yml in your home directory containing your HDX key eg.

    hdx_key: "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX"
    hdx_read_only: false
    hdx_site: test
    
 You will also need to pass in your user agent as a parameter or pass a parameter *user_agent_config_yaml* specifying where your user agent file is located. It should be of the form:
 
    user_agent: MY_USER_AGENT
    
 If you have many user agents, you can create a file of this form, put its location in *user_agent_config_yaml* and specify the lookup in *user_agent_lookup*:
 
    myscraper:
        user_agent: MY_USER_AGENT
    myscraper2:
        user_agent: MY_USER_AGENT2

 Note for HDX scrapers: there is a universal .useragents.yml file you should use.

 Alternatively, you can set up environment variables eg. for production runs: USER_AGENT, HDX_KEY, HDX_SITE, BASIC_AUTH, EXTRA_PARAMS, TEMP_DIR, LOG_FILE_ONLY