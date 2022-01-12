# Pacemaker
This repo contains a MATLAB simulink model that simulates the functions and features of a real pacemaker as well as a Device Controller Monitor design for the Pacemaker.

## Pacemaker Target Hardware
-The Pacemaker simulink model will be run on the NXP FRDM-K64F embedded microcontroller 

-A custom Pacemaker shield will be attached to the micontroller which is designed to simulate the bioelectrical interface of the heart with a real-time microcontroller.The purpose of the shield is to allow for the microcontroller to send and receive pacing information as well as collect data signals to and from the heart through the standard lead connections. The shield allows for collection of analog signals along with PWM output that charge capacitors that determine voltage settings in various locations in the shield.

<img src="images\Pacemaker_Hardware.jpg" alt="alt text" width="700" height="400">

-The Device controller Monitor is python based and can be hosted on any computer that can interface with the NXP FRDM-K64F embedded microcontroller using serial communication

## Sample Output on Osciliiscope 
<img src="images\Sample_Hardware_Output.PNG" alt="alt text" width="700" height="400">
