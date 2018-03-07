#!/usr/bin/env python

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal
import os
import re


def Main():
    indicator = appindicator.Indicator.new('vpn_status', os.path.abspath('lock.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    indicator.set_label(get_label(), 'VPN Status')
    gtk.main()

def build_menu():
    menu = gtk.Menu()
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def get_label():
    with open('/home/john/nw/vpn/logs/openvpn.log', 'r') as file:
        for line in file:
            if 'Peer Connection with' in line:
                ip_match = re.match(r'AF\_INET\](\w{3}\.\w{3}\.\w{3}\.\w{3})', str(line))
                return ip_match.group(1)
        file.close()

def quit(source):
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Main()
