from commands import Commands
from config import Config
from engines.interface import InterfaceEngine

class CLI:

    def __init__(self):

        self.config = Config()

        self.hostname = self.config.hostname()

        self.mode = "user"

        self.current_vlan = None

        self.iface = InterfaceEngine()

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

    def run(self):

        while True:

            cmd = input(self.prompt()).strip()

            if cmd == "":
                continue

            #
            # USER MODE
            #

            if self.mode == "user":

                if cmd == "enable":

                    self.mode = "privileged"

                elif cmd == "exit":

                    print("Bye!")

                    break

                else:

                    Commands.invalid()

            #
            # PRIVILEGED
            #

            elif self.mode == "privileged":

                if cmd in ("configure terminal", "conf t"):

                    self.mode = "config"

                elif cmd == "disable":

                    self.mode = "user"

                elif cmd == "show version":

                    Commands.show_version()

                elif cmd == "show vlan brief":

                    Commands.show_vlan()

                elif cmd == "show mac address-table":

                    Commands.show_mac()

                elif cmd == "show ip interface brief":

                    Commands.show_ip_interface_brief()
                   
                elif cmd == "show interfaces status":

                    Commands.show_interfaces_status(
                       self.iface
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

                    elif parts[0] == "vlan":

                        if len(parts) > 1:

                            self.current_vlan = parts[1]

                            self.config.add_vlan(parts[1])

                            self.mode = "config-vlan"

                    elif parts[0] == "interface":

                       if len(parts) > 1:

                         iface = parts[1]

                         iface = iface.replace("fa", "Fa")
                         iface = iface.replace("gi", "Gi")

                         if self.iface.exists(iface):

                            self.current_interface = iface

                            self.mode = "config-if"

                         else:

                            print("% Interface does not exist")

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

                elif cmd == "shutdown":

                  self.iface.shutdown(
                  self.current_interface
                  )

                elif cmd == "no shutdown":

                  self.iface.no_shutdown(
                  self.current_interface
                  )

                elif cmd.startswith("switchport access vlan "):

                  vlan = int(cmd.split()[-1])

                  self.iface.set_access_vlan(
                  self.current_interface,
                  vlan
                  )

                else:
                  print("% Invalid command")
