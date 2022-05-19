#import utils
import https://raw.githubusercontent.com/MathildeAlice93/streamlit-example/master/utils.py
import csv
import re
import streamlit as st

property_types = ['house', 'apartment', 'garage']  # TODO: manage type issue

url = "https://www.immoweb.be/en/search/" + \
    property_types[0] + \
    "/for-sale/brussels/district?countries=BE&page=1&orderBy=newest"

# xpath for any URL value
xpath = '//*[@id="main-content"]/li//h2//a/@href'

page_houses_url = utils.catch_xpath_in_url_returning_list(url, xpath)

timestamp_formatted = utils.give_current_timestamp_formatted('%y%m%d%H%M%S')

# create folder and based on function in utils.py
utils.create_folder('./saved_data/list_of_new')
filename = 'saved_data/list_of_new/new_properties_' + timestamp_formatted + '.csv'

# open file
f = open(filename, 'w', newline='')
newest_properties = csv.writer(f)

# add a header
my_header = ['url', 'pc', 'id', 'property_type']
newest_properties.writerow(my_header)
# extract url, pc and id and write them down in folder
url_counter = 1
for url in page_houses_url:
    print("Scanned line ", url_counter, ": ", url)
    postcodes = re.findall(r'\/([\d]{4})\/', url)
    for postcode in postcodes:
        postcode = postcode
        break
    st.write("Extracted postcode: ", postcode)
    ids = re.findall(r'\/([\d]{7}?)', url)
    for id in ids:
        id = id
        break
    print("Extracted id: ", id)
    types = re.findall(
        r'https:\/\/www\.immoweb\.be\/en\/classified\/([a-z\-]*)\/', url)
    for type in types:
        type = type
        break
    # !!! NOT WORKING !!!
    #my_regex = "https:\/\/www\.immoweb\.be\/en\/classified\/([a-z\-]*)\/"
    #type = utils.find_regex_in_text(my_regex, url)
    print("Extracted type: ", type)
    house_info = [url, postcode, id, type]
    st.write(house_info)
    newest_properties.writerow(house_info)
    url_counter += 1
