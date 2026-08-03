from devices.device import Device


class DeviceManager:

    def __init__(self):

        self.devices = {}

        self.mac_entries = []

    def learn_mac(
        self,
        vlan,
        mac,
        port
    ):

        for entry in self.mac_entries:

            if entry["mac"] == mac:

                return

        self.mac_entries.append({

            "vlan": vlan,

            "mac": mac,

            "port": port

        })

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

        self.learn_mac(
            1,
            mac,
            port
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

    def mac_table(
        self
    ):

        return self.mac_entries

    def mac_count(
        self
    ):

        return len(
            self.mac_entries
        )

    def clear_mac_table(
        self
    ):

        self.mac_entries.clear()

    def exists(
        self,
        name
    ):

        for device in self.devices.values():

            if device.name == name:

                return True

        return False
