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

from utilities import km_to_au,mi_to_au,au_to_mi,km_to_au, \
num_to_month,convert_date_to_speech

# https://space.stackexchange.com/questions/13825/how-to-obtain-utc-of-the-epoch-time-in-a-satellite-tle-two-line-element
# Convert epoch_jd to UTC

def roadster(timeOut=1,units="miles",task="distance"):
    """

    :type timeOut: Optional[int]

    Returns details about the Tesla Model 3 Roadster

    Parameters
    ----------

    timeOut : time out in seconds

    Returns 
    -------
    a string in speech format containing details of the Tesla Model 3
        Roadster, including position, speed etc
    """

    result = getJson(1,"roadster")
    SPEECH = "Sorry, I couldnt understand what you need me to do, maybe you could try again?"
    # Get instance of the number to words engine
    p = inflect.engine()

    # Distance from Earth
    if (task == "distance"):
        # Get appropriate distance depending on units
        if (str(units) == "None"):
            units="Miles"
        if units.lower() == "kilometers":
            dist=int(float(result['mars_distance_km']))
        if units.lower() == "miles":
            dist=int(float(result['mars_distance_mi']))
        distance_away = p.number_to_words(dist)
        SPEECH = distance_away + " " + str(units) + " away from Earth."
        
    # Distance from Mars
    if (task == "mars"):
        # Get appropriate distance depending on units
        if (str(units) == "None"):
            units="Miles"
        if units.lower() == "kilometers":
            dist=int(float(result['earth_distance_km']))
        if units.lower() == "miles":
            dist=int(float(result['earth_distance_mi']))
        distance_away = p.number_to_words(dist)
        SPEECH = distance_away + " " + str(units) + " away from Mars."
    
    # Travelling speed
    if (task == "speed"):
        # Get appropriate speed depending on units
        if (str(units) == "None"):
            units="Miles"
        if units.lower() == "kilometers":
            speed=int(float(result['speed_kph']))
        if units.lower() == "miles":
            speed=int(float(result['speed_mph']))
        fast = p.number_to_words(speed)
        SPEECH = fast + " " + str(units) + " per hour"
    
    # orbit details
    if (task == "orbit"):
        # Get appropriate speed depending on units
        if (str(units) == "None"):
            units="Miles"
        if units.lower() == "kilometers":
            speed=int(float(result['speed_kph']))
        if units.lower() == "miles":
            speed=int(float(result['speed_mph']))
        orbit_type = result['orbit_type']
        period=int(float(result['period_days']))
        fast = p.number_to_words(speed)
        SPEECH = " a " + orbit_type + " orbit, is travelling at " + fast + " " + str(units) + " per hour,,"
        SPEECH = SPEECH + "It has a period of " + p.number_to_words(period) + " days."
    
    # roadster details
    if (task == "details"):
        # Get the textual description
        SPEECH = result['details']

    # apoapsis
    if (task == "apoapsis_au"):
        # Get the apoapsis in AU
        SPEECH = p.number_to_words(str(result['apoapsis_au']),group=1).replace(","," ")

    # periapsis
    if (task == "periapsis_au"):
        # Get the periapsis in AU
        SPEECH = p.number_to_words(str(result['periapsis_au']),group=1).replace(","," ")

    # Periapsis Argument
    if (task == "periapsis_arg"):
        # Get the periapsis argument
        SPEECH = p.number_to_words(str(result['periapsis_arg']),group=1).replace(","," ")

     # Semi-major axis
    if (task == "semi_major_axis"):
        # Get the semi major axis in AU
        SPEECH = p.number_to_words(str(result['semi_major_axis_au']),group=1).replace(","," ")

    # Eccentricity
    if (task == "eccentricity"):
        # Get the orbital eccentricity
        SPEECH = p.number_to_words(str(result['eccentricity']),group=1).replace(","," ")

    # Inclination
    if (task == "inclination"):
        # Get the orbital inclination
        SPEECH = p.number_to_words(str(result['inclination']),group=1).replace(","," ")

    # Longitude
    if (task == "longitude"):
        # Get the longitude of the ascending node
        SPEECH = p.number_to_words(str(result['longitude']),group=1).replace(","," ")



    # NORAD ID
    if (task == "norad"):
        # Get the textual description
        SPEECH = p.number_to_words(int(str(result['norad_id'])), group=1).replace(","," ")
        
    # roadster name
    if (task == "name"):
        # Get the textual description of the name
        SPEECH = result['name']
        
    # roadster launch date information
    # Get complete launch date and time
    if (task == "launch-long"):
        SPEECH=convert_date_to_speech(result['launch_date_utc'],"long")

    if (task == "launch-short"):
    # Get launch date
        SPEECH=convert_date_to_speech(result['launch_date_utc'],"short")

        
    if (task == "mass"):
    # Get its' launch weights
        masskg =  p.number_to_words(int(result['launch_mass_kg']))
        masslbs = p.number_to_words(int(result['launch_mass_lbs']))        
        
        SPEECH = "Its launch weight was " + masskg + " kilograms, or " + masslbs + " pounds"
    
    
    return SPEECH
    
    