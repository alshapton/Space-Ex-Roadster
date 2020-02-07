
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from ask_sdk_model import ui

from FunctionalIntentHandlers.Launches.launches import launches
from utilities import getJson


class LaunchesNextHandler(AbstractRequestHandler):
    """Handler for querying the next launch """
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("LaunchNext")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        result = getJson(1,"launches/next")

        speak_output = launches(result,1,"","next-long","")
        card_title   = "Next Space/X Launch"
        card_text    = "The next launch is on " + launches(result,1,"","next-date-short","text") + "."
        
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
                
        speak_output = launches(result,1,"","last-long","")
        card_title   = "Most recent Space/X Launch"
        card_text    = "The most recent launch was on " + launches(result,1,"","next-date-short","text") + "."
        
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