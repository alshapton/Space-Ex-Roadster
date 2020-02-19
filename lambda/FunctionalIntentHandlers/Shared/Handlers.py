"""Shared Handlers 

This file is used to drive the handlers for the following intents:

    Intent              Handler
    ======              =======
    
    ChangeUnitsIntent   ChangeUnitsIntentHandler

"""
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 


class ChangeUnitsIntentHandler(AbstractRequestHandler):
    """Handler for Change units Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("ChangeUnitsIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
          
        slots = handler_input.request_envelope.request.intent.slots
        units = slots['units'].value
        speak_output = "Your units are now," + str(units) + " "
        handler_input.attributes_manager.session_attributes["Units"] = str(units)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
