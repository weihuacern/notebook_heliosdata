This is a walk through note for the data flow, 2018/05/24. Contact info: weihua19900704@gmail.com

### platform: multiple vms

To check system healthiness with chassis manager, go to http://192.168.7.8:8500
To monitor the data flow with Kibana, go to http://192.168.7.11:5601

### platform: personal vm, single machine
VMWare, CentOS. 192.168.7.114.

### platform setup

#### clear network environment
Note, CentOS will firewall will pick up back the ip/port rules from time to time... So disable it and then flush iptable
```
systemctl disable firewalld
iptables -F
```

#### git
```bash
sudo yum install git
```

#### docker
```bash
cd ~
git clone git@github.com:yourgithubid/helios.git
cd helios/helios/platform
sudo ./docker_install.sh Linux x86_64
```

### containers setup
```bash
cd ~
cd helios/
make
sudo ./start_local.sh run
```
We should have all containers running. 

### pcap workflow
process your pcap file with collector container:
```bash
cp youpcapfile.pcap /opt/helios/bro/spool/
docker exec -it collector bash
bro -r /usr/local/spool/youpcapfile.pcap /usr/local/share/bro/site/local.bro
```

check ELK log processing workflow with Kibana: go to browser, 192.168.7.114. user name: elastic, password: helios12$

check the log processing result in postgre db:
```bash
docker exec -it docker_db_1 bash
psql -U helios helios
\dt
select * from conn limit 5;
```
