#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal
import os
import subprocess

APPINDICATOR_ID = 'vpn_status'
VPN_IP = ''
VPN_STATUS = ''

def Main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('lock.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    start_vpn()
    indicator.set_label('IP: ' + VPN_IP, 'VPN Status')
    gtk.main()

def start_vpn():
    os.chdir('/home/john/nw/vpn/configs')
    vpn_cmd = subprocess.Popen('sudo openvpn --config ipvanish-US-Dallas-dal-a10.ovpn > /home/john/nw/vpn/logs/openvpn.log', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def get_status():
    with open("/home/john/nw/vpn/logs/openvpn.log", "r") as file:
        for line in file:
            print(line)
            if 'Peer Connection with [AF_INET]' in line:
                ip_match = re.match(r'AF\_INET\](\w{3}\.\w{3}\.\w{3}\.\w{3})', line)
                VPN_IP = ip_match.group()

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_vpn = gtk.MenuItem('VPN')
    item_quit.connect('activate', quit)
    menu.append(item_vpn)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Main()
