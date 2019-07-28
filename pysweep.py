#!/usr/bin/python3

import subprocess
import ipaddress
import os

ip_target = '13.224.2.24' 
#response = os.system("fping -a, -C 5, -q, {}!".format (ip_target))

def main():
    #if ip in ip_target:
    #sub_ip = subprocess.run(['fping', '-a', '-C 5', '-q', ip_target])
    sub_ip = subprocess.run(['fping', '-a', '-C 5', '-q', ip_target], capture_output=True)
    with open('ip_target.txt', 'w') as f:
        f.write(str(sub_ip.stderr))   
    print(sub_ip.stdout)
    print(sub_ip)

if __name__ == '__main__':
    main()
#if response == 0:
#    print(ip_target, 'is up')
#else:
#    print(ip_target, 'is down')
