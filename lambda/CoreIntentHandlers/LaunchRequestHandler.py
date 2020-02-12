"""Handler for main skill launch function  

This file is used to drive the handlers for the following intent:

    Intent          Handler
    ======          =======
    
    LaunchRequest   LaunchRequestHandler    -   Start the skill
    
"""
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from ask_sdk_model import ui
from utilities import getConfig

import json

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Welcome, I can tell you about space ex. say Help for more information about what you can ask me to do. Note that I am not affiliated with space ex in any way."
        session_attr = handler_input.attributes_manager.session_attributes
        result = getConfig()
        VERSION=result["release_info"]["version"]
        
        handler_input.attributes_manager.session_attributes["Units"] = "Miles"
        
        card_title   = "Space/X Info"
        card_text    = "Information about Space/X's activities.\nNote that this Alexa skill is not affiliated with Space/X in ANY way.\n\nVersion " +  VERSION

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(
                    ui.StandardCard(
                        title = card_title,
                        text  = card_text,
                        image = ui.Image(
                            "https://s3.amazonaws.com/CAPS-SSE/echo_developer/c6b9/849faf85adba4e6fa3a8f05777a48bbd/APP_ICON?versionId=4x9HzSdwy0_86_YxXVdMDskHFzSBL9Qq&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200208T211312Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJFEYRBGIHK2BBYKA%2F20200208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=95796d60b2583954d0da906d2ae176fd44629a354e519c08a4fd6b17ee94d043",
                            "https://s3.amazonaws.com/CAPS-SSE/echo_developer/69e2/4efe3d0dd1eb4390b87875b4b94d6b9b/APP_ICON_LARGE?versionId=jZi3YDaHhs8Y30qcu8Ji_WrdUz6D2TBE&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200208T211312Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJFEYRBGIHK2BBYKA%2F20200208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6bfb34b87719adfd13f88727371278e723f0abbfcc5c19fccdd539a103ef7ba0"
                        )))
        .response
        )