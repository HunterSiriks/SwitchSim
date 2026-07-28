import time
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

    @staticmethod
    def show_running_config(config, iface_engine):

        config_text = ""

        config_text += (
            f"hostname {config.hostname()}\n\n"
        )

        for vlan, name in config.vlans().items():

            config_text += (
                f"vlan {vlan}\n"
            )

            config_text += (
                f" name {name}\n\n"
            )

        for iface, data in iface_engine.all().items():

            if (
                data["description"] or
                data["access_vlan"] != 1 or
                data["admin_up"]
            ):

                config_text += (
                    f"interface {iface}\n"
                )

                if data["description"]:

                    config_text += (
                        f" description "
                        f"{data['description']}\n"
                    )

                config_text += (
                    f" switchport access vlan "
                    f"{data['access_vlan']}\n"
                )

                if data["admin_up"]:

                    config_text += (
                        " no shutdown\n"
                    )

                else:

                    config_text += (
                        " shutdown\n"
                    )

                config_text += "\n"

        size = len(
            config_text.encode("utf-8")
        )

        print()

        print(
            "Building configuration..."
        )

        time.sleep(2)

        print()

        print(
            f"Current configuration : "
            f"{size} bytes"
        )

        print()

        print(config_text)

        print("end")

    @staticmethod
    def show_startup_config(config):

        startup = config.load_startup()

        if startup is None:

            print(
                "% Startup configuration not found"
            )

            return

        print()

        print(
            "Using startup configuration"
        )

        print()

        print(
            f"hostname "
            f"{startup['hostname']}"
        )

        print()

        for vlan, name in startup[
            "vlans"
        ].items():

            print(f"vlan {vlan}")

            print(f" name {name}")

            print()

        for iface, data in startup[
            "interfaces"
        ].items():

            print(
                f"interface {iface}"
            )

            if data["description"]:

                print(
                    f" description "
                    f"{data['description']}"
                )

            print(
                f" switchport access vlan "
                f"{data['access_vlan']}"
            )

            if data["admin_up"]:

                print(
                    " no shutdown"
                )

            else:

                print(
                    " shutdown"
                )

            print()

        print("end")
