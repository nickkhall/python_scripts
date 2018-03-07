#!/usr/bin/env bash

echo Pick a server number from 01 to 36
read SERVER_NUMBER

echo Let me spin up an openvpn session for you, please hold...

sleep 1

cd /home/john/nw/vpn/configs

xterm -e "sudo openvpn --script-security 2 --config ipvanish-US-Dallas-dal-a$SERVER_NUMBER.ovpn --tun-mtu-extra 0 > /home/john/nw/vpn/logs/openvpn.log"
sleep 20
xterm -e "cd /home/john/projects/github/py/python_scripts/linux_app_indicator && python3 ./indicator.py"
