class InterfaceEngine:

    def __init__(self):
        self.interfaces = {}

        # FastEthernet 0/1-24
        for i in range(1, 25):
            self.interfaces[f"Fa0/{i}"] = {
                "description": "",
                "admin_up": False,
                "mode": "access",
                "access_vlan": 1,
                "input_packets": 0,
                "output_packets": 0,
                "errors": 0
            }

        # GigabitEthernet 0/1-2
        for i in range(1, 3):
            self.interfaces[f"Gi0/{i}"] = {
                "description": "",
                "admin_up": False,
                "mode": "access",
                "access_vlan": 1,
                "input_packets": 0,
                "output_packets": 0,
                "errors": 0
            }

    def exists(self, name):
        return name in self.interfaces

    def set_description(self, name, desc):
        self.interfaces[name]["description"] = desc

    def shutdown(self, name):
        self.interfaces[name]["admin_up"] = False

    def no_shutdown(self, name):
        self.interfaces[name]["admin_up"] = True

    def set_access_vlan(self, name, vlan):
        self.interfaces[name]["access_vlan"] = vlan

    def increment_input(
        self,
        iface
    ):

        self.interfaces[iface][
            "input_packets"
        ] += 1


    def increment_output(
        self,
        iface
    ):

        self.interfaces[iface][
            "output_packets"
        ] += 1

    def clear_counters(
        self
    ):

        for iface in self.interfaces:

            self.interfaces[iface][
                "input_packets"
            ] = 0

            self.interfaces[iface][
                "output_packets"
            ] = 0

            self.interfaces[iface][
                "errors"
            ] = 0

    def get(self, name):
        return self.interfaces[name]

    def all(self):
        return self.interfaces
    def export(self):
        return self.interfaces

    def import_data(self, data):

        if data:
            self.interfaces.update(data)

    def default_interface(self, iface):

            self.interfaces[iface] = {
                "description": "",
                "admin_up": True,
                "mode": "access",
                "access_vlan": 1,
                "input_packets": 0,
                "output_packets": 0,
                "errors": 0
            }
