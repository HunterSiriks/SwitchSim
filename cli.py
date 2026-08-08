import time

import readline

from commands import Commands

from config import Config

from engines.interface import InterfaceEngine

from devices.manager import DeviceManager

from save import copy_running_to_startup

from save import reload_config

from save import erase_startup_config

from save import erase_running_config

from help import UserHelp, PrivHelp, GlobelHelp

class CLI:

    def __init__(self):

        self.config = Config()

        self.hostname = self.config.hostname()
        
        self.start_time = time.time()

        self.mode = "user"

        self.current_vlan = None

        self.iface = InterfaceEngine()
       
        self.devices = DeviceManager()
 
        self.iface.import_data(
            self.config.load_interfaces()
        )

        self.current_interface = None

    def prompt(self):

        if self.mode == "user":
            return f"{self.hostname}> "

        elif self.mode == "privileged":
            return f"{self.hostname}# "

        elif self.mode == "config":
            return f"{self.hostname}(config)# "

        elif self.mode == "config-vlan":
            return f"{self.hostname}(config-vlan)# "

        elif self.mode == "config-if":
            return f"{self.hostname}(config-if)# "

    def uptime(self):

        seconds = int(
            time.time() - self.start_time
        )

        hours = seconds // 3600

        minutes = (
            seconds % 3600
        ) // 60

        seconds = seconds % 60

        return (
            f"{hours}h "
            f"{minutes}m "
            f"{seconds}s"
        )

    def run(self):

        while True:

            cmd = input(self.prompt()).strip()

            if readline.get_current_history_length() > 20:

                readline.remove_history_item(
                    0
                )

            if cmd == "":
                continue

            #
            # USER MODE
            #

            if self.mode == "user":

                if cmd in ["enable", "en"]:

                    self.mode = "privileged"
                
                elif cmd in ["help", "?"]:

                    UserHelp.user()

                elif cmd == "exit":

                    print("Bye!")

                    break

                else:

                    Commands.invalid()

            #
            # PRIVILEGED
            #

            elif self.mode == "privileged":

                if cmd in ["configure terminal", "conf t"]:

                    self.mode = "config"

                elif cmd == "disable":

                    self.mode = "user"
                
                elif cmd in [
                    "show history",
                    "sh history"
                ]:

                    print()

                    for i in range(
                        1,
                        readline.get_current_history_length() + 1
                    ):

                        print(
                            f"{i}  "
                            f"{readline.get_history_item(i)}"
                        )

                elif cmd.startswith("learn-mac "):
                    parts = cmd.split()

                    if len(parts) == 3:

                        self.mac.learn(
                            1,
                            parts[2],
                            parts[1]
                        )

                elif cmd in [
                    "show mac address-table count",
                    "show mac count",
                    "sh mac address-table count",
                    "sh mac count"
                ]:

                    print()

                    print(
                        f"Total MAC Addresses for this criterion: {self.devices.mac_count()}"
                    )

                elif cmd in [
                    "show devices",
                    "sh devices"
                ]:

                    print()


                    print(
                        "Port     Device    MAC Address"
                    )

                    print()

                    for port, device in self.devices.all().items():

                        print(
                            f"{port:<8} "
                            f"{device.name:<8} "
                            f"{device.mac}"
                        )

                elif cmd.startswith(
                    "disconnect-device "
                ):

                    parts = cmd.split()

                    if len(parts) == 2:

                        port = parts[1]

                        self.devices.disconnect(
                            port
                        )

                        print(
                            f"Device disconnected from {port}"
                        )

                elif cmd.startswith(
                    "ping "
                ):

                    parts = cmd.split()

                    if len(parts) == 2:

                        target = parts[1]

                        if self.devices.exists(
                            target
                        ):

                            port = self.devices.get_port(
                                target
                            )

                            if not self.iface.get(
                                port
                            )["admin_up"]:

                                print()

                                print(
                                    "....."
                                )

                                print(
                                    "Success rate is 0 percent (0/5)"
                                )

                            else:

                                self.iface.increment_input(
                                    port
                                )

                                self.iface.increment_output(
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
                                "....."
                            )

                            print(
                                "Success rate is 0 percent (0/5)"
                            )

                elif cmd == "clear counters":

                    self.iface.clear_counters()

                    print()

                    print(
                        "All interface counters cleared"
                    )

                elif cmd in [
                    "show version",
                    "sh ver"
                ]:

                    Commands.show_version()

                elif cmd in [
                    "show uptime",
                    "sh uptime"
                ]:

                    print(
                        f"System uptime: {self.uptime()}"
                    )

                elif cmd in ["show clock", "sh clock"]:

                    Commands.show_clock()

                elif cmd in ["show users", "sh users"]:

                    print()

                    print(
                        "Line       User"
                    )

                    print(
                        "* console  admin"
                    )

                elif cmd in ["show hostname", "sh hostname"]:

                    print()

                    print(
                        f"Hostname: {self.config.hostname()}"
                    )

                elif cmd in ["help", "?"]: ###
                    PrivHelp.privilege()

                elif cmd in ["show?","sh?"]:
                    PrivHelp.show()

                elif cmd == "clear?":
                    PrivHelp.clear()

                elif cmd in ["show vlan brief", "sh vlan", "show vlan"]:

                    Commands.show_vlan()

                elif cmd.startswith("connect-device "):

                    parts = cmd.split()

                    if len(parts) == 3:

                        port = parts[1]

                        name = parts[2]

                        mac = (
                            "0011.2233."
                            + str(
                                len(
                                    self.devices.all()
                                ) + 1
                            ).zfill(4)
                        )

                        if self.devices.connect(
                            port,
                            name,
                            mac
                        ):

                            print(
                                f"Device {name} connected to {port}"
                            )

                        else:

                            print(
                                "Port already has a device connected"
                            )

                    else:

                        Commands.invalid()

                elif cmd.startswith in [
                    "show interface ",
                    "sh interface"
                ]:

                    parts = cmd.split()

                    if len(parts) == 3:

                        iface = parts[2]

                        data = self.iface.get(
                            iface
                        )

                        print()

                        print(
                            f"{iface} is "
                            + (
                                "up"
                                if data["admin_up"]
                                else "down"
                            )
                        )

                        print()

                        print(
                            f"Description: {data['description']}"
                        )

                        print(
                            f"Access VLAN: {data['access_vlan']}"
                        )

                        print()

                        print(
                            f"Input packets : {data['input_packets']}"
                        )

                        print(
                            f"Output packets: {data['output_packets']}"
                        )

                        print(
                            f"Errors        : {data['errors']}"
                        )

                elif cmd.startswith in [
                    "show vlan id",
                    "sh vlan id"
                ]:

                    vlan = int(cmd.split()[-1])

                    Commands.show_vlan_id(
                        self.config,
                        vlan
                    )

                elif cmd in [
                    "show mac address-table",
                    "sh mac",
                    "sh mac address-table",
                    "show mac"
                ]:

                    Commands.show_mac(
                        self.devices
                    )

                elif cmd in [
                    "show interfaces counters",
                    "sh interfaces counters",
                    "sh int counters"
                ]:

                    print()

                    print(
                        "Port     InPkts   OutPkts   Errors"
                    )

                    for iface, data in self.iface.all().items():

                        print(
                            f"{iface:<8} "
                            f"{data.get('input_packets', 0):<8} "
                            f"{data.get('output_packets', 0):<8} "
                            f"{data.get('errors', 0)}"
                        )

                elif cmd == (
                    "clear mac address-table"
                ):

                    self.devices.clear_mac_table()

                    print()

                    print(
                        "MAC address table cleared"
                    )

                elif cmd in ("show ip interface brief", "sh ip int br"):

                    Commands.show_ip_interface_brief()
                   
                elif cmd in [
                    "show interfaces status",
                    "sh int status",
                    "show int status",
                    "sh interface status"
                ]:

                    Commands.show_interfaces_status(
                       self.iface
                    )

                elif cmd in [
                    "show interfaces switchport",
                    "sh int switchport",
                    "show int switchport",
                    "sh interface switchport"
                ]:

                    Commands.show_interfaces_switchport(
                       self.iface
                    )

                elif cmd in [
                    "show interfaces description",
                    "sh int desc",
                    "show int desc",
                    "sh interface desc",
                    "sh int description",
                    "show interface desc",
                    "sh interface description"
                ]:

                    Commands.show_interfaces_description(
                       self.iface
                    )

                elif cmd in [
                    "show running-config",
                    "sh run",
                    "show run",
                    "sh running-config"
                ]:

                    Commands.show_running_config(
                       self.config,
                       self.iface
                    )

                elif cmd in [
                "copy running-config startup-config",
                "copy run start"
                ]:

                    copy_running_to_startup()

                elif cmd in ("write memory", "wr"):

                    copy_running_to_startup()

                elif cmd in [
                "show startup-config",
                "sh start",
                "show start",
                "sh startup-config"
                ]:

                    Commands.show_startup_config(
                        self.config
                    )

                elif cmd in [
                    "erase startup-config",
                    "erase start"
                ]:

                    erase_startup_config()

                elif cmd in [
                    "erase running-config"
                    "erase run"
                ]:

                    erase_running_config()

                    self.config.load()

                    self.hostname = (
                        self.config.hostname()
                    )

                    self.iface.import_data(
                        self.config.load_interfaces()
                    )

                elif cmd in ("write erase", "we"):

                    erase_running_config()

                    self.config.load()

                    self.hostname = (
                        self.config.hostname()
                    )

                    self.iface.import_data(
                        self.config.load_interfaces()
                    )

                elif cmd in ["reload", "rel"]:

                    if reload_config():

                        self.config.load()

                        self.hostname = (
                            self.config.hostname()
                        )

                        self.iface.import_data(
                            self.config.load_interfaces()
                        )

                elif cmd == "exit":

                    print("Bye!")

                    break

                else:

                    Commands.invalid()

            #
            # CONFIG MODE
            #

            elif self.mode == "config":

                if cmd == "end":

                    self.mode = "privileged"

                elif cmd == "exit":

                    self.mode = "privileged"

                else:

                    parts = cmd.split()

                    if len(parts) == 0:
                        continue

                    if parts[0] == "hostname":

                        if len(parts) > 1:

                            self.hostname = parts[1]

                            self.config.set_hostname(parts[1])

                    elif cmd in ["help", "?"]:
                        GlobelHelp.conf()

                    elif cmd.startswith("vlan "):

                        vlan = int(cmd.split()[1])

                        if vlan < 1 or vlan > 4094:

                            print(
                                "% Invalid VLAN ID"
                            )

                        else:

                            self.config.add_vlan(vlan)

                            self.current_vlan = vlan

                            self.mode = "config-vlan"

                    elif cmd.startswith("no vlan "):

                        vlan = int(cmd.split()[-1])

                        result = self.config.remove_vlan(vlan)

                        if result is True:

                            print(f"VLAN {vlan} deleted.")

                        elif result is False:

                            print("% Default VLAN 1 cannot be deleted.")

                        else:

                            print(f"% VLAN {vlan} does not exist.")

                    elif (
                        cmd.startswith("interface ")
                        or
                        cmd.startswith("int ")
                    ):


                       if len(parts) > 1:

                         iface = parts[1]

                         iface = iface.replace("fa", "Fa")
                         iface = iface.replace("gi", "Gi")

                         if self.iface.exists(iface):

                            self.current_interface = iface

                            self.mode = "config-if"

                         else:

                            print("% Invalid input detected at '^' marker.")

                    elif (
                        cmd.startswith("default interface ")
                        or
                        cmd.startswith("def int ")
                    ):

                        if cmd.startswith in [
                            "default interface ",
                            "def int",
                            "def interface",
                            "deefault int"
                        ]:

                            iface = cmd[18:]

                        else:

                            iface = cmd[8:]

                        iface = iface.replace(
                            "fa",
                            "Fa"
                        )

                        iface = iface.replace(
                            "gi",
                            "Gi"
                        )

                        if self.iface.exists(
                            iface
                        ):

                            self.iface.default_interface(
                                iface
                            )

                            self.config.save_interface(
                                iface,
                                self.iface.get(iface)
                            )

                        else:

                            Commands.invalid()

            #
            # VLAN MODE
            #

            elif self.mode == "config-vlan":

                if cmd.startswith("name "):

                    name = cmd[5:]

                    self.config.set_vlan_name(self.current_vlan, name)

                elif cmd == "exit":

                    self.mode = "config"

                elif cmd == "end":

                    self.mode = "privileged"

                else:

                    Commands.invalid()
            
            elif self.mode == "config-if":

                if cmd == "exit":
                    self.mode = "config"

                elif cmd == "end":
                    self.mode = "privileged"

                elif cmd.startswith in [
                    "description ",
                    "desc"
                ]:

                    self.iface.set_description(
                        self.current_interface,
                        cmd[12:]
                    )

                    self.config.save_interface(
                        self.current_interface,
                        self.iface.get(self.current_interface)
                    )

                elif cmd in [
                    "no description",
                    "no desc"
                ]:

                    self.iface.set_description(
                        self.current_interface,
                        ""
                    )

                    self.config.save_interface(
                        self.current_interface,
                        self.iface.get(
                            self.current_interface
                        )
                    )

                    print(
                        f"Description removed from "
                        f"{self.current_interface}"
                    )

                elif cmd == "shutdown":

                    self.iface.shutdown(
                        self.current_interface
                    )

                    self.config.save_interface(
                        self.current_interface,
                        self.iface.get(self.current_interface)
                    )

                elif cmd == "no shutdown":

                    self.iface.no_shutdown(
                        self.current_interface
                    )

                    self.config.save_interface(
                        self.current_interface,
                        self.iface.get(self.current_interface)
                    )

                elif cmd.startswith("switchport access vlan "):

                    vlan = int(cmd.split()[-1])

                    if self.config.vlan_exists(vlan):

                        self.iface.set_access_vlan(
                            self.current_interface,
                            vlan
                        )

                    else:

                        print(
                            "% VLAN does not exist"
                        )
                else:

                     Commands.invalid()
