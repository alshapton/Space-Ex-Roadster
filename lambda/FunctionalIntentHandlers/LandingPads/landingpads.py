"""Landingpads module

This file is imported as a module and contains the following
function:

    * landingpads - returns the requested information about the available Space/X landing pads
    
        task == "name"                  - returns the name of the landingpad given the id
        task == "getLandingPadsList"    - returns a list of landing pads with all their information as an array of JSON documents

"""

# based on a module originally coded for SpacePY-X

import json
import requests
import inflect

from utilities import convert_date_to_speech, getJson

def landingpads(timeOut=1,units="miles",task="name",parameter="None"):
    """

    :type timeOut: Optional[int]

    Returns details about the Landing pads available

    Parameters
    ----------

    timeOut : time out in seconds

    Returns 
    -------
    a string in speech format containing details of the information requested
    OR 
    a JSON String
    OR
    a List
    OR 
    a String
    """

    
    # Get instance of the number to words engine
    p = inflect.engine()

    # landingpad Names
    if (task == "name"):
        
        result = getJson(timeOut,"landpads/" + parameter)
        R = result['full_name']
        
    if (task == "getLandingPadsList"):
        result = getJson(timeOut,"landpads")
        R=[]
        for i in result:
            R.append(i)
        
    return R
    
    