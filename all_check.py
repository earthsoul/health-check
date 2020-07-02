import os
import shutil
import sys

def check_disk_full(disk,min_gb,min_percentage):
    du = shutil.disk_usage(disk)
    percentage_free = 100*du.free / du.total
    gigabytes_free = du.free / 2*30
    if percentage_free < min_percentage or gigabytes_free < min_gb:
        return True
    return False

def main():
    if check_disk_full(disk = '/',min_gb = 2,min_percentage = 10):
        print("Disk full.")
        sys.exit(1)
    
    print("Everything ok.")
    sys.exit(0)

main()
