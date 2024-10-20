from masterpiece.core import MasterPiece


class JMqtt(MasterPiece):
    """Base class for MQTT brokers."""

    def __init__(self, name):
        super().__init__(name)

    def disconnect_from_server(self):
        """Disconnect from the MQTT broker.

        It is up to the sub classes to implement the method.
        """

    def connect_to_server(
        self, host: str = "localhost", port: int = 1883, keepalive: int = 60
    ) -> int:
        """Connect to MQTT server

        Args:
            host (str, optional): host. Defaults to "localhost".
            port (int, optional): port. Defaults to 1883.
            keepalive (int, optional): keep alive, in seconds. Defaults to 60.

        Returns:
            0 if ok, non-zero values indicate errors

        """
        return 0

    def loop_stop(self):
        """Stop the network loop.

        No further messages shall be dispatched.
        """
