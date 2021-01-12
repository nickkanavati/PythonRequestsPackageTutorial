import requests
from datetime import datetime # Used to convert epoch time in seconds to a human readable iso formatted string.
###########################
#### COINSTATS.APP API ####

###########################################################################################
#### EXAMPLE 1: COIN STATS APP API (https://coinstats.app/, https://apidocs.coinstats.app/)
coinstatsapp_base_url      = 'https://api.coinstats.app/public/v1/'
coinstatsapp_news_endpoint = coinstatsapp_base_url + 'news'

coinstatsapp_url = coinstatsapp_news_endpoint + "?skip=0&limit=10"
response = requests.get(coinstatsapp_url)

textdata = response.text
jsondata = response.json()

# Print results
entryNumber = 1
for entry in jsondata['news']:
    epoch_time_seconds = entry['feedDate'] / 1000 # https://www.epochconverter.com/
    isoformatedDateTime = datetime.fromtimestamp(epoch_time_seconds).isoformat()
    # print('\n{:>2}.  {:23}{:50}'.format(entryNumber, isoformatedDateTime, entry['title']))
    print('\n{:>2}.  {:23}'.format(entryNumber, isoformatedDateTime))
    entryNumber += 1
    for key in entry.keys():
        print('\t{:30}{:60}'.format(key, str(entry[key])))

####################
#### AMAZON.COM ####
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0',
    'Accept':  'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.5',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Host': 'www.amazon.com',
    'Pragma': 'no-cache'
}
###########################################################################################
#### EXAMPLE 2: Amazon product identification using Amazon Stock Identification Number (ASIN)

amazon_base_url                    = 'https://www.amazon.com/'
amazon_product_page_endpoint       = amazon_base_url + 'dp/'
ASIN_Samsung_SSD = 'B07BN217QG' # Concat id number (a.k.a. ASIN) for Samsung Solid State Drive

amazon_solid_state_harddrive_url   = amazon_product_page_endpoint + ASIN_Samsung_SSD
print(amazon_solid_state_harddrive_url)
data_amazon_product_information = requests.get(amazon_solid_state_harddrive_url)
data_amazon_product_information.status_code
data_amazon_product_information.reason
data_amazon_product_information.text

data_amazon_product_information = requests.get(amazon_solid_state_harddrive_url, headers=headers)
data_amazon_product_information.status_code
data_amazon_product_information.reason
data_amazon_product_information.text

amazon_competitive_offers_endpoint              = amazon_base_url + "gp/offer-listing/"
amazon_competitive_offers_with_filter_query_url = amazon_competitive_offers_endpoint + ASIN_Samsung_SSD + "?condition=new"
print(amazon_competitive_offers_with_filter_query_url)

data_amazon_competitive_offers = requests.get(amazon_competitive_offers_with_filter_query_url)


data_amazon_competitive_offers = requests.get(amazon_competitive_offers_with_filter_query_url, headers=headers)
data_amazon_competitive_offers.status_code
data_amazon_competitive_offers.reason


