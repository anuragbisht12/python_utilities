# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 22:07:50 2020

@author: anurag
"""
from pprint import pprint

def get_drive_time(apiKey, origin, destination):
    """
    Returns the driving time between using the Google Maps Distance Matrix API. 
    API: https://developers.google.com/maps/documentation/distance-matrix/start
    https://maps.googleapis.com/maps/api/distancematrix/json?origins=28.482401,77.086267&destinations=28.599947,77.227308&key=AIzaSyAuFVEys52izKZr1IQgfe26g8J3vzO-WiE
    # INPUT -------------------------------------------------------------------
    apiKey                  [str]
    origin                  [str]
    destination             [str]
    # RETURN ------------------------------------------------------------------
    drive_tim               [float] (minutes)
    """
    import requests
    url = ('https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={}&destinations={}&key={}'
           .format(origin.replace(' ','+'),
                   destination.replace(' ','+'),
                   apiKey
                  )
          )
    try:
        response = requests.get(url)
        resp_json_payload = response.json()
        drive_time = resp_json_payload['rows'][0]['elements'][0]['duration']['value']/60
        pprint(drive_time)
    except:
        print('ERROR: {}, {}'.format(origin, destination))
        drive_time = 0
    return drive_time


if __name__ == '__main__':
    # get key
    fname = r'GoogleMapsKey.txt'
    file  = open(fname, 'r')
    apiKey = file.read()
    print(apiKey)
 
    # get coordinates 
    origin = '1 Rocket Road, Hawthorne, CA'
    destination = '1 Rocket Road, McGregor, TX'
    drive_time = get_drive_time(apiKey, origin, destination)
#    print('Origin:      {}\nDestination: {}\nDrive Time:  {} hr'.format(origin, destination, drive_time/60))
