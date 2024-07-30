# https://tutorials-raspberrypi.com/raspberry-pi-measure-humidity-temperature-dht11-dht22/
# https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup
#NOTE RUNS WITH PYTHON3

# DHT error marings is +- 2 degrees celsius

import time
import board
import adafruit_dht
import writetodb

dht11 = adafruit_dht.DHT11(board.D4, use_pulseio = False)

location = "Loftet"
pin = 4

def measure_temp_hum(pin, location):
    while True:
        try:
            # Print the values to the serial port
            temp_c = dht11.temperature
            temp_f = temp_c * (9 / 5) + 32
            humidity = dht11.humidity
            writetodb.write_from_dht11(pin, temp_c, temp_f, humidity, location)
            break
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            continue
        #time.sleep(2.0)
        except Exception as error:
            dht11.exit()
            raise error
    
measure_temp_hum(pin, location)
 
    #time.sleep(2.0)