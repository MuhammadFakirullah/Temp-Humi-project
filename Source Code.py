from machine import Pin
from time import sleep
import dht
import json
import network
import time
from umqtt.simple import MQTTClient

SERVER = "mqtt.favoriot.com"
client = MQTTClient("umqtt_client, SERVER, user="your API key here", password = "your API key here")

station = network.WLAN(network.STA_IF)
station.active(True)
station.disconnect()

if not station.isconnected():
  print('connecting to network...')
  station.connect('your ssid', 'your password')
  time.sleep(3)
  client.connect()
  
while station.isconnected():
  sensor.measure()
  temperature = sensor.temperature()
  humidity = sensor.humidity()
  dat = {"device_developer_id": "your device_developer_id", "data": {'Temperature:' :temperature, 'Humidity' :humidity}}
  data = str(json.dumps(dat))
  topic = "your API key here/v2/streams"
  
  client.publish(topic,data)
  print('Temperature: %3.1f C' %temperature, 'Humidity: %3.1f %%' %humidity)
  time.sleep(5)
