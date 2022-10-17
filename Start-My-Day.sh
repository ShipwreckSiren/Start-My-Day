#!/bin/bash

echo "Hello, ShipwreckSiren. Your current working directory is: $(pwd). Initializing firewall login."

cd "C:\cygwin64\home\a_user\bin"

python firewall-login.py

wait

python expo-launch.py

echo "Login complete."

chmod 711 start-my-day.sh
