This is a walk through note for the data flow, 2018/05/24. Contact info: weihua19900704@gmail.com <br />

### platform: multiple VMs

Hua-test-192.168.7.114, Password: 0*867#16?6 <br />
Hua-test-192.168.7.143
- Setup VMs at vCenter: 192.168.7.2, administrator@vsphere.local, Helios123$ <br />
New vCenter: 192.168.7.98, administrator@vsphere.local, Helios12$ <br />
Setup the whole system in hybrid mode: mgmt and one collector on one hypervisor, the second collector, connector, analytics and mle on the other hypervisor. <br />
For collector, it need to get access to both management interface and traffic interface. Therefore we need to configure two different port groups with two VMNICs for the collector VMs before we install and configure with wizard. <br />

Some notes to setup ip after VM and Ops installed: <br />
```bash
dhclient ens192
/etc/sysconfig/network-scripts/ifcfg-ens192
```

- Setup all VMs with corresponding docker composes. management go first, then connector, then collectors, then analytics or mle. <br />
Some special tips: 
    - The docker_install.sh, it is very likely to get timeout at the step to add docker.repo into yum. If this happens, install docker by hand first. <br />
    - Keep an eye on the installation log, make sure every step have been processed successfully. <br />
    - Also, make sure to type in the password in time, otherwise we will have certification failure. <br />

```bash
make install INSTALL_TYPE=management INSTALL_ADDR=192.168.7.14
make install INSTALL_TYPE=connector INSTALL_ADDR=192.168.7.15
make install INSTALL_TYPE=collector INSTALL_ADDR=192.168.7.16
make install INSTALL_TYPE=analytics INSTALL_ADDR=192.168.7.17
make install INSTALL_TYPE=mle INSTALL_ADDR=192.168.7.18
make install INSTALL_TYPE=collector INSTALL_ADDR=192.168.7.19
bin/x-pack/setup-passwords interactive
```
To check system healthiness with chassis manager, go to http://192.168.7.8:8500 <br />
To monitor the data flow with Kibana, go to http://192.168.7.11:5601 <br />

Update since June 7th, 2018: root, haie123 (192.168.7.3 or 192.168.7.4) <br />

Rest the whole system by June 11th, 2018: <br />

| Node name                          | Hypervisor | CPU | Memory | Storage |
|------------------------------------|------------|-----|--------|---------|
|management-192.168.7.14             | 192.168.7.4|  2  |   4GB  |   32GB  |
|connector-192.168.7.15              | 192.168.7.3|  2  |   4GB  |   32GB  |
|collector-192.168.7.16              | 192.168.7.3|  2  |   4GB  |   32GB  |
|analytics-192.168.7.17              | 192.168.7.3|  2  |   4GB  |  128GB  |
|machine-learning-engine-192.168.7.18| 192.168.7.3|  2  |   4GB  |  128GB  |
|collector-192.168.7.19              | 192.168.7.4|  2  |   4GB  |   32GB  |

Note, We need to increase the collector size to 64GB, due to the large fuzzy app. <br />

### platform: personal vm, single machine
VMWare, CentOS. 192.168.7.114. <br />

### platform setup

#### clear network environment
Note, CentOS will firewall will pick up back the ip/port rules from time to time... So disable it and then flush ip-table. <br />
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

### pcap work-flow
process your pcap file with collector container: <br />
```bash
cp youpcapfile.pcap /opt/helios/bro/spool/
docker exec -it collector bash
bro -r /usr/local/spool/youpcapfile.pcap /usr/local/share/bro/site/local.bro
```

check ELK log processing work-flow with Kibana: go to browser, 192.168.7.114. user name: elastic, password: helios12$ <br />
check the log processing result in postgre db: <br />
```bash
docker exec -it docker_db_1 bash
psql -U helios helios
\dt
select * from conn limit 5;
drop schema public cascade;
```

### Clear reset
delete all containers and images: <br />
```bash
docker rm $(docker ps -a -q)
docker rmi $(docker images -q)
```

### 20180529
Install go and golint: <br />
```bash
yum install go -y
go get -u golang.org/x/lint/golint
```

### Data flow
Define the logs that can be sent to Kafka from bro: <br />
https://github.com/jjyy1946/helios/blob/master/helios/bro/kafka.bro <br />

Define the topics that have been created in kafka: <br />
https://github.com/jjyy1946/helios/blob/master/helios/kafka/env <br />

Define the topics in kafka that been parsed by logstash: <br />
https://github.com/jjyy1946/helios/blob/master/helios/logstash/logstash.conf <br />
