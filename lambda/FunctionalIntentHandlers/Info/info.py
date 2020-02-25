"""Info module

This file is imported as a module and contains the following
function:

    * info - returns the requested information about Space/X and the API

"""

# based on a module originally coded for SpacePY-X

from utilities import convert_date_to_speech, getJson

def info(timeOut=1,units="miles",task="api-version",parameter="None"):
    """

    :type timeOut: Optional[int]

    Returns details about the company and the API

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


    API_result = getJson(timeOut,"")
    COMPANY_result = getJson(timeOut,"info")
    
    # API Version
    if (task == "api-version"):
        R = API_result['version']
        
    # Company Info
    if (task == "company"):
        R = COMPANY_result    
    
    return R
    
    