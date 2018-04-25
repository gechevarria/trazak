Proof of concept for TRAZAK usin the following technologies:

CONPOT(https://github.com/mushorg/conpot)
HoneyPot to simulate industrial environments
Steps to set up an running.
1. Install Docker
2. Run docker pull honeynet/conpot
3. Run docker run -it -p 80:80 -p 102:102 -p 502:502 -p 161:161/udp --network=bridge honeynet/conpot:latest /bin/sh
4. Finally run conpot --template default

PLCSCAN (https://github.com/meeas/plcscan)
Python tool to extract devices information by using p7 and modbus protocols.
Open Pycharm and execute plcscan_trazak.py by setting an IP or a set of IPs