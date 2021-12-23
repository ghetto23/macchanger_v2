from os import system as sys
from optparse import OptionParser

usage = "python3 mac_changer.py -i eth0 -m 22:BB:56:CC:23:AA"

parser = OptionParser(usage=usage)

parser.add_option("-i","--interface",help="wireless ise wlan0, kablolu baglanti ise eth0",
                  dest="arayuz")
parser.add_option("-m","--mac",help="yeni mac addresi",dest="mac")

(options, args) = parser.parse_args()

arayuz = options.arayuz
mac = options.mac

sys(f"ifconfig {arayuz} down")
sys(f"ifconfig {arayuz} hw ether {mac}")
sys(f"ifconfig {arayuz} up")

print("\n\tYeni mac addressiniz: {}".format(mac))