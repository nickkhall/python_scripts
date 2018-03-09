#!/usr/bin/env bash

clear

echo About to execute script...

sleep 1

echo Starting client...

sleep 2

python3 ./tcp_client.py 127.0.0.1 3333

sleep 1

echo Client running..

# sudo lsof -i :3333
