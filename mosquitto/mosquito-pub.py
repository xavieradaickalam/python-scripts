'''
Created on Feb 12, 2015

@author: I057588
'''
import mosquitto

def publish ():
    mqttc = mosquitto.Mosquitto("python_pub")
    mqttc.will_set("/event/dropped", "Sorry, I seem to have died.")
    mqttc.connect("10.30.92.239", 188, 60, True)    
    mqttc.publish("hello/world", "Hello, World!")
    
if __name__ == '__main__':
    publish()