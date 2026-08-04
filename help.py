class Help:

    @staticmethod
    def user():
        print()

        print("enable")
        print("exit")
        print("help")
        print("ping")
        print("show")

    @staticmethod ###
    def privillage():

        print()

        print("clear")
        print("configure")
        print("connect-device")
        print("disconnect-device")
        print("ping")
        print("reload")
        print("show")
        print("exit")

    @staticmethod ###
    def clear():

        print()

        print("counters")
        print("mac")

    @staticmethod
    def configure():
        print()

        print("terminal")

    @staticmethod
    def connect_device():
        print()

        print("<interface> <device-name>")

    @staticmethod
    def disconnect_device():
        print()

        print("<interface>")

    @staticmethod
    def ping():
        print()

        print("<device-name>")

    @staticmethod ###
    def reload():

        print()

        print("Reload the switch")

    @staticmethod ###
    def show():

        print()

        print("clock")
        print("devices")
        print("hostname")
        print("interface")
        print("interfaces")
        print("mac")
        print("running-config")
        print("startup-config")
        print("users")
        print("version")
        print("vlan")

    @staticmethod
    def mac_help():

        print()

        print("address-table")
        print("count")

    @staticmethod ###
    def exit():

        print()

        print("Exit current mode")
