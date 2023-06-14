#!/usr/bin/env python3

import os
import sys
import shutil
import sys



def check_reboot():
    
    """Returns True if the computer has a pending reboot."""
    
    return os.path.exist('/run/reboot-required')


def check_disk_usage(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false other wise."""
    du=shutil.disk_usage(disk)

    #Calculate the percentage of free space

    percent_free=100*du.free/du.total
    
    #Calculate how many gigabytes

    gigabytes_free=du.free/2**30
    if percent_free < min_percent or gigabytes_free <min_gb:
        return False
    return True 

if not check_disk_usage('/', 2, 10):
    print('ERROR! Not enough disk space.')
    sys.exit(1)
print('Everything OK.')
sys.exit(0)


def check_root_full():
    """Returns True if the root partition is full, False otherwise"""
    return check_disk_full("/", 2, 10)




def main():
    checks=[
            (check_reboot, "Pending reboot"),
            (check_root_full, "Root partition full")
            ]

    everything_ok=True
    for check, msg in checks:
        if check():
            print(msg)
            everything_ok=False
    if not everything_ok:
        sys.exit(1)
    
    print("Everything Ok!")
main()



