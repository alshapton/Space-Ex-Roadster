# -*- coding: utf-8 -*-

import boto3

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder       import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input       import HandlerInput

import pytz

# UI components
from ask_sdk_model import Response

# Import core intent handling classes
from CoreIntentHandlers.LaunchRequestHandler      import LaunchRequestHandler
from CoreIntentHandlers.CancelOrStopIntentHandler import CancelOrStopIntentHandler
from CoreIntentHandlers.CatchAllExceptionHandler  import CatchAllExceptionHandler
from CoreIntentHandlers.IntentReflectorHandler    import IntentReflectorHandler
from CoreIntentHandlers.HelpIntentHandler         import HelpIntentHandler

# Granular Help Handler
from CoreIntentHandlers.AssistanceIntentHandler import AssistanceIntentHandler

# Shared Handlers
from FunctionalIntentHandlers.Shared.Handlers import ChangeUnitsIntentHandler

# Import functional intent handling classes
# Roadster
from FunctionalIntentHandlers.Roadster.Handlers import   \
RoadsterOrbitIntentHandler,RoadsterSpeedHandler,         \
RoadsterLocationIntentHandler,RoadsterMarsHandler,       \
RoadsterInfoHandler

# Launches
from FunctionalIntentHandlers.Launches.Handlers import \
LaunchesNextHandler,LaunchesLastHandler

# Landing Pads
from FunctionalIntentHandlers.LandingPads.Handlers import LandingPadsHandler



logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        # Any cleanup logic goes here.

        return handler_input.response_builder.response

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

# Landing Pads Handlers
sb.add_request_handler(LandingPadsHandler())

# Exception Handler to deal with mop up
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(IntentReflectorHandler()) # This MUST be last so it doesn't override the custom intent handlers

lambda_handler = sb.lambda_handler()

# End of Lambda Function


