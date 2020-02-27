#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal
import os
import subprocess

APPINDICATOR_ID = 'openvpn_cli-client'
VPN_IP = ''
VPN_STATUS = ''
VPN_COMMAND = None

def Main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('lock.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    start_vpn()
    get_status(indicator)
    gtk.main()

def start_vpn():
    os.chdir('/home/john/nw/vpn/configs')
    VPN_COMMAND = subprocess.Popen('sudo openvpn --config ipvanish-US-Dallas-dal-a10.ovpn > /home/john/nw/vpn/logs/openvpn.log', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def get_status(ind):
    with open("/home/john/nw/vpn/logs/openvpn.log", "r") as file:
        for line in file:
            print(line)
            if 'Peer Connection with [AF_INET]' in line:
                ip_match = re.match(r'AF\_INET\](\w{3}\.\w{3}\.\w{3}\.\w{3})', line)
                ind.set_label('IP: ' + ip_match.group(1), 'VPN Status')
                return
        file.close()


def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def quit(source):
    gtk.main_quit()
    os.killpg(os.getpgid(VPN_COMMAND.pid), signal.SIGTERM)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Main()
