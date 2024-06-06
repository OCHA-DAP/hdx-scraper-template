# Template Usage

Replace scrapername everywhere with your scraper's name eg. worldbank
Replace ScraperName everywhere with your scraper's name eg. World Bank
Look for xxx and ... and replace add text accordingly.

## Testing

Scrapers can be tested locally in a Python virtualenv which can be set up by running
./setup.sh and run with ./run.sh. 

## Deployment

Scrapers can either be installed on GitHub Actions or Jenkins. In either case, they can be 
set up to run on a schedule. For scripts that run for more than 6 hours and/or for which
resuming failed runs in important, Jenkins must be used.

### GitHub Actions 
Uses the .github/workflows/python-package.yaml file. Set up the environment variables to be 
passed to your script in that file mapping them from secrets configured in the GitHub 
repository's UI. You can also set up the cron schedule.
(The files listed under Jenkins below are not used.)

### Jenkins
docker-compose.yaml, docker-requirements.yaml, Dockerfile, run-dev.sh, run-once-dev.sh and run_env
are only needed for Jenkins. (.github/workflows/python-package.yaml is not used.) 

## Best Practices
It is highly recommended to have a README.md that details what your script does, from where it
obtains data, how to run it, what resources it uses (eg. CPU, memory, disk, network) and what 
environment variables are needed. An example is shown below the heading "Text for Scraper's 
README.md below" 

It is a good idea to set up GitHub Actions for running tests on check in 
(using the run-python-tests.yaml and the GitHub Actions UI to set up any secrets) and to set up [coveralls](https://coveralls.io/) 
in the website UI to ensure that tests cover the majority of your code.

It is very helpful to comment your code appropriately especially things that you think might
confuse someone looking at your code for the first time.

## Examples

For a full scraper following this template for GitHub Actions see:
[OAD](https://github.com/OCHA-DAP/hdx-scraper-scrapername)

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
[![Build Status](https://github.com/OCHA-DAP/hdx-scraper-scrapername/workflows/build/badge.svg)](https://github.com/OCHA-DAP/hdx-scraper-scrapername/actions?query=workflow%3Abuild) [![Coverage Status](https://coveralls.io/repos/github/OCHA-DAP/hdx-scraper-scrapername/badge.svg?branch=main&ts=1)](https://coveralls.io/github/OCHA-DAP/hdx-scraper-scrapername?branch=main)

Collector designed to collect ScraperName datasets from the [ScraperName](http://) website 
and to automatically register datasets on the 
[Humanitarian Data Exchange](http://data.humdata.org/) project.

### Usage
python run.py

For the script to run, you will need to either pass in your HDX API key as a parameter or have a file called .hdx_configuration.yaml in your home directory containing your HDX key eg.

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

 Note for HDX scrapers: there is a universal .useragents.yaml file you should use.

 Alternatively, you can set up environment variables eg. for production runs: USER_AGENT, HDX_KEY, HDX_SITE, BASIC_AUTH, EXTRA_PARAMS, TEMP_DIR, LOG_FILE_ONLY