import time

START_TIME = time.time()

from datetime import datetime

from config import Config

cfg = Config()


class Commands:

    @staticmethod
    def invalid():
        print(
            "% Invalid input detected at '^' marker."
        ) 

    @staticmethod
    def uptime():

        seconds = int(
            time.time() - START_TIME
        )

        return f"{seconds} seconds"

    @staticmethod
    def show_clock():

        print(
            datetime.now().strftime(
                "%H:%M:%S %a %b %d %Y"
            )
        )

    @staticmethod
    def ping(
        target,
        devices,
        iface
    ):

        if devices.exists(
            target
        ):

            port = devices.get_port(
                target
            )

            if not iface.get(
                port
            )["admin_up"]:

                print()

                print(
                    "% Interface is administratively down"
                )

                print(
                    "Success rate is 0 percent (0/5)"
                )

            else:

                iface.increment_input(
                    port
                )

                iface.increment_output(
                    port
                )

                print()

                print(
                    "!!!!!"
                )

                print(
                    "Success rate is 100 percent (5/5)"
                )

        else:

            print()

            print(
                f"% Unknown host or device: {target}"
            )

            print(
                "Success rate is 0 percent (0/5)"
            )

    @staticmethod
    def show_version():

        print(f"""

Cisco IOS Software

SwitchSim Software Version 0.4

Model Number : Catalyst-2960

System image file is "flash:switchsim.bin"

System uptime : {Commands.uptime()}

Compiled Thu 29-Jul-26

Copyright (c) 2026 SwitchSim Project

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
    def show_mac(
        devices
    ):

        print()

        print(
            "Mac Address Table"
        )

        print()

        print(
            "-------------------------------------------"
        )

        print()

        print(
            "Vlan    Mac Address       Type      Ports"
        )

        print()

        for entry in devices.mac_table():

            print(
                f"{entry['vlan']:<8}"
                f"{entry['mac']:<18}"
                f"DYNAMIC   "
                f"{entry['port']}"
            )

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

    @staticmethod
    def show_vlan_id(config, vlan):

        vlan = str(vlan)

        if vlan not in config.vlans():

            print(
                f"% VLAN {vlan} does not exist."
            )

            return

        print()

        print(f"VLAN ID : {vlan}")

        print(
            f"Name    : {config.vlans()[vlan]}"
        )

        print("Status  : active")

        print()

    @staticmethod
    def show_interfaces_switchport(
        iface_engine
    ):

        for iface, data in (
            iface_engine.all().items()
        ):

            print()

            print(f"Name: {iface}")

            print()

            print(
                f"Administrative Mode: "
                f"{data['mode']}"
            )

            print(
                f"Operational Mode: "
                f"{data['mode']}"
            )

            print(
                f"Access Mode VLAN: "
                f"{data['access_vlan']}"
            )

            print(
                f"Description: "
                f"{data['description']}"
            )

            print()

    @staticmethod
    def show_interfaces_description(
        iface_engine
    ):

        print()

        print(
            "Interface    Status    Description"
        )

        print(
            "---------    ------    -----------"
        )

        for iface, data in (
            iface_engine.all().items()
        ):

            status = (
                "up"
                if data["admin_up"]
                else "down"
            )

            print(
                f"{iface:<12}"
                f"{status:<10}"
                f"{data['description']}"
            )

        print()
