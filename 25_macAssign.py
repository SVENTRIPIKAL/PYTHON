"""
    Program allows user to
    manually spoof MAC address.
"""

#!/usr/bin/env python

import subprocess, optparse, re


def parse_Options():
    parser = optparse.OptionParser() ;
    parser.add_option("-i", "--interface", dest="interface", help="interface to modify MAC address") ;
    parser.add_option("-m", "--mac", dest="new_address", help="new MAC address") ;
    (options, arguments) = parser.parse_args() ;
    if (options.interface == None):
        options.interface = input("\nInterface >> ") ;
    if ( not (options.interface) or not (options.interface == 'eth0') and not (options.interface == 'lo') ):
        parser.error("\n[!] Please specify a valid interface; use --help for more info.\n") ;
    if (options.new_address == None):
        options.new_address = input("\nMAC Address >> ") ;
    if not (options.new_address):
        parser.error("\n[!] Please specify a valid MAC address; use --help for more info.\n") ;
    return options ;

def assign_Address():
    global interface, new_address, old_address ;
    if (new_address == old_address):
        print(f"\n[!] Similar MAC address requested -- No changes assigned to \"{interface}\" interface\n") ;
    else:
        print(f"\n[+] Changing MAC address for \"{interface}\" interface -- from ({old_address}) to ({new_address})\n") ;
        subprocess.call(["ifconfig", interface, "down"]) ;
        subprocess.call(["ifconfig", interface, "hw", "ether", new_address]) ;
        subprocess.call(["ifconfig", interface, "up"]) ;
        subprocess.call(["ifconfig"]) ;

def analyze_Result( result ):
    global interface, old_address ;
    if not (result == None):
        old_address = result.group(0) ;
        assign_Address() ;
    else:
        print(f"\n[!] No MAC address found for \"{interface}\" interface\n") ;


options = parse_Options() ;     interface = options.interface ;     new_address = options.new_address ;

output = subprocess.check_output(["ifconfig", interface]) ;         output = output.decode("utf-8") ;

result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output) ;      analyze_Result( result ) ;