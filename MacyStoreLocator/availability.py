__author__ = 'amith tudur'
"""
description: Given a zipcode and a Macy.com OfferURL, shows the 8 closest stores and the product availability.
parameters: Zipcode OfferURL Size(optional) Color(optional)
requires: python 2.7.2
"""
import urllib
import urllib2
import json
import sys
import os
import re
from urlparse import urlparse,parse_qs

def show_availability(zip_code,
                     offer_url,
                     size,
                     color):
    '''
    -parses the page source of Macy.com to get the UPCId of the product
    -calls the Macy's server with the productID, zipCode and upcID
    -parses the response JSON and displays the result
    '''
    req_source = urllib2.Request(offer_url)
    page_source = urllib2.urlopen(req_source).read()
    ####
    # search for string of the form "upc": '123456'
    ##########
    try:
        upc  = re.search('\"upc\":\s*(?P<upc_id>\'\d+\')', page_source)
        upc_id = upc.group('upc_id')
    except IndexError, (e):
        print "error parsing: failed to get the UPC ID of the product. Probably macys.com changed the source for HTML?"
        exit(1)
    except AttributeError, (e):
        print "Sorry! This product is unavailable."
        exit(1)

    product_id = parse_qs(urlparse(offer_url).query)["ID"]
    ####
    #url - does the magic and gives us the required results
    ##########
    url = "http://www.macys.com/store/storeavailability/index.ognc"
    values = { "size" : size,
               "color" : color,
               "type" : "none",
               "zipCode" : int(zip_code),
               "city" : "",
               "state" : "NOSELECTION",
               "productID": product_id,
               "upcID" : upc_id
    }
    data = urllib.urlencode(values)
    req = urllib2.Request(url,
                          data
                    )
    store_avail = urllib2.urlopen(req).read()
    availability = json.loads(store_avail)
    try:
        for stores in availability['inStoreAvailabilityVB']['searchResults']:
            print "\n%s\n%s/ %s, %s %s\n%s" % (stores["storeName"],
                                             stores["addressVB"]["address1"].rstrip(),
                                             stores["addressVB"]["city"].rstrip(),
                                             stores["addressVB"]["state"],
                                             stores["addressVB"]["zipCode"],
                                             stores["availabilityStatus"].upper())
    except KeyError, e:
        print "error is store availability - key not found: %s \nresponse received: %s" % (e, the_page)


if __name__ == "__main__":
    try:
        zipCode = sys.argv[1]
        offerUrl = sys.argv[2]
        size = sys.argv[3] if len(sys.argv) > 3 else "none"
        color = sys.argv[4] if len(sys.argv) > 4 else "No Color"
    except IndexError, e:
        print "Usage: ./%s <zipcode> <offer_url> [size [color]]" % (os.path.basename(sys.argv[0]))
        exit(1)

    show_availability(zipCode,
                     offerUrl,
                     size,
                     color)
