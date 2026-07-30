class InterfaceEngine:

    def __init__(self):
        self.interfaces = {}

        # FastEthernet 0/1-24
        for i in range(1, 25):
            self.interfaces[f"Fa0/{i}"] = {
                "description": "",
                "admin_up": False,
                "mode": "access",
                "access_vlan": 1
            }

        # GigabitEthernet 0/1-2
        for i in range(1, 3):
            self.interfaces[f"Gi0/{i}"] = {
                "description": "",
                "admin_up": False,
                "mode": "access",
                "access_vlan": 1
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
                "admin_up": False,
                "mode": "access",
                "access_vlan": 1
            }
