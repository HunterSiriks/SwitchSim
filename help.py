class UserHelp:

    @staticmethod
    def user():
        print("enable")
        print("exit")
        print("help")
        print("ping")
        print("show")

        print()
        print("Use <command>? to get info")
        print()

    @staticmethod
    def enable():
        print("Enter privileged EXEC mode")

        print()

    @staticmethod
    def exit():
        print("Exit the simulator")

        print()

    @staticmethod
    def ping():
        print("<device-name>")

        print()

    @staticmethod
    def show():
        print("clock")
        print("hostname")
        print("users")
        print("version")

        print()

    @staticmethod
    def clock():
        print("Display system clock")

        print()

    @staticmethod
    def users():
        print("Display active users")

        print()

    @staticmethod
    def version():
        print("Display software version information")

        print()

class PrivHelp:

    @staticmethod ### Privilege
    def privilege():
        print("clear")
        print("configure")
        print("connect-device")
        print("disconnect-device")
        print("ping")
        print("reload")
        print("show")
        print("exit")

        print()

    @staticmethod ###
    def clear():
        print("counters")
        print("mac")

        print()

    @staticmethod
    def counters():
        print("Clear interface counters")

        print()

    @staticmethod
    def mac():
        print("address-table")

        print()

    @staticmethod
    def mac_table():
        print("Clear dynamic MAC address entries")

        print()

    @staticmethod
    def configure():

        print("terminal")

        print()

    @staticmethod
    def conf_t():
        print("Enter configuration mode")

        print()

    @staticmethod
    def connect_device():
        print("<interface> <device-name>")

        print()

    @staticmethod
    def disconnect_device():
        print("<interface>")

        print()

    @staticmethod ###
    def reload():
        print("Reload the switch")

        print()

    @staticmethod ###
    def show():
        print("clock")
        print("devices")
        print("hostname")
        print("interfaces")
        print("mac")
        print("running-config")
        print("startup-config")
        print("users")
        print("version")
        print("vlan")

        print()

    @staticmethod
    def device():
        print("Display connected devices")

        print()

    @staticmethod
    def interfaces():
        print("status")

        print()

    @staticmethod
    def int_status():
        print("Display interface status information")

        print()

    @staticmethod
    def mac_help():
        print("address-table")
        print("count")

        print()

    @staticmethod
    def mac_table():
        print("Display the MAC address table")

        print()

    @staticmethod
    def mac_count():
        print("Display the number of learned MAC addresses")

        print()

    @staticmethod
    def run():
        print("Display current running configuration")

        print()

    @staticmethod
    def start():
        print("Display saved startup configuration")

        print()

    @staticmethod
    def users():
        print("Display active users")

        print()

    @staticmethod
    def vlan():
        print("brief")

        print()

    @staticmethod
    def vlan_brief():
        print("Display VLAN information")

        print()

class GlobelHelp:

    @staticmethod ### Globel
    def conf():
        print("exit")
        print("hostname")
        print("interface")
        print("vlan")

        print()

    @staticmethod
    def exit():
        print("Exit current mode")

        print()

    @staticmethod
    def hostname():
        print("Display switch hostname")

        print()

    @staticmethod
    def interface():
        for i in range(
            1,
            25
        ):

            print(
                f"Fa0/{i}"
            )

        for i in range(
            1,
            3
        ):

            print(
                f"Gi0/{i}"
            )

        print()

    @staticmethod
    def vlan():
        print(
            "<1-4094>  VLAN ID"
        )

        print()
