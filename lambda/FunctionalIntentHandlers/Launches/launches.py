"""Launches module

This file is imported as a module and contains the following
function:

    * launches - returns the requested information about the launches

"""

# based on a module originally coded for SpacePY-X


import inflect
import json
import requests

from utilities import convert_date_to_speech
from FunctionalIntentHandlers.Ships.ships import ships


def cores(result):
    return len(result['rocket']['first_stage']['cores'])

def launches(timeOut=1,units="miles",task="distance"):
    """

    :type timeOut: Optional[int]

    Returns details about the Launches

    Parameters
    ----------

    timeOut : time out in seconds

    Returns 
    -------
    a string in speech format containing details of the information requested
    """
    
    """ Base URL from which to assemble request URLs """
    base = "https://api.spacexdata.com"

    """ API Version """
    version = "v3"
    root_url = base + "/" + version + "/launches/"
    # Get instance of the number to words engine
    p = inflect.engine()

    
    # Next Launch
    if (task == "next"):
        result = json.loads(json.dumps(requests.get(url = str(root_url+"next"),timeout = timeOut).json()))
        
        SPEECH = "The next launch is for the " + result['mission_name'] + " mission, on  " + convert_date_to_speech(result['launch_date_utc'],"long")
        SPEECH = SPEECH + ". " + result['details'] + ". "
        # SPEECH = SPEECH + ships(1,"","name","OCISLY")
        ccores = cores(result)
        SPEECH=SPEECH + "There will be " + str(ccores) + " " + p.plural("core", ccores)
        
        droneshipslist=ships(1,"","getDroneShipsList","")
        
        
    return SPEECH
    
    