import requests
from datetime import datetime # Used to convert epoch time in seconds to a human readable iso formatted string.

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

###########################################################################################
#### EXAMPLE 2: Amazon product identification using Amazon Stock Identification Number (ASIN)

amazon_base_url                    = 'https://www.amazon.com/'
amazon_product_page_endpoint       = amazon_base_url + 'dp/'
ASIN_Samsung_SSD = 'B07BN217QG' # Concat id number (a.k.a. ASIN) for Samsung Solid State Drive

amazon_solid_state_harddrive_url   = amazon_product_page_endpoint + ASIN_Samsung_SSD
print(amazon_solid_state_harddrive_url)

amazon_competitive_offers_endpoint              = amazon_base_url + "gp/offer-listing/"
amazon_competitive_offers_with_filter_query_url = amazon_competitive_offers_endpoint + ASIN_Samsung_SSD + "?condition=new"
print(amazon_competitive_offers_with_filter_query_url)
