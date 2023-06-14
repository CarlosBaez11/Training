#!/usr/bin/env python3

import shutil
import sys

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

