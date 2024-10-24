import os
import paho.mqtt.client as mqtt
from dotenv import load_dotenv
from topic import topics

# Load credentials from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')


# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker successfully")
    else:
        print(f"Failed to connect. Return code: {rc}")

# Callback when the client disconnects
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print(f"Unexpected disconnection. Return code: {rc}")
    try:
        client.reconnect()  # Try to reconnect
    except Exception as e:
        print(f"Reconnection failed: {e}")

# Callback when a message is received
def on_message(client, userdata, message):
    try:
        payload = message.payload.decode()
        print(f"Received message: {payload} from topic: {message.topic}")
    except Exception as e:
        print(f"Error processing message: {e}")

# Callback when the client subscribes to a topic
def on_subscribe(client, userdata, mid, granted_qos):
    if granted_qos[0] == 128:
        print("Subscription failed")
    else:
        print(f"Subscribed to topic with QoS {granted_qos}")

def subscriber(env_file_path, topics):
    # Load credentials from .env file
    load_dotenv(dotenv_path=env_file_path)
    broker_address = os.getenv("MQTT_BROKER")
    broker_port = int(os.getenv("MQTT_PORT",1888))
    username = os.getenv("MQTT_USERNAME")
    secret_key = os.getenv("MQTT_SECRET_KEY")

    # Create an MQTT client instance
    client = mqtt.Client()

    # Set username and password for the broker
    client.username_pw_set(username, secret_key)

    # Set callbacks
    client.on_connect = on_connect
    client.on_disconnect = on_disconnect
    client.on_message = on_message
    client.on_subscribe = on_subscribe

    try:
        # Connect to the broker
        client.connect(broker_address, broker_port)
        client.loop_start()
            
        for topic in topics:
            try:
                client.subscribe(topic)
                print(f"Trying to subscribe to topic: {topic}")
            except Exception as e:
                print("Failed to subscribe to topic: {topic}. Error: {e}")
        while True:
            pass

    except KeyboardInterrupt:
        print("\nKeyboard interrupt detected.")
    finally:
        client.loop_stop()
        client.disconnect()
        print("Client disconnected and program terminated.")

def main():
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    subscriber(env_file, topics)

if __name__ == "__main__":
    main()
