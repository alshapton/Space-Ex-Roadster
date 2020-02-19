

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

class AssistanceIntentHandler(AbstractRequestHandler):
    """Handler for Detailed help."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("Assist")(handler_input) 

    def handle(self, handler_input): 
        
        # type: (HandlerInput) -> Response
        slots = handler_input.request_envelope.request.intent.slots
        subject = slots['assistanceSubject'].value
         
        SPEECH = str(subject)
        if (subject is None):
            SPEECH = "Please tell me what you want help with,, roadster, launches or units"
            
        if (str(subject).lower() == "roadster"):
            SPEECH = "To find out where the roadster is, say ,,where is it,,"
            SPEECH = SPEECH + "To find out how far from Mars, say ,, how close to mars,,"
            SPEECH = SPEECH + "To find out about its orbit, say,, tell me about the orbit"
            
        if (str(subject).lower() == "units"):
            SPEECH = "By default, the units of distance are miles,, but you can change that, if you wish,,"
            SPEECH = SPEECH + "To change the units to kilometers, say,, change units to kilometers,,"
            SPEECH = SPEECH + "To change the units to miles, say,, change units to miles"
            
        if (str(subject).lower() == "launches"):
            SPEECH = "To find out when the next launch is, say Whens the next launch?"

        return (
            handler_input.response_builder
                .speak(SPEECH)
                .ask(SPEECH)
                .response
        )