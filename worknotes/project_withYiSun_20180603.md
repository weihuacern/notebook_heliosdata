## Elastic visualization

Get consul scanned and then put them into elasticsearch visualization.

Test Yi's code:
```
pip install sqlparse
pip install elasticsearch
export PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1
pip install pymssql
sudo PYTHONPATH=/root/helios/helios/app/ python3 /root/helios/helios/app/frontend/elastic_query.py
sudo PYTHONPATH=/root/test/helios/helios/app/ python3 /root/test/helios/helios/app/frontend/elastic_query.py
```

/opt/helios/config/els.conf
```
els_host=192.168.7.8
els_port=9200
els_user=elastic
els_password=helios12$
consul_host=192.168.7.5
```

Build a finite state machine for ETL, then make output to the Kibana. <br />

Mock the environment, fake sql queries... <br />
- my local mac, aok
- 192.168.7.114 (hua test vm, CentOS), aok
- 192.168.7.14, aok
- 192.168.7.15, aok
- 192.168.7.16, aok
- 192.168.7.17, aok

```
yum -y install vim*
yum install gcc
yum install freetds-devel
pip3.6 install pymssql
pip3.6 install pymysql
pip3.6 install names
```

Setup Web sever: <br />
```
https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-16-04
/var/www/html
http://192.168.7.155/PIIFormTest/
```
