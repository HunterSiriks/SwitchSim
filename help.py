class Help:

    @staticmethod
    def show():

        print()

        print("Available Commands")
        print("------------------")

        print("enable                 Enter privileged mode")
        print("configure terminal     Enter configuration mode")
        print("hostname <name>        Change hostname")
        print("vlan <id>              Create VLAN")
        print("interface <name>       Enter interface mode")

        print()

        print("show running-config    Display running config")
        print("show startup-config    Display startup config")
        print("show interfaces status Display interface status")
        print("show vlan              Display VLANs")

        print()

        print("copy running-config startup-config")
        print("write memory")
        print("wr")
        print("erase startup-config")
        print("erase running-config")
        print("write erase")
        print("we")
        
        print()
