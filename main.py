from cli import CLI


def main():
    print("""
====================================
      SwitchSim v0.3
 Cisco IOS CLI Simulator
====================================
""")

    cli = CLI()
    cli.run()


if __name__ == "__main__":
    main()
