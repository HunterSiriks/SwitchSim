# SwitchSim

A Cisco-like network switch simulator built in Python CLI.

## Features

- Cisco-style CLI modes
- VLAN management
- Interface configuration
- Running and startup configuration
- MAC address table
- Interface status commands
- Basic switching simulation

## Version History

### v0.3 - Configuration Management Complete
- Added running-config and startup-config
- Added save/load configuration
- Added show running-config
- Added show startup-config

### v0.2 - Interface Engine
- Added interface configuration
- Added interface status commands
- Added switchport access VLAN support

### v0.1 - Initial Release
- Created basic CLI engine
- Added command parser
- Started switch simulation

## Installation

```bash
git clone https://github.com/USERNAME/switchsim.git
cd switchsim
python main.py

# Example Commands

Switch> enable
Switch# show running-config
Switch# configure terminal
Switch(config)# vlan 10
Switch(config-vlan)# name SALES
Switch(config)# interface Fa0/1
Switch(config-if)# switchport access vlan 10
