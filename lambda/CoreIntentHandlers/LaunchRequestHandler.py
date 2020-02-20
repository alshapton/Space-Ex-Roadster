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

from ask_sdk_model.dialog import DynamicEntitiesDirective
from ask_sdk_model.er.dynamic import UpdateBehavior, EntityListItem, Entity, EntityValueAndSynonyms

from utilities import getConfig, get_locale
from FunctionalIntentHandlers.LandingPads.landingpads import landingpads

import json
import requests
import boto3

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        # Get configurayion informatoin
        
        result = getConfig()
        VERSION      = result["release_info"]["version"]
        
        # Retrieve users's locale......
        locale=get_locale(handler_input)
        
        # ..... and  get their language index......
        langindex=0
        lang=0
        
        for language in result['i8n']['languages']:
            if language['language'] == locale:
                lang=langindex
            langindex = langindex+1    
        
        # ..... to get their welcome settings.
        speak_output = result['i8n']['languages'][lang]['settings']['Welcome_speech']
        
        card_text    = result['i8n']['languages'][lang]['settings']['Welcome_card_text'] + VERSION
        card_title   = result["release_info"]["skill_name"]

        # MAYBE STORE THE JSON AND THE INDEX FOR THE VERSION STUFF IN A CUSTOM SLOT SO WE DONT HAVE TO GO BACK TO THE WEB EVERY TIME - EFFICIENCY-ISE.....?
        
        #LandingZoneList slot population (using dynamic entities)
        
        results = landingpads(1,"","getLandingPadsList","None")

        R=[]
        for pad in results:
            R.append(Entity(id=pad["id"].replace("-",""), name=EntityValueAndSynonyms(value=pad["full_name"], synonyms=["X","Y"])))

        replace_entity_directive = DynamicEntitiesDirective(
            update_behavior=UpdateBehavior.REPLACE,
            types=[EntityListItem(name="LandingZoneList", values=R)],
        )        
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .add_directive(replace_entity_directive)
                .set_card(
                    ui.StandardCard(
                        title = card_title,
                        text  = card_text,
                        image = ui.Image(
                            "https://s3.amazonaws.com/CAPS-SSE/echo_developer/c6b9/849faf85adba4e6fa3a8f05777a48bbd/APP_ICON?versionId=4x9HzSdwy0_86_YxXVdMDskHFzSBL9Qq&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200208T211312Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJFEYRBGIHK2BBYKA%2F20200208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=95796d60b2583954d0da906d2ae176fd44629a354e519c08a4fd6b17ee94d043",
                            "https://s3.amazonaws.com/CAPS-SSE/echo_developer/69e2/4efe3d0dd1eb4390b87875b4b94d6b9b/APP_ICON_LARGE?versionId=jZi3YDaHhs8Y30qcu8Ji_WrdUz6D2TBE&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20200208T211312Z&X-Amz-SignedHeaders=host&X-Amz-Expires=86400&X-Amz-Credential=AKIAJFEYRBGIHK2BBYKA%2F20200208%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=6bfb34b87719adfd13f88727371278e723f0abbfcc5c19fccdd539a103ef7ba0"
                        )))
        .response
        ), synonyms=["X","Y"]