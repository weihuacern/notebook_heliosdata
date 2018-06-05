## Elastic visualization

Get consul scanned and then put them into elasticsearch visualization.

Test Yi's code:
```
pip install sqlparse
pip install elasticsearch
export PYMSSQL_BUILD_WITH_BUNDLED_FREETDS=1
pip install pymssql
sudo PYTHONPATH=/root/helios/helios/app/ python3 /root/helios/helios/app/frontend/elastic_query.py
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
