"""Roadster module

This is a module which allows wrapper access to information about Elon
Musk's Tesla Model 3 Roadster which is now an artificial satellite of
the Sun.

This file is imported as a module and contains the following
function:

    * roadster - returns all roadster information

"""

# based on a module originally coded for SpacePY-X

import requests
import json
import inflect


def roadster(timeOut=1,units="miles"):
    """

    :type timeOut: Optional[int]

    Returns details about the Tesla Model 3 Roadster

    Parameters
    ----------

    timeOut : time out in seconds

    Returns 
    -------
    a string in JSON format containing details of the Tesla Model 3
        Roadster, including position, speed etc
    """
    
    """ Base URL from which to assemble request URLs """
    base = "https://api.spacexdata.com"

    """ API Version """
    version = "v3"
    roadster_url = base + "/" + version + "/roadster"
    result = json.loads(json.dumps(requests.get(url = str(roadster_url),timeout = timeOut).json()))
    # Get appropriate distance depending on units
    if (str(units) == "None"):
        units="Miles"
    if units.lower() == "kilometers":
        dist=int(float(result['earth_distance_km']))
    if units.lower() == "miles":
        dist=int(float(result['earth_distance_mi']))
    p = inflect.engine()
    distance_away = p.number_to_words(dist)
    return "The roadster is " + distance_away + " " + str(units) + " away from Earth"
