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

class MACTable:

    def __init__(
        self
    ):

        self.table = []

    def learn(
        self,
        vlan,
        mac,
        port
    ):

        self.table.append(
            {
                "vlan": vlan,
                "mac": mac,
                "port": port
            }
        )

    def show(
        self
    ):

        print()

        print(
            "Vlan    Mac Address       Port"
        )

        print(
            "----    ----------------  -----"
        )

        for entry in self.table:

            print(
                f"{entry['vlan']:<8}"
                f"{entry['mac']:<18}"
                f"{entry['port']}"
            )

    def count(
        self
    ):

        return len(
            self.table
        )

    def clear(
        self
    ):

        self.table.clear()
