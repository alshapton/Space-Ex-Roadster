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
from FunctionalIntentHandlers.Info.info import info


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
        SMALL_IMAGE  = result["Welcome_small_image"]
        LARGE_IMAGE  = result["Welcome_large_image"]
        
        # Retrieve the API version
        api_version=info(1,"","api-version","")
        
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
        
        card_text    = result['i8n']['languages'][lang]['settings']['Welcome_card_text'] + "\nSkill Version: " + VERSION + "\nAPI Version: " + api_version
        card_title   = result["release_info"]["skill_name"]

        # MAYBE STORE THE JSON AND THE INDEX FOR THE VERSION STUFF IN A CUSTOM SLOT SO WE DONT HAVE TO GO BACK TO THE WEB EVERY TIME - EFFICIENCY-ISE.....?
        
        #LandingZoneList slot population (using dynamic entities)
        
        results = landingpads(1,"","getLandingPadsList","None")
        
        R=[]
        for pad in results:
            R.append(Entity(id=pad["id"].replace("-",""), name=EntityValueAndSynonyms(value=pad["full_name"], synonyms=["X","Y"])))

        lzlist_entity_directive = DynamicEntitiesDirective(
            update_behavior=UpdateBehavior.REPLACE,
            types=[EntityListItem(name="LandingZoneList", values=R)],
        )        
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .add_directive(lzlist_entity_directive)
                .set_card(
                    ui.StandardCard(
                        title = card_title,
                        text  = card_text,
                        image = ui.Image(SMALL_IMAGE,LARGE_IMAGE)
                        )
                    )
        .response
        )