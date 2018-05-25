This is a walk through note for the data flow, 2018/05/24. Contact info: weihua19900704@gmail.com <br />

### platform: multiple vms

To check system healthiness with chassis manager, go to http://192.168.7.8:8500 <br />
To monitor the data flow with Kibana, go to http://192.168.7.11:5601 <br />

### platform: personal vm, single machine
VMWare, CentOS. 192.168.7.114. <br />

### platform setup

#### clear network environment
Note, CentOS will firewall will pick up back the ip/port rules from time to time... So disable it and then flush iptable. <br />
```
systemctl disable firewalld
iptables -F
```

#### git
```bash
sudo yum install git
```
Then set up ssh key on the vm following [this link](https://help.github.com/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent/) and [this link](https://help.github.com/articles/adding-a-new-ssh-key-to-your-github-account/). <br />

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
We should have all containers running. <br />

### pcap workflow
process your pcap file with collector container: <br />
```bash
cp youpcapfile.pcap /opt/helios/bro/spool/
docker exec -it collector bash
bro -r /usr/local/spool/youpcapfile.pcap /usr/local/share/bro/site/local.bro
```

check ELK log processing workflow with Kibana: go to browser, 192.168.7.114. user name: elastic, password: helios12$ <br />
check the log processing result in postgre db: <br />
```bash
docker exec -it docker_db_1 bash
psql -U helios helios
\dt
select * from conn limit 5;
```
