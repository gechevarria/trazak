Proof of concept for TRAZAK usin the following technologies (included some useful commands for each product)

PYTHON
Create virtual environments in order to select the most appropiate for each module
virtualenv <DIR>
source <DIR>/bin/activate

DOCKER
Installation -> https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
sudo docker image ls
sudo docker container ls


CONPOT(https://github.com/mushorg/conpot)
HoneyPot to simulate industrial environments
Steps to set up an running.
1. Install Docker
2. Run docker pull honeynet/conpot
3. Run docker run -it -p 80:80 -p 102:102 -p 502:502 -p 161:161/udp --network=bridge honeynet/conpot:latest /bin/sh
4. Finally run "conpot --template default"

PLCSCAN (https://github.com/meeas/plcscan)
Python tool to extract devices information by using p7 and modbus protocols.
Open Pycharm and execute plcscan_trazak.py by setting an IP or a set of IPs

MARIADB (https://mariadb.org/)
Relational database to store the devices' information.
Installation -> https://www.tecmint.com/install-mariadb-in-ubuntu-and-debian/  -> NOT THE DEFAULT  (dveaber doesnt work)
Execute script after creating database.
mysql -u root -p
CREATE DATABASE trazak;
use trazak;
show tables;

PATTON (https://patton-server.readthedocs.io/en/latest/docker.html)
Run as docker container along with a container for a posgree database (with persistence -> http://tleyden.github.io/blog/2017/06/14/running-postgresql-in-docker/)
sudo docker run -d -p 5432:5432 -e POSTGRES_USER=patton -e POSTGRES_DB=patton -v /home/trazak/Database/:/var/lib/postgresql/data postgres:10.1
sudo docker run --rm -e BACKLOG=512 -e LISTEN_PORT=8080 -e POSTGRES_USER=postgres -p 8080:8080 bbvalabs/patton-server
#to enter PostgreSQL command line terminal
sudo docker exec -it 8df4b330ba46 psql -U postgres
SELECT * FROM pg_catalog.pg_tables;

