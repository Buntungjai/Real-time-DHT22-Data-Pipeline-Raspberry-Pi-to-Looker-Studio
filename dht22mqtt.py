import time
import board
import adafruit_dht
import paho.mqtt.client as mqtt
import json

# ---- DHT22 ----
dht = adafruit_dht.DHT22(board.D4)  # GPIO4

# ---- MQTT ----
MQTT_BROKER = "localhost"   # Pi เป็น server เอง
MQTT_TOPIC = "sensor/dht22"

client = mqtt.Client()
client.connect(MQTT_BROKER, 1883, 60)

while True:
    try:
        temp = dht.temperature
        hum = dht.humidity

        if temp is not None and hum is not None:
            payload = {
                "temperature": round(temp, 2),
                "humidity": round(hum, 2)
            }
            client.publish(MQTT_TOPIC, json.dumps(payload))
            print(payload)

    except RuntimeError as e:
        print("Read error:", e)

    time.sleep(2)
