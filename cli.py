import time

from commands import Commands

from config import Config

from engines.interface import InterfaceEngine

from save import copy_running_to_startup

from save import reload_config

from save import erase_startup_config

from save import erase_running_config

from help import Help

class CLI:

    def __init__(self):

        self.config = Config()

        self.hostname = self.config.hostname()
        
        self.start_time = time.time()

        self.mode = "user"

        self.current_vlan = None

        self.iface = InterfaceEngine()
        
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

            if cmd == "":
                continue

            #
            # USER MODE
            #

            if self.mode == "user":

                if cmd in ["enable", "en"]:

                    self.mode = "privileged"
                
                elif cmd == "help":

                    Help.show()

                elif cmd == "?":

                    Help.show()

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

                elif cmd in ["show version", "sh ver"]:

                    Commands.show_version()

                elif cmd == "show uptime":

                    print(
                        f"System uptime: {self.uptime()}"
                    )

                elif cmd in ["show clock", "sh clock"]:

                    Commands.show_clock()

                elif cmd in ["help", "?"]:

                    Help.show()

                elif cmd in ["show vlan brief", "sh vlan", "show vlan"]:

                    Commands.show_vlan()

                elif cmd.startswith("show vlan id "):

                    vlan = int(cmd.split()[-1])

                    Commands.show_vlan_id(
                        self.config,
                        vlan
                    )

                elif cmd in ["show mac address-table", "sh mac"]:

                    Commands.show_mac()

                elif cmd in ("show ip interface brief", "sh ip int br"):

                    Commands.show_ip_interface_brief()
                   
                elif cmd in ["show interfaces status", "sh int status"]:

                    Commands.show_interfaces_status(
                       self.iface
                    )

                elif cmd in [
                    "show interfaces switchport",
                    "sh int switchport"
                ]:

                    Commands.show_interfaces_switchport(
                       self.iface
                    )

                elif cmd in [
                    "show interfaces description",
                    "sh int desc"
                ]:

                    Commands.show_interfaces_description(
                       self.iface
                    )

                elif cmd in ("show running-config", "sh run"):
                
                    Commands.show_running_config(
                       self.config,
                       self.iface
                    )
                
                elif cmd in ["copy running-config startup-config", "copy run start"]:

                    copy_running_to_startup()
                
                elif cmd in ("write memory", "wr"):
                
                    copy_running_to_startup()

                elif cmd in ["show startup-config", "sh start"]:

                    Commands.show_startup_config(
                        self.config
                    )

                elif cmd == "erase startup-config":

                    erase_startup_config()
                
                elif cmd == "erase running-config":

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

                        if cmd.startswith(
                            "default interface "
                        ):

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

                elif cmd.startswith("description "):

                    self.iface.set_description(
                        self.current_interface,
                        cmd[12:]
                    )

                    self.config.save_interface(
                        self.current_interface,
                        self.iface.get(self.current_interface)
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
