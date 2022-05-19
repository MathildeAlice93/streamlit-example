import os
from os import listdir
from os.path import isfile, join
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By  # the By implementation
from parsel import Selector
import datetime
import re

# FUNCTION: "test"
# CREATED: "YYYY-MM-DD"
# PURPOSE: testing things
# INPUT: arguments
# OUTPUT: other arguments
# CONTEXT: testing
# LIBRARIES: required libraries


def test():
    print('Hello, World of M!')

# FUNCTION: "create_folder"
# CREATED: "2022-05-??"
# PURPOSE: Creating a folder if not existing
# INPUT: directory (path + filename)
# OUTPUT: -
# CONTEXT: Created to facilitate folder creation
# LIBRARIES: os libraries


def create_folder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# FUNCTION: "read_data_as_df_giving_header"
# CREATED: "2022-05-??"
# PURPOSE: Reading a csv as a df
# INPUT: file, header
# OUTPUT: df
# CONTEXT: Created to be able to catch errors
# LIBRARIES: pandas


def read_data_as_df_giving_header(file, header):
    print('in read_data_func')
    try:
        df = pd.read_csv(file, header=None, names=header)
        return df
    except EmptyDataError:
        df = pd.DataFrame()

# FUNCTION: "list_unprocessed_files_in_directory"
# CREATED: "2022-05-??"
# PURPOSE: Listing unmarked files within a path
# INPUT: path, marker
# OUTPUT: list
# CONTEXT: Initially used to fetch files of which content was not saved
# LIBRARIES: os libraries


def list_unprocessed_files_in_directory(path, marker):
    list_of_files_in_path = [f for f in listdir(path) if isfile(join(path, f))]
    list_of_unprocessed_files = []
    for file in list_of_files_in_path:
        splitted_file = file.split(".")
        filename = splitted_file[0]
        if not filename.endswith(marker):
            list_of_unprocessed_files.append(filename)
    return list_of_unprocessed_files

# FUNCTION: "catch_xpath_in_url_returning_list"
# CREATED: "2022-05-18"
# PURPOSE: Searching xpath within url to return a list of matches
# INPUT: url, xpath
# OUTPUT: list
# CONTEXT: Initially used to fetch url's of new properties
# LIBRARIES : selenium libraries and parsel


def catch_xpath_in_url_returning_list(url, xpath):
    chrome_options = Options()  # req: import Options from chrome.options
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')

    # To prevent image loading and improve performance
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)  # .Chrome is a class

    # driver.implicitly_wait(10)

    driver.get(url)  # .get is a method

    sel = Selector(text=driver.page_source)  # req: import Selector

    fetch_items_list = sel.xpath(xpath).extract()  # xpath comes from By implmt

    return fetch_items_list

# FUNCTION: "give_current_timestamp_formatted"
# CREATED: "2022-05-18"
# PURPOSE: Giving the current timestamp in the desired format
# INPUT: desired format, correction factor for timezones (default value being zero)
# OUTPUT: formatted timestamp
# CONTEXT: Initially used to name files
# LIBRARIES : datetime library


def give_current_timestamp_formatted(desired_format, hours_delta=0):

    # catch current datetime in a variable
    naive_datetime = datetime.datetime.now()

    # correct for timezone and format for filename and folder name
    time_delta = datetime.timedelta(hours=hours_delta)
    run_timestamp = naive_datetime + time_delta
    timestamp_formatted = run_timestamp.strftime(desired_format)

    return timestamp_formatted

# !!! NOT WORKING !!!
# FUNCTION: "find_regex_in_text"
# CREATED: "2022-05-18"
# PURPOSE: Renders first match for a given regex
# INPUT: regex
# OUTPUT: first match
# CONTEXT: Initially used to extract data from immoweb url's
# LIBRARIES : re library


def find_regex_in_text(regex, url):
    matches = re.findall(rf"{regex}", url)
    for match in matches:
        match = match
        break
    return match
