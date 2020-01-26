
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 


from FunctionalIntentHandlers.Roadster.roadster import roadster

class RoadsterOrbitIntentHandler(AbstractRequestHandler):
    """Handler for Orbit of Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterOrbit")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        orb = roadster(1,str(units),"orbit")
        speak_output="It has " + str(orb)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class RoadsterSpeedHandler(AbstractRequestHandler):
    """Handler for Speed of Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterSpeed")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        speak_output = "The roadster is " + str(roadster(1,str(units),"speed"))
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
        speak_output="It is " + str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class RoadsterInfoHandler(AbstractRequestHandler):
    """Handler for Full/Partial information about the roadster."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterInfo")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]        
        infolevel = str(handler_input.request_envelope.request.intent.slots['RoadsterInformation'].resolutions.resolutions_per_authority[0].values[0].value.id)
        
        earth = roadster(1,str(units),"distance")

        if (infolevel.lower() == "yes"): # Long 

            details = roadster(1,"","details")
            norad = roadster(1,"","norad")
            launchdatetime=roadster(1,"","launch-long")
            weights = roadster(1,"","mass")
            norad = roadster(1,"","norad")

            
            mars = roadster(1,str(units),"mars")
            
            speak_output = str(details) + ",, It was launched on " + launchdatetime
            speak_output = speak_output + ",," + weights
            speak_output = speak_output + ",,Its Norad eye dee is " + norad
            speak_output = speak_output + " . It is currently " + earth + " and " + mars
        
        if (infolevel.lower() == "no"): # Short 

            name = roadster(1,"","name")
            launchdatetime=roadster(1,"","launch-short")
            
            speak_output = str(name) + " was launched on " + launchdatetime + " and is currently " + earth
        
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
        speak_output="The roadster is " + str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )