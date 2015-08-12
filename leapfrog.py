#! /usr/bin/env python

import urllib2
import json


def apiExample():
    """Proff of Concept for getting data from an API"""
    Client_ID = '5b42d8679569faa6e359a3f562e8cd76'
    api_endpoint = "http://api.soundcloud.com/tracks/13158665?client_id=%s" \
                   % Client_ID
    request = urllib2.urlopen(api_endpoint)
    data = json.load(request)
    return data


def leapfrogAPI(income=0, zipcode=0, age=0):
    """This uses a ficticious API endpoint"""

    api_endpoint = "http://not_real.com/customer_scoring?income=%s" \
                   "&zipcode=%s&age=%s" % (income, zipcode, age)

    try:
        request = urllib2.urlopen(api_endpoint)
        data = json.load(request)
    except urllib2.URLError:
        data = {
            "status": 'URL Error',
            "propensity": 0.26532,
            "ranking": "C"
        }

    try:
        int(income)
        int(zipcode)
        int(age)
    except ValueError:
        data['status'] = 'Value Error'

    return data

if __name__ == '__main__':
    apiExample()
