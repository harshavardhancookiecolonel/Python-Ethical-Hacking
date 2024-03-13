import subprocess
import argparse
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="This program changes the MAC address to a custom one")
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change the mac_address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="Custom mac address you wnat to chan")
