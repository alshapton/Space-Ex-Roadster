"""Handlers for Launches 

This file is used to drive the handlers for the following intents:

    Intent          Handler
    ======          =======
    
    LaunchNext      LaunchesNextHandler
    LaunchLast      LaunchesLastHandler
    
"""
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler 
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from ask_sdk_model import ui

from FunctionalIntentHandlers.Launches.launches import launches
from utilities import getJson, getTimezone


class LaunchesNextHandler(AbstractRequestHandler):
    """Handler for querying the next launch """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LaunchNext")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        result = getJson(1,"launches/next")
        
        userTimeZone = getTimezone(handler_input)
        handler_input.attributes_manager.session_attributes["TimeZone"] = str(userTimeZone)
        
        speak_output = launches(result,1,"","next-long","",userTimeZone)
        
        card_title   = "Next Space/X Launch"
        card_text    = "The next launch is on " + launches(result,1,"","next-date-short","text",userTimeZone) + "."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(
                    ui.StandardCard(
                        title = card_title,
                        text  = card_text,
                        image = ui.Image(
                            launches(result,1,"","image","['links']['mission_patch_small']"),
                            launches(result,1,"","image","['links']['mission_patch']")
                        )))
                .response
        )
    
class LaunchesLastHandler(AbstractRequestHandler):
    """Handler for querying the last launch """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LaunchLast")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        result = getJson(1,"launches/latest")

        userTimeZone = getTimezone(handler_input)
        handler_input.attributes_manager.session_attributes["TimeZone"] = str(userTimeZone)
        
        speak_output = launches(result,1,"","last-long","",userTimeZone)
        card_title   = "Most recent Space/X Launch"
        card_text    = "The most recent launch was on " + launches(result,1,"","next-date-short","text",userTimeZone) + "."
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(
                    ui.StandardCard(
                        title = card_title,
                        text  = card_text,
                        image = ui.Image(
                            launches(result,1,"","image","['links']['mission_patch_small']"),
                            launches(result,1,"","image","['links']['mission_patch']")
                        )))
                .response
        )