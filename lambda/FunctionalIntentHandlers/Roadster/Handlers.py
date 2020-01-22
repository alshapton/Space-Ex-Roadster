
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
        orb = roadster(1,str(units),"orbit")
        speak_output=str(orb)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class SpeedIntentHandler(AbstractRequestHandler):
    """Handler for Speed of Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("SpeedIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        loc = roadster(1,str(units),"speed")
        speak_output=str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
    
class RoadsterLocationIntentHandler(AbstractRequestHandler):
    """Handler for Location of Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterLocation")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        loc = roadster(1,str(units),"distance")
        speak_output=str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class MarsIntentHandler(AbstractRequestHandler):
    """Handler for distance away from Mars of the Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("MarsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        loc = roadster(1,str(units),"mars")
        speak_output=str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )