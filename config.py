import json
import os

CONFIG_FILE = "configs/running.json"


class Config:

    def __init__(self):
        self.load_startup()

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
    
    def reset_interfaces_vlan(self, vlan):

        for iface, data in self.data["interfaces"].items():

            if data["access_vlan"] == vlan:

                data["access_vlan"] = 1

        self.save()

    def vlan_exists(self, vlan):

        return str(vlan) in self.data["vlans"]
   
    def remove_vlan(self, vlan):

        vlan = str(vlan)

        if vlan == "1":
            return False

        if vlan in self.data["vlans"]:

            del self.data["vlans"][vlan]

            self.reset_interfaces_vlan(
                int(vlan)
            )

            return True

        return None

    def save_interface(self, name, data):

        self.data["interfaces"][name] = data

        self.save()

    def load_interfaces(self):

        return self.data.get("interfaces", {})

    def load_startup(self):

        if not os.path.exists(
            "configs/startup.json"
        ):

            self.load()

            return

        with open(
            "configs/startup.json",
            "r"
        ) as f:

            self.data = json.load(f)

        self.save()
