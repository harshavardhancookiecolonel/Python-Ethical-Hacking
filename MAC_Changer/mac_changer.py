import subprocess 
import argparse 
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="This program changes the MAC address to a custom one")
    parser.add_argument ("-1", "--interface", dest="interface", help="Interface to change the MAC address")
    parser.add_argument ("-m", "--mac", dest="new_mac", help="Custom MAC address you want to change it to")
    args = parser.parse_args ()
    if not args. interface:
        parser.error ("[-) Please specify interface use --help/-h for info") 
    elif not args.new_mac:
        parser.error ("[-) Please specify new_mac use --mac/-m for info")
    return args
    
def change_mac (interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"] ) 
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac (interface):
    ifconfig_result = subprocess. check_output(["ifconfig", interface])
    search_result = re.search(r"\w\w: \w\w: \w\w: \w\w: \w\w: \w\w", str(ifconfig_result))
    if search_result:
        return search_result. group (0)
    else:
        print("[-] Could not read MAC address")
        
args = get_arguments()

current mac = get_current _mac(args. interface)
print("Current MAC" + str(current mac))

change_mac (args. interface, args. new_mac)

current_mac = get_current_mac (args. interface)
if current_mac == args.new_mac:
print(" [+] MAC address changed to " + current_mac)
else:
print("[-] MAC address did not get changed")
