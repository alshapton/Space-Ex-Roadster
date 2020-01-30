"""Ships module

This file is imported as a module and contains the following
function:

    * ships - returns the requested information about the ships

"""

# based on a module originally coded for SpacePY-X

import json
import requests
import inflect

from utilities import convert_date_to_speech, getJson

def ships(timeOut=1,units="miles",task="distance",parameter="None"):
    """

    :type timeOut: Optional[int]

    Returns details about the Launches

    Parameters
    ----------

    timeOut : time out in seconds

    Returns 
    -------
    a string in speech format containing details of the information requested
    OR 
    a JSON String
    """

    
    # Get instance of the number to words engine
    p = inflect.engine()

    # Ship Name
    if (task == "name"):
        
        result = getJson(timeOut,"ships/" + parameter)
        R = result['ship_name']
        
    if (task == "getDroneShipsList"):
        result = getJson(timeOut,"ships?role=ASDS%20barge")
        R=[]
        for i in result:
            R.append(i['ship_id'] + ':' + i['ship_name'] )
        
    return R
    
    