from config import Config

cfg = Config()


class Commands:

    @staticmethod
    def invalid():
        print("% Invalid command")

    @staticmethod
    def show_version():

        print("""
Cisco IOS Software

SwitchSim Software Version 0.2

Model Number : Catalyst-2960

System image : flash:switchsim.bin
""")

    @staticmethod
    def show_vlan():

        cfg.load()

        print()

        print("VLAN Name                             Status")
        print("---- -------------------------------- --------")

        for vlan, name in cfg.vlans().items():

            print(f"{vlan:<4} {name:<32} active")

        print()

    @staticmethod
    def show_mac():

        print("""
          Mac Address Table

-------------------------------------------

Vlan    Mac Address       Type      Ports

1       0011.2233.4455    DYNAMIC   Fa0/1

1       00AA.BBCC.DDEE    DYNAMIC   Fa0/2
""")

    @staticmethod
    def show_ip_interface_brief():

        print("""
Interface              IP-Address      Status

Vlan1                  unassigned      up

Fa0/1                  unassigned      up

Fa0/2                  unassigned      up
""")

    @staticmethod
    def show_interfaces_status(iface_engine):

        print()

        print(
            "Port      Status      VLAN  Description"
        )

        print(
            "--------- ----------- ----- ----------------"
        )

        for name, data in iface_engine.all().items():

            status = (
                "connected"
                if data["admin_up"]
                else "disabled"
            )

            print(
                f"{name:<9} "
                f"{status:<11} "
                f"{data['access_vlan']:<5} "
                f"{data['description']}"
            )

        print()
