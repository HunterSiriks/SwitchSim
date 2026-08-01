from devices.device import Device


class DeviceManager:

    def __init__(self):

        self.devices = {}

    def connect(
        self,
        port,
        name,
        mac
    ):

        if port in self.devices:

            return False

        self.devices[port] = Device(
            name,
            mac
        )

        return True

    def disconnect(
        self,
        port
    ):

        if port in self.devices:

            del self.devices[port]

    def get_port(
        self,
        name
    ):

        for port, device in self.devices.items():

            if device.name == name:

                return port

        return None

    def all(self):

        return self.devices

    def mac_table(self):

        table = []

        for port, device in self.devices.items():

            table.append({

                "vlan": 1,

                "mac": device.mac,

                "port": port

            })

        return table

    def exists(
        self,
        name
    ):

        for device in self.devices.values():

            if device.name == name:

                return True

        return False
