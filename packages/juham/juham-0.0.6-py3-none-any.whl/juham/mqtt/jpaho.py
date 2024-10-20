import os
import paho.mqtt.client as paho
from juham.base.jmqtt import JMqtt


class JPaho(JMqtt):
    """MQTT broker implementation based on paho.mqtt.

    Creates a paho mosquitto client running on localhost and port 1883.
    """

    paho_api_version = 1

    def __init__(self, name="paho"):
        """Construct MQTT client for the configured mqtt broker of the
        configured paho_version.

        Args:
            name (str): name for the object.
        """
        super().__init__(name)
        if self.paho_api_version == 2:
            self.mqtt_client = paho.Client(
                paho.CallbackAPIVersion.VERSION1, name + str(os.getpid())
            )
        else:
            self.mqtt_client = paho.Client(name + str(os.getpid()))

    def connect_to_server(
        self,
        host="locahost",
        port=1883,
        keepalive=60,
        bind_address="",
        clean_start=True,
        properties=None,
    ):
        """Connects the client to the mqtt broker."""
        return self.mqtt_client.connect(host, port, keepalive, bind_address)

    def disconnect_from_server(self):
        self.mqtt_client.disconnect()

    def loop_stop(self):
        self.mqtt_client.loop_stop()

    def subscribe(self, topic, qos=0):
        """Subscribe to the given topic."""
        self.mqtt_client.connected_flag = True
        self.mqtt_client.subscribe(topic, qos)

    def publish(self, topic, msg=None, qos=0, retain=False):
        """Publishes an MQTT message.

        This method sends a message to the MQTT broker and publish it
        to the given topic.

        Parameters:
        msg (str): The topic the message is published to.
        msg (str): The message to be published.

        Raises:
        ValueError: If the message is not a string or is empty.
        ConnectionError: If there is a problem connecting to the MQTT broker.
        MQTTException: If there is an error during the publish operation.
        """
        pass

    def on_message(self, mth):
        """Set the message handler, a method to be called when new messages are
        published.

        Args:
            mth (meth): python method to be called on arrival messages.
        """
        self.mqtt_client.on_message = mth

    def on_connect(self, mth):
        self.mqtt_client.on_connect = mth

    def on_disconnect(self, mth):
        self.mqtt_client.on_disconnect = mth

    def loop_start(self):
        self.mqtt_client.loop_start()

    def loop_forever(self):
        self.mqtt_client.loop_forever()
