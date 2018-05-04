Proof of concept for TRAZAK usin the following technologies (included some useful commands for each product)

PYTHON
Create virtual environments in order to select the most appropiate for each module
virtualenv <DIR>
source <DIR>/bin/activate

DOCKER
Installation -> https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce
sudo apt-get intall docker-compose
sudo docker image ls
sudo docker container ls
sudo docker stop <container-name>
docker rm <container-name>
docker rmi <image-name>
sudo docker inspect container
sudo docker start <container-name>
sudo docker ps -a -> to check all the containers

CONPOT(https://github.com/mushorg/conpot)
HoneyPot to simulate industrial environments
Steps to set up an running.
1. Install Docker
2. Run docker pull honeynet/conpot
3. Run (only first time, then docker start <component-name>) docker run --name=HONEYPOT_CONPOT_CONTAINER -it -p 80:80 -p 102:102 -p 502:502 -p 161:161/udp --network=bridge honeynet/conpot:latest /bin/sh
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

PATTON (https://patton-server.readthedocs.io/en/latest/quickstart.html)
Install patton-server:
1. First create a python 3.6 environment
2. https://patton-server.readthedocs.io/en/latest/quickstart.html#first-of-run-patton-server
3. In case there are problems in the installation, execute:
   sudo apt-get install python3.6-dev libmysqlclient-dev
   after that I activate the virtual environment and execute the following command
   pip3 install mysqlclient
Patton Server main commands:
- patton-server serve
- patton-server update-db (NIST releases new vulnerability information around 2 hours)


Container for Postgree database (with persistence -> http://tleyden.github.io/blog/2017/06/14/running-postgresql-in-docker/ -> stores the database in the host, not in the container)
start POSTGRES container-> sudo docker run --name=POSTGRESDB_CONTAINER --hostname=localhost -d -p 5432:5432 -e POSTGRES_USER=patton -e POSTGRES_DB=patton -v /home/trazak/Database/:/var/lib/postgresql/data postgres:10.1
*** check the host where POSTGRES_CONTAINER is runnig in order to start PATTON_SERVER_CONTAINER properly (sudo docker inspect POSTGRES_CONTAINER -> IPAddress parameter) -> POSTGRES_HOST=172.17.0.2

#to enter PostgreSQL command line terminal
sudo docker exec -it POSTGRES_CONTAINER psql -U postgres
SELECT * FROM pg_catalog.pg_tables;
show databases
SELECT datname FROM pg_database
WHERE datistemplate = false;

show tables
SELECT table_schema,table_name
FROM information_schema.tables
ORDER BY table_schema,table_name;

Tables related to Patton
select * from vuln_product;
select * from vuln;
select * from prod;
select * from prod_reference;
select * from cpe23;
select * from cpe_norm;

(these sentences can also be executed through PGADMIN4)


PGADMIN 4 to administer PostgreSQL
sudo docker pull dpage/pgadmin4
sudo docker run -p 80:80 --name=PGADMIN4_CONTAINER -e "PGADMIN_DEFAULT_EMAIL=gmeva@yahoo.es" -e "PGADMIN_DEFAULT_PASSWORD=trazak" -d dpage/pgadmin4

POSTMAN to call PATTON SERVER API via REST
Installation
wget https://dl.pstmn.io/download/latest/linux64 -O postman.tar.gz
sudo tar -xzf postman.tar.gz -C /opt
rm postman.tar.gz
sudo ln -s /opt/Postman/Postman /usr/bin/postman