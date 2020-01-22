
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from roadster import roadster

class RoadsterOrbitIntentHandler(AbstractRequestHandler):
    """Handler for Orbit of Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterOrbit")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        loc = roadster(1,str(units),"orbit")
        speak_output=str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )