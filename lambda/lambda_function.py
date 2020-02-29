# -*- coding: utf-8 -*-

#import boto3

import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder       import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input       import HandlerInput

#import pytz

# UI components
from ask_sdk_model import Response

# Import core intent handling classes
from CoreIntentHandlers.LaunchRequestHandler        import LaunchRequestHandler       #@ <BLANK>
from CoreIntentHandlers.CancelOrStopIntentHandler   import CancelOrStopIntentHandler  #@ <BLANK>
from CoreIntentHandlers.CatchAllExceptionHandler    import CatchAllExceptionHandler   #@ <BLANK>
from CoreIntentHandlers.IntentReflectorHandler      import IntentReflectorHandler     #@ <BLANK>
from CoreIntentHandlers.HelpIntentHandler           import HelpIntentHandler          #@ <BLANK>
from CoreIntentHandlers.SessionEndedRequestHandler  import SessionEndedRequestHandler #@ <BLANK>

# Granular Help Handler
from CoreIntentHandlers.AssistanceIntentHandler import AssistHandler                  #@ Get mode detailled help

# Shared Handlers
from FunctionalIntentHandlers.Shared.Handlers import ChangeUnitsHandler               #@ Swap units of measure (Miles/Km)

# Import functional intent handling classes
# Roadster

from FunctionalIntentHandlers.Roadster.Handlers import RoadsterOrbitHandler           #@ Information about the eliptical orbit of the Tesla roadster   
from FunctionalIntentHandlers.Roadster.Handlers import RoadsterSpeedHandler           #@ Find out how fast the vehicle is travelling
from FunctionalIntentHandlers.Roadster.Handlers import RoadsterLocationHandler        #@ Find the location of the Tesla Roadster 
from FunctionalIntentHandlers.Roadster.Handlers import RoadsterMarsHandler            #@ Find the location of the Tesla Roadster with respect to Mars
from FunctionalIntentHandlers.Roadster.Handlers import RoadsterInfoHandler            #@ Get the complete low-down on the Roadster    

# Launches
from FunctionalIntentHandlers.Launches.Handlers import LaunchNextHandler              #@ The next launch
from FunctionalIntentHandlers.Launches.Handlers import LaunchLastHandler              #@ The most recent launch

# Landing Pads
from FunctionalIntentHandlers.LandingPads.Handlers import LandingPadsHandler          #@ Find out about Space/X's landing pads, zones and drone ships

# Company
from FunctionalIntentHandlers.Info.Handlers import CompanyHandler                     #@ Get information about the Space/X company itself

# Set logging level
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# The SkillBuilder object acts as the entry point for the skill, routing all request and response
# payloads to the handlers above. 

sb = SkillBuilder()

# Skill startup Handler
sb.add_request_handler(LaunchRequestHandler())

# Core Handlers
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(HelpIntentHandler())

# Roadster Handlers
sb.add_request_handler(RoadsterMarsHandler())
sb.add_request_handler(AssistHandler())
sb.add_request_handler(RoadsterOrbitHandler())
sb.add_request_handler(RoadsterLocationHandler())
sb.add_request_handler(RoadsterSpeedHandler())
sb.add_request_handler(RoadsterInfoHandler())

# Launch Handlers
sb.add_request_handler(LaunchNextHandler())
sb.add_request_handler(LaunchLastHandler())

# Shared Component Handler
sb.add_request_handler(ChangeUnitsHandler())

# Landing Pads Handler
sb.add_request_handler(LandingPadsHandler())

# Company Handler
sb.add_request_handler(CompanyHandler())

# Exception Handler to deal with mop up
sb.add_exception_handler(CatchAllExceptionHandler())
sb.add_request_handler(IntentReflectorHandler()) # This MUST be last so it doesn't override the custom intent handlers

lambda_handler = sb.lambda_handler()

# End of Lambda Function


