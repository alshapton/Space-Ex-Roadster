# -*- coding: utf-8 -*-

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder       import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input       import HandlerInput

from ask_sdk_model import Response

# Import core intent handling classes
from CoreIntentHandlers.LaunchRequestHandler      import LaunchRequestHandler
from CoreIntentHandlers.CancelOrStopIntentHandler import CancelOrStopIntentHandler
from CoreIntentHandlers.CatchAllExceptionHandler  import CatchAllExceptionHandler
from CoreIntentHandlers.IntentReflectorHandler    import IntentReflectorHandler

# Granular Help Handler
from CoreIntentHandlers.AssistanceIntentHandler import AssistanceIntentHandler


# Import functional intent handling classes
# Roadster
from FunctionalIntentHandlers.Roadster.Handlers import   \
RoadsterOrbitIntentHandler,RoadsterSpeedHandler,         \
RoadsterLocationIntentHandler,RoadsterMarsHandler,       \
RoadsterInfoHandler

# Launches
from FunctionalIntentHandlers.Launches.Handlers import \
LaunchesNextHandler,LaunchesLastHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ChangeUnitsIntentHandler(AbstractRequestHandler):
    """Handler for Change units Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ChangeUnitsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        units = slots['units'].value
        speak_output = "Your units are now," + str(units)
        handler_input.attributes_manager.session_attributes["Units"] = str(units)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "You can find out about Elon Musks roadster,by saying,, help me with,, and a specific area, such as roadster, units or launches"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for the skill, routing all request and response
# payloads to the handlers above. 

sb = SkillBuilder()

# Skill startup Handler
sb.add_request_handler(LaunchRequestHandler())

# Roadster Handlers
sb.add_request_handler(RoadsterMarsHandler())
sb.add_request_handler(AssistanceIntentHandler())
sb.add_request_handler(RoadsterOrbitIntentHandler())
sb.add_request_handler(RoadsterLocationIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(RoadsterSpeedHandler())
sb.add_request_handler(RoadsterInfoHandler())

# Launch Handlers
sb.add_request_handler(LaunchesNextHandler())
sb.add_request_handler(LaunchesLastHandler())

# Shared Component Handlers
sb.add_request_handler(ChangeUnitsIntentHandler())

# Core Handlers
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())


# Exception Handler to deal with mop up
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(IntentReflectorHandler()) # This MUST be last so it doesn't override the custom intent handlers


lambda_handler = sb.lambda_handler()




# End of Lambda Function