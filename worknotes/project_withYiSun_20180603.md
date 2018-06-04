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
