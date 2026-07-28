import json
import os

CONFIG_FILE = "configs/running.json"


class Config:

    def __init__(self):
        self.load()

    def load(self):
        if os.path.exists(CONFIG_FILE):
            with open(CONFIG_FILE, "r") as f:
                self.data = json.load(f)
        else:
            self.data = {
                "hostname": "Switch",
                "vlans": {
                    "1": "default"
                },
                "interfaces": {},
                "mac_table": [],
                "routes": []
            }

    def save(self):
        with open(CONFIG_FILE, "w") as f:
            json.dump(self.data, f, indent=4)

    def hostname(self):
        return self.data["hostname"]

    def set_hostname(self, hostname):
        self.data["hostname"] = hostname
        self.save()

    def vlans(self):
        return self.data["vlans"]

    def add_vlan(self, vlan):

        vlan = str(vlan)

        if vlan not in self.data["vlans"]:
            self.data["vlans"][vlan] = f"VLAN{vlan}"
            self.save()

    def set_vlan_name(self, vlan, name):
        self.data["vlans"][str(vlan)] = name
        self.save()
    def interfaces(self):
        return self.data["interfaces"]

    def save_interface(self, name, data):

        self.data["interfaces"][name] = data

        self.save()

    def load_interfaces(self):

        return self.data.get("interfaces", {})

    def load_startup(self):

        if not os.path.exists(
            "configs/startup.json"
        ):

            return None

        with open(
            "configs/startup.json",
            "r"
        ) as f:

            return json.load(f)
