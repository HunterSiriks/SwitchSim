import os
import json
import shutil

def copy_running_to_startup():

    shutil.copy(
        "configs/running.json",
        "configs/startup.json"
    )

    print("[OK]")

def erase_startup_config():

    if os.path.exists(
        "configs/startup.json"
    ):

        os.remove(
            "configs/startup.json"
        )

        print("[OK]")

    else:

        print(
            "% Startup configuration not found"
        )

def reload_config():

    if not os.path.exists(
        "configs/startup.json"
    ):

        print(
            "% Startup configuration not found"
        )

        return False

    shutil.copy(
        "configs/startup.json",
        "configs/running.json"
    )

    print("Reloading...")

    return True

def erase_running_config():

    default_config = {
        "hostname": "switch",
        "vlans": {
            "1": "default"
        },
        "interfaces": {},
        "mac_table": [],
        "routes": []
    }

    with open(
        "configs/running.json",
        "w"
    ) as f:

        json.dump(
            default_config,
            f,
            indent=4
        )

    print(
        "[OK] Running configuration erased"
    )
