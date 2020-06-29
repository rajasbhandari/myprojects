import subprocess
import optparse

parser= optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface which you would like to change")
parser.add_option("-m", "--mac_address", dest="new_mac", help="desired MAC address")

option,_ = parser.parse_args()

interface=option.interface
new_mac=option.new_mac

print("[+] changing mac address to", new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig",interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] changed to ",new_mac)

