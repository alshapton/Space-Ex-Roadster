"""Handlers for Roadster 

This file is used to driver the handlers for the following intents:

    Intent              Handler
    ======              =======
    
    RoadsterOrbit       RoadsterOrbitHandler
    RoadsterSpeed       RoadsterSpeedHandler
    RoadsterLocation    RoadsterLocationHandler
    RoadsterInfo        RoadsterInfoHandler
    RoadsterMars        RoadsterMarsHandler
    
"""

import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput 

from ask_sdk_model import ui

from FunctionalIntentHandlers.Roadster.roadster import roadster

class RoadsterOrbitHandler(AbstractRequestHandler):
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
                .set_card(
                    ui.StandardCard(
                        title = "Elon Musk's Tesla Roadster",
                        text  = "The Roadster, picture with Earth in background. 'Spaceman' mannequin wearing SpaceX Spacesuit in driving seat. The camera is mounted on an external boom.",
                        image = ui.Image(
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg")
                        ))
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
                .set_card(
                    ui.StandardCard(
                        title = "Elon Musk's Tesla Roadster",
                        text  = "The Roadster, picture with Earth in background. 'Spaceman' mannequin wearing SpaceX Spacesuit in driving seat. The camera is mounted on an external boom.",
                        image = ui.Image(
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg")
                        ))
                .response
        )
    
class RoadsterLocationHandler(AbstractRequestHandler):
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
                .set_card(
                    ui.StandardCard(
                        title = "Elon Musk's Tesla Roadster",
                        text  = "The Roadster, picture with Earth in background. 'Spaceman' mannequin wearing SpaceX Spacesuit in driving seat. The camera is mounted on an external boom.",
                        image = ui.Image(
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg")
                        ))
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

        if ((infolevel.lower() == "full") or (infolevel.lower() == "extended")): # full / extended 

            details = roadster(1,"","details")
            norad = roadster(1,"","norad")
            launchdatetime=roadster(1,"","launch-long")
            weights = roadster(1,"","mass")
            norad = roadster(1,"","norad")

            
            mars = roadster(1,str(units),"mars")
            
            speak_output = ""
            #speak_output = speak_output + str(details)
            speak_output = speak_output + ",, It was launched on " + launchdatetime
            speak_output = speak_output + ",," + weights
            speak_output = speak_output + ",,Its Norad eye dee is " + norad
            speak_output = speak_output + " . It is currently " + earth + " and " + mars
        
        if (infolevel.lower() == "extended"): # Extended 
            
            apoapsis_au = roadster(1,"","apoapsis_au")
            periapsis_au = roadster(1,"","periapsis_au")
            semi_major_axis = roadster(1,"","semi_major_axis")
            eccentricity = roadster(1,"","eccentricity")
            inclination = roadster(1,"","inclination")
            longitude = roadster(1,"","longitude")
            periapsis = roadster(1,"","periapsis_arg")


            speak_output = speak_output + ",,In astronomical units, its apoapsis is " + apoapsis_au
            speak_output = speak_output + ",its periapsis is " + periapsis_au + ", whilst its semi major axis is " + semi_major_axis
            speak_output = speak_output + ". It has an orbital eccentricity of " + eccentricity + ", an inclination of " + inclination + " degrees."
            speak_output = speak_output + "Its periapsis argument is " + periapsis + " degrees."
            

        if (infolevel.lower() == "basic"): # Basic 

            name = roadster(1,"","name")
            launchdatetime=roadster(1,"","launch-short")
            
            speak_output = str(name) + " was launched on " + launchdatetime + " and is currently " + earth
        # https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(
                    ui.StandardCard(
                        title = "Elon Musk's Tesla Roadster",
                        text  = "The Roadster, picture with Earth in background. 'Spaceman' mannequin wearing SpaceX Spacesuit in driving seat. The camera is mounted on an external boom.",
                        image = ui.Image(
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg")
                        ))
                .response
                )

class RoadsterMarsHandler(AbstractRequestHandler):
    """Handler for distance away from Mars of the Roadster Intent."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return ask_utils.is_intent_name("RoadsterMars")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        units = handler_input.attributes_manager.session_attributes["Units"]
        loc = roadster(1,str(units),"mars")
        speak_output="The roadster is " + str(loc)
        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .set_card(
                    ui.StandardCard(
                        title = "Elon Musk's Tesla Roadster",
                        text  = "The Roadster, picture with Earth in background. 'Spaceman' mannequin wearing SpaceX Spacesuit in driving seat. The camera is mounted on an external boom.",
                        image = ui.Image(
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg",
                            "https://upload.wikimedia.org/wikipedia/commons/2/20/Elon_Musk%27s_Tesla_Roadster_%2840110304192%29.jpg")
                        ))
                .response
        )