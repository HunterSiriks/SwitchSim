class MacEngine:

    def __init__(self):

        self.table = []

    def learn(
        self,
        vlan,
        mac,
        port
    ):

        for entry in self.table:

            if entry["mac"] == mac:

                entry["port"] = port
                return

        self.table.append({
            "vlan": vlan,
            "mac": mac,
            "port": port
        })

    def all(self):

        return self.table
