class Help:

    @staticmethod
    def show():

        print()

        print("          Available Commands          ")
        print("--------------------------------------")

        print()

        print("-- USER EXEC MODE (>)")
        print("enable                 Enter privileged mode")
        print("help                   Display help")

        print()

        print("-- PRIVILEGED EXEC MODE (#)")
        print("disable                Return to user mode")
        print("configure terminal     Enter configuration mode")
        print("show running-config    Display running config")
        print("show startup-config    Display startup config")
        print("show version           Display version")
        print("show uptime            Display uptime")
        print("show clock             Display clock")
        print("show vlan              Display VLANs")
        print("show interfaces status Display interface status")
        print("show mac address-table Display MAC table")

        print()

        print("-- CONFIG MODE (config)#")
        print("hostname <name>        Change hostname")
        print("vlan <id>              Create VLAN")
        print("no vlan <id>           Delete VLAN")
        print("interface <name>       Enter interface mode")
        print("default interface      Reset interface")

        print()

        print("-- INTERFACE MODE (config-if)#")
        print("description <text>")
        print("switchport access vlan <id>")
        print("shutdown")
        print("no shutdown")

        print()
