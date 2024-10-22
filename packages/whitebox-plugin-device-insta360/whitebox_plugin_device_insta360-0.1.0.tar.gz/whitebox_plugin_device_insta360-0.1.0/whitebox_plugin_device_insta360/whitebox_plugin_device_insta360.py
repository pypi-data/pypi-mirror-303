from plugin.utils import Plugin
from devices.base import Device


class Insta360Base(Device):
    @classmethod
    def get_connection_types(cls):
        return {
            "wifi": {
                "name": "Wi-Fi",
                "fields": {
                    "ssid": {
                        "name": "Network Name",
                        "type": "text",
                        "required": True,
                    },
                    "password": {
                        "name": "Network Password",
                        "type": "password",
                        "required": True,
                    },
                },
            },
        }

    def check_connectivity(self):
        """
        Check whether the device has connection.

        Returns:
            Boolean whether the device has connection.
        """

        # TODO: Connect to WIFI, whether directly, or by controlling some kind
        #       of a relay that can connect to the device's WiFi
        #       Issue: whitebox#96
        return True


class Insta360X3(Insta360Base):
    codename = "insta360_x3"
    device_name = "Insta360 X3"


class Insta360X4(Insta360Base):
    codename = "insta360_x4"
    device_name = "Insta360 X4"


class WhiteboxPluginDeviceInsta360(Plugin):
    """
    A plugin that enables support for Insta360 cameras.

    Attributes:
        name: The name of the plugin.
    """

    name = "Insta360 Camera Support"
    device_classes = [Insta360X3, Insta360X4]


plugin_class = WhiteboxPluginDeviceInsta360
