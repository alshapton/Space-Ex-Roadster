"""Info Handlers 

This file is used to drive the handlers for the following intent:

    Intent              Handler
    ======              =======
    
    CompanyIntent       CompanyIntentHandler

"""
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from FunctionalIntentHandlers.Info.info import info

import inflect

class CompanyHandler(AbstractRequestHandler):
    """Handler for Company Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Company")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        
        
        # Get instance of the number to words engine
        p = inflect.engine()
        results = info(1,"","company","")
        
        worth = p.number_to_words(results["valuation"])
        employees = p.number_to_words(results["employees"])
        vehicles=p.number_to_words(results["vehicles"])
        launch_sites = p.number_to_words(results["launch_sites"])
        test_sites  = p.number_to_words(results["test_sites"])
        
        ceo = results["ceo"]
        cto = results["cto"]
        coo = results["coo"]
        cto_propulsion = results["cto_propulsion"]
        mgt =  "Headquartered in " + results["headquarters"]["city"] + ", " + results["headquarters"]["state"] 
        mgt = mgt + ", it's Chief Executive Officer is " + ceo + ", the Chief Operating Officer, " + coo + ", Chief Technology Officer, " + cto +  " and the Chief Technology Officer for Propulsion is " + cto_propulsion

        speak_output = results["summary"] + ". It has " + employees + " staff and is currently worth " + worth + " dollars. "
        speak_output = speak_output + "It has " + vehicles + " launch " + p.plural("vehicle",vehicles) + ", " + launch_sites + " launch " + p.plural("site",launch_sites) + ", and " + test_sites + " test " + p.plural("site",test_sites) + "."
        speak_output = speak_output + "     " + mgt
        
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )
