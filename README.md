# Space/X Info

<div align="center">
<p align="center">
<img src="https://github.com/alshapton/Space-X-Info-Alexa/blob/master/alexarocket.png" width="30%" height="30%">

## Alexa Skill for Space/X Information, using [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)

</p>
</div>

# Invocation

Use "Alexa, open SpaceX info" to invoke the skill

Once the  skill is invoked, you can do the following:



Find the location of the Tesla Roadster

	How far is the roadster from Earth

	How far is the Tesla from Earth

	Where is the Tesla

	Where is the roadster



Swap units of measure (Miles/Km)

	Change units to {units}



Find out how fast the vehicle is travelling

	What's the Tesla's speed

	What is the roadster's speed

	How fast is the Tesla going

	How fast is Starman going 



Find the location of the Tesla Roadster with respect to Mars

	How close is the Tesla to Mars

	How far is the roadster from Mars

	How far is the Tesla from Mars



Information about the eliptical orbit of the Tesla roadster

	Tell me about the Tesla's orbit

	What's the car's' orbit

	What is the roadster's orbit

	Tell me about the car's orbit

	Tell me about the roadster's orbit



Get mode detailled help

	Help me with {assistanceSubject}



Get the complete low-down on the Roadster

	Tell me all about the Tesla

	Tell me about the Tesla

	Tell me about the car

	Tell me about the roadster



The next launch

+	sxi {TimeZone} sxi ln

	What is the next launch

	whats the next launch

	Whens the next launch

	When is the next launch



The most recent launch

+	sxi {TimeZone} sxi ll

	Tell me about the most recent launch

	Tell me about the last launch

	W was the most recent launch

	What was the most recent launch

	what was the last launch

	When was the last launch



Find out about Space/X's landing pads, zones and drone ships

	Tell me about the drone ship {DroneShip}

	Tell me about the {LandingArea}

	Tell me about the landing areas



Get information about the Space/X company itself

	What is spaceX

*	What is space ex

	What is space x

	Tell me about space x

*	Tell me about Space ex

	Tel me about SpaceX


# Release History

        0.0.5 - ALS -               * Added initial support for local timezones for launches etc 
                                    * Further modularised code and increased efficiency
                                    * Added support for listing landing zones/drone ships
                                    * Initial support for multi-lingual interaction
                                    * Added API version to the splash screen
                                    * Support for asking for information about the Space/X company itself
                                    * Tidied up code, and continued adding graphics to interactions

        0.0.4 - ALS -   08/02/2020  * Added initial support for previous launch
                                    * Added landing zones into the speech for where the boosters would/have landed
                                    * Added display device support for :
                                                o Next Launch
                                                o Previous Launch
                                    * Added some (quiescent) initial landing pad support
                                    * Added version information to display on initial launch
                                    
        0.0.3 - ALS -   31/01/2020  * Initial support for display devices
                                    * Split roadster information up into basic, full and extended levels
                                    * More code modularisation
                                    * Further work on granular help
                                    * Started to add support for next launch
                                    * Added some (quiescent) initial ship support
        
        0.0.2 - ALS -   21/01/2020  * Added distance from Mars, Speed and orbit information
                                    * Commenced adding detailled, more granular help function
                                    * Split up code to make it tidier and more modular
                                    * Renamed from "Roadster in Space" to "Space/X Information"

        0.0.1 - ALS -   12/01/2020  * Initial release - distance only


### Credits
Jake Meyer's [r-spacex/SpaceX-API](https://github.com/r-spacex/SpaceX-API)






