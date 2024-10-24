# OpenSTS Python
This Python package provides a simple MQTT client using the `paho-mqtt` library, with built-in support for subscribing to multiple topics and handling messages. The package supports configuration via environment variables for enhanced security.

## Configuration

This package uses environment variables for credentials. You can configure these by creating a `.env` file in the project directory:

### Environment variables

```env
MQTT_BROKER=your_broker_address
MQTT_PORT=1883
MQTT_USERNAME=your_username
MQTT_SECRET_KEY=your_secret_key
```

### Topics in MQTT
In OpenSTS, MQTT topics follow a specific format to allow for proper identification of devices and applications.
This ensures that data published by a device under a particular application can be easily accessed by authorized users or services.
The topic format looks like this `applications/{Application ID}/devices/{Device ID}` e.g `applications/23/devices/12`. 
