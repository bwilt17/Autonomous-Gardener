# Autonomous Gardener V1.0

A mechatronics course project designed to autonomously care for a potted plant.


## Project Overview 

This project was designed and produced by Manraj Banghu and Beverly Wilt at San Jose State University in Spring 2021. Because of meeting constraints due to the Covid-19 pandemic, the project was done collaboratively online and two physical prototypes were made for testing, one for each team member.

<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/prototype1.jpg" width="400" />  <img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/prototype2.jpg" width="400" />


## General Design and Goals

**Goal Product:**
  - Autonomous plant caretaker that interfaces the Adafruit nRF52840 sense microcontroller with the following:
    - 3V Water Pump
    - BH1750 Light Sensor(s)
    - STEMMA I2C Capacitive Soil Moisture Sensor

***Note:** Due to shipping issues during the Covid-19 pandemic, the light sensors were ultimately replaced with the integrated temperature sensor on the STEMMA due to lack of connector components.*

**Design Goals:**
  - Not to exceed $100 budget (including university provided components)
  - Sized for reasonable desktop use
  - Makes use of 3D printed water distribution part sized for use in a basic 4.5in terracotta pot from Home Depot and saucer
  - No heavier than 5lbs 

***(UPDATE: 5/10/21)** The final prototype accomplished all of the design goals EXCEPT the weight restriction due to the weight of the water reservoir and moistened soil. Final specifications to be added at a later date.*

<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/design.png" width="400" />


## Water Distribution Part Info

A part for this project to distribute water around the pot was designed in SolidWorks and 3D printed. Print specifications and 3D model files can be found under [CAD files](https://github.com/bwilt17/Autonomous-Gardener/tree/main/CAD%20files).

***(UPDATE: 4/5/21)** Part design needs to be modified to have longer stakes for better soil penetration OR soil level in final potted plant used must be specified to be no lower than approx. 1/2" from the top edge of the pot.*

***(UPDATE: 5/10/21)** For the purposes of this course project, soil level in final potted plant was specified and increased to appropriate level. Another issue found in the final prototype is that the nozzle outlets furthest from the inlet have trouble getting water, presumably because the pump does not fill the nozzle completely in its runtime. Need stronger pump to ensure complete fill and/or narrower interior section.* 

<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/partSW-1.PNG" width="400" /> <img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/part1-2.jpg" width="400" />


## Circuit Design:

The interface circuit makes use of a darlington transistor acting as a switch for the pump control. This simplified the circuit design, as it was similar to a setup from a course lab assignment, and allowed us to PWM for better control over pump speed. 

<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/circdiagram.png" width="700" />
<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/asmbcircuit.jpg" width="700" />


## Coding

The program for the autonomous gardener was made in CircuitPython with Mu as a main editor and user interface. The full code, as presented for the course, can be found under [code](https://github.com/bwilt17/Autonomous-Gardener/tree/main/code).

A general flowchart for the program can be seen below:

<img src="https://github.com/bwilt17/Autonomous-Gardener/blob/main/images/flowchart.png" width="700" />

## Proof of Functionality

A short video showcasing the prototype's functionality can be found on [Youtube](https://www.youtube.com/watch?v=F2NkZJcwzsY).

## Improvements/Recommendations

The following are some suggestions for future improvement, to be done in V2.0: 
  - Decrease electronics footprint by putting nRF directly on breadboard 
     - Need external speaker OR replace moisture sensor with one that has integrated speaker to keep error/pump audio cues
  - Waterproof box to contain electronics to prevent shorting/damage
  - Add a water level sensor (ultrasonic sensor?) to the reservoir to prevent motor damage due to low water level
  - Battery/LCD screen integration to remove need for computer tether
  - Larger water reservoir for less user-dependency
  - Housing that combines electronics, reservoir, etc. into a more polished product
  - Different plant type scenarios (ie. succulent, tropical, etc.) for moisture regulation, or allow for user input
