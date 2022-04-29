# Team210-ThermoCover
This is the README file for the Thermo Mask.

The Thermo Mask is a  wearable mask, with added features that will improve users’ experiences and comfort such as a temperature sensor, a pressure sensor, and an LED display that can display a users' current health. The pressure sensor will act as the power button where once it senses the user it will turn on. There will be an interrupt while waiting to recieve access to a users temperature using the MQTT server. After access has been granted from the server, the temperature sensor will then gather data about the user's temperature and send that data to the LED display. The data will blink for some time on the LED display and then turn off until access is granted again. 
