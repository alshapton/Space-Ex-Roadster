"""Handlers for Landingpads 

This file is used to drive the handlers for the following intents:

    Intent          Handler
    ======          =======
    
    LandingPads     LandingPadsHandler
    
"""
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler 
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from ask_sdk_model import ui

from FunctionalIntentHandlers.LandingPads.landingpads import landingpads
from utilities import getJson, getTimezone


class LandingPadsHandler(AbstractRequestHandler):
    """Handler for querying the list of landing pads  """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LandingPads")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        result = getJson(1,"landpads")

        slots = handler_input.request_envelope.request.intent.slots
        speak_output = ""
        try:
            landingarea  = str(slots["LandingArea"].resolutions.resolutions_per_authority[0].values[0].value.id)
                
            if (landingarea == "RTLS"):
                speak_output = "Space ex has the following landing pads, "
                speak_connect = ', at , '
                
            if (landingarea == "ASDS"):
                speak_output = "Space ex has the following autonomous drone ships, "
                speak_connect = ', home port of , '
            
            for i in result:
                if (i['landing_type'] == landingarea):
                    speak_output = speak_output + i['full_name'] + speak_connect+ i['location']['name'] + ' , '
        
        except:

            speak_output = "Space ex has the following landing pads, " 
            
            for i in result:
                if (i['landing_type'] == "RTLS"):
                    speak_output = speak_output + i['full_name'] + ', ' 
            
            speak_output = speak_output + " and drone ships,"
            
            for i in result:
                if (i['landing_type'] == "ASDS"):
                    speak_output = speak_output + i['full_name'] + ', ' 
            
                
        card_title   = "Space/X Landing Pads"
        card_text    = "Landing Pads (Land and Sea)"
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )