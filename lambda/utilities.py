"""utilities module

This file is imported as a module and exposes the following
functions:

    * km_to_au      - converts kilometers to AU
    * mi_to_au      - converts miles to AU
    * au_to_km      - converts AU to kilometers 
    * au_to_mi      - converts AU to miles
    * num_to_month  - converts a month number into the text equivalent
    * get_image     - returns the specified image from the JSON result
    * convert_date_to_speech - Takes a date and converts it into a long or short version ready for speech
    * getJson       - takes a REST endpoint and returns the result (respecting any parameters) as a JSON payload    
    * getConfig     - reads the configuration file as a JSON payload
    * UTC_to_local  - converts a UTC time to a time in the user's timezone
    * getTimezone   - gets the user's device timezone (or defaults to UTC) and stores it in a session slot
    * get_locale    - gets the users's locale
    
"""
import inflect
import requests
import json
from ask_sdk_model.intent_request import IntentRequest

# Calculating timezone-specific times from UTC
import pytz
from datetime import datetime
import tzlocal 

AU_KM = 149597871
AU_MI = 92955807

def km_to_au(km):
    return km / AU_KM  

def mi_to_au(mi):
    return mi / AU_MI

def au_to_km(au):
    return au * AU_KM  

def au_to_mi(au):
    return au * AU_MI  

def num_to_month(month):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return months[month-1] 

def get_image(result,data_item=""):
    IMAGE = ""
    
    if (data_item == "None"):
        return IMAGE 
    else:
        return eval("result" + data_item )

def convert_date_to_speech(longlaunchdateutc="No date",fmt="short",tz=""):
    p = inflect.engine()
    
    longlaunchdateutc=UTC_to_local(longlaunchdateutc,tz)
    
    if (longlaunchdateutc == "No date"):
        return longlaunchdateutc

    launchyear  = p.number_to_words(int(longlaunchdateutc[0:4]))
    launchmonth = num_to_month(int(longlaunchdateutc[6:7]))
    launchday   = p.ordinal(int(longlaunchdateutc[8:10]))
    
    launchhour  = p.number_to_words(int(longlaunchdateutc[11:13]))
    if (int(longlaunchdateutc[11:13]) < 10):
        launchhour = "oh " + launchhour
        
    launchmin  =  p.number_to_words(int(longlaunchdateutc[14:16]))
    if (int(longlaunchdateutc[14:16]) < 10):
        launchmin = "oh " + launchmin
    
    launchsec   = p.number_to_words(longlaunchdateutc[17:18])
    if (tz == "UTC"):
        launchtz    = "You Tee See"
    else:
        launchtz    = "local time"   
        
    if (fmt == "long"):
        # Long stuff 
        launchdatetime = launchday + " of " + launchmonth + " " + launchyear + " at " + launchhour + " " + launchmin + " hours and " + launchsec + " seconds " + launchtz
    
    if (fmt == "short"):
        # Short stuff 
        
        launchdatetime = launchday + " of " + launchmonth + " " + launchyear 
        
    return launchdatetime


def getJson(timeOut=1,url_segment=""):
    """ Base URL from which to assemble request URLs """
    base = "https://api.spacexdata.com"

    """ API Version """
    version = "v3"
    root_url = base + "/" + version + "/"

    result = json.loads(json.dumps(requests.get(url = str(root_url + url_segment),timeout = timeOut).json()))
    return result

def getTimezone(handler_input):
    
    try:
        userTimeZone = handler_input.attributes_manager.session_attributes["TimeZone"]
    except Exception:
        userTimeZone = "UNDEFINED"
    
    if (userTimeZone == "UNDEFINED"):
        # get device id
        sys_object = handler_input.request_envelope.context.system
        device_id = sys_object.device.device_id
        
        # get Alexa Settings API information
        api_endpoint = sys_object.api_endpoint
        api_access_token = sys_object.api_access_token
        
        # construct systems api timezone url
        url = '{api_endpoint}/v2/devices/{device_id}/settings/System.timeZone'.format(api_endpoint=api_endpoint, device_id=device_id)
        headers = {'Authorization': 'Bearer ' + api_access_token}
        
        userTimeZone = ""
        try:
            r = requests.get(url, headers=headers)
            res = r.json()
            #logger.info("Device API result: {}".format(str(res)))
            userTimeZone = str(res)
        except Exception:
            userTimeZone="UTC"
        
    return userTimeZone

def getConfig():
    with open('config.json') as json_file:
        return json.load(json_file)


def UTC_to_local(t,userTimeZone):
    # format of t is 2010-12-08T15:43:00.000Z
    
    if (t == ""):
        return "unknown time"
    if (userTimeZone == "" or userTimeZone == "UTC" ):
        return str(t) + "UTC"
    
    utc=datetime.strptime(t,'%Y-%m-%dT%H:%M:%S.000Z')
    utc_timezone = pytz.timezone("UTC")

    # returns datetime in the new timezone
    local_time = utc_timezone.localize(utc).astimezone(pytz.timezone(userTimeZone)) 
    return local_time

def get_locale(handler_input):
    # type: (HandlerInput) -> AnyStr
    #Return locale value from input request.
    return handler_input.request_envelope.request.locale
    