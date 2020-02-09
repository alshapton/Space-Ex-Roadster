"""Launches module

This file is imported as a module and contains the following
function:

    * launches - returns the requested information about the launches

"""

# based on a module originally coded for SpacePY-X


import inflect
import json
import requests

from utilities import convert_date_to_speech, num_to_month, get_image
from FunctionalIntentHandlers.Ships.ships import ships
from FunctionalIntentHandlers.LandingPads.landingpads import landingpads

def cores(result):
    return len(result['rocket']['first_stage']['cores'])

def cores_landed(result):
    R=[]
    listofpads = json.loads(json.dumps(landingpads(1,"","getLandingPadsList","")))
    for core in result['rocket']['first_stage']['cores']:
        this_lv = core['landing_vehicle']
        s_name = ''
        for lv in listofpads:
            if (lv["id"] == core['landing_vehicle']):
                if (lv["landing_type"]=="ASDS"):
                    s_name = " the drone ship "
                else:
                    s_name = " at the landing zone "
                s_name   = s_name + lv["full_name"]
                
        if (core['land_success']):
            R.append('YES' + ':' + s_name )
        else:
            R.append('NO' + ':'  + s_name )
            
    return R

def core_reuse(result):
    c_reused = 0
    c_new    = 0
    for core in result['rocket']['first_stage']['cores']:
        if (core['reused']):
            c_reused = c_reused + 1
        else:
            c_new    = c_new + 1
    return str(c_reused) + ":" + str(c_new)

def rocket(result):
    return result['rocket']['rocket_name']

def launches(result="",timeOut=1,units="miles",task="none",parameter="none"):
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
    
    # Get instance of the number to words engine
    p = inflect.engine()

        
    # Previous Launch
    if (task == "last-long"):
        
        SPEECH = "The last launch was for the " + result['mission_name'] + " mission, on  " + convert_date_to_speech(result['launch_date_utc'],"long") + "."
        droneshipslist=ships(1,"","getDroneShipsList","")
        
        SPEECH=SPEECH + " It was launched by a " + rocket(result) + "  rocket,"
        
        core_speech =  " and had " 
        
        cores_used = core_reuse(result).split(":")
        core_speech_r = ""
        core_speech_n = ""
        
        if (int(cores_used[0]) > 0):
            core_speech_r = cores_used[0] + " reused " + p.plural("core",int(cores_used[0]))  
            core_speech = core_speech + core_speech_r
            if (int(cores_used[1]) >0):
                core_speech = core_speech + " and "
                
        if (int(cores_used[1]) >0):
            core_speech_n = cores_used[1] + " new " + p.plural("core",int(cores_used[1]))  
            core_speech = core_speech + core_speech_n
            
        
        if (result['rocket']['first_stage']['cores']):
            core_speech = core_speech + ". "
            cores_down = cores_landed(result)
            core_count = 0
            for core_down in cores_down:
                core_count = core_count + 1
                coreinfo  = core_down.split(":")
                core_status   = coreinfo[0]
                landing_vehicle = coreinfo[1]
                if (core_status == "YES"):
                    core_speech = core_speech + "Core " + str(core_count) + " landed successfully " + coreinfo[1] + "."
                else:
                    core_speech = core_speech + "Core " + str(core_count) + " did not land on its target of  " + cooreinfo[1] + "."
                
        RET = SPEECH + core_speech
        
    if (task == "next-long"):
        
        SPEECH = "The next launch is for the " + result['mission_name'] + " mission, on  " + convert_date_to_speech(result['launch_date_utc'],"long")
        listofpads = json.loads(json.dumps(landingpads(1,"","getLandingPadsList","")))
        
        details = result['details']
        
        for lv in listofpads:
            s_name = ''
            if (lv["landing_type"]=="ASDS"):
                s_name = " the drone ship "
            else:
                s_name = " the landing zone "
            s_name   = s_name + lv["full_name"]
            details   = details.replace(lv["id"],"," + s_name)

        SPEECH = SPEECH + ". " + details + ". "
        
        SPEECH=SPEECH + " It'll be launched by a " + rocket(result) + "  rocket,"
        
        core_speech =  " and will have " 
        
        cores_used = core_reuse(result).split(":")
        core_speech_r = ""
        core_speech_n = ""
        
        if (int(cores_used[0]) > 0):
            core_speech_r = cores_used[0] + " reused " + p.plural("core",int(cores_used[0]))  
            core_speech = core_speech + core_speech_r
            if (int(cores_used[1]) >0):
                core_speech = core_speech + " and "
                
        if (int(cores_used[1]) >0):
            core_speech = cores_used[1] + " new " + p.plural("core",int(cores_used[1]))  
        
        RET = SPEECH + core_speech
    
    # Next launch date (short form)
    if (task == "next-date-short"):
        if (parameter == "speech"):
            RET = convert_date_to_speech(result['launch_date_utc'],"short")
        if (parameter == "text"):
            longlaunchdateutc = result['launch_date_utc']
            launchyear  = longlaunchdateutc[0:4]
            launchmonth = num_to_month(int(longlaunchdateutc[6:7]))
            launchday   = p.ordinal(int(longlaunchdateutc[8:10]))
            launchhour  = longlaunchdateutc[11:13]
            launchmin  =  longlaunchdateutc[14:16]

            RET = launchday + " of " + launchmonth + " " + launchyear + " at " + launchhour + ":" + launchmin + " UTC"
        
    # retrieve launch images
    if (task == "image"):
        RET = get_image(result,parameter)  
        
    return RET
    
    