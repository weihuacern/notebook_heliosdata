## Elasticsearch, Logstash and Kibana

[Udemy course](https://www.udemy.com/elasticsearch-6-and-elastic-stack-in-depth-and-hands-on/learn/v4/overview) <br />

#### Installation

```bash
sudo apt-get install openssh-server
sudo apt-get install default-jdk
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
sudo apt-get install apt-transport-https
echo "deb https://artifacts.elastic.co/packages/6.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-6.x.list
sudo apt-get update && sudo apt-get install elasticsearch
```

#### Test

Shakespeare. <br />

```bash
wget http://media.sundog-soft.com/es6/shakes-mapping.json
curl -H 'Content-Type: application/json' -XPUT 127.0.0.1:9200/shakespeare --data-binary @shakes-mapping.json
wget http://media.sundog-soft.com/es6/shakespeare_6.0.json
curl -H 'Content-Type: application/json' -X POST '127.0.0.1:9200/shakespeare/doc/_bulk?pretty' --data-binary @shakespeare_6.0.json
curl -H 'Content-Type: application/json' -XGET '127.0.0.1:9200/shakespeare/_search?pretty' -d '{"query": {"match_phrase": {"text_entry": "to be or not to be"}}}'
```

Movielens. <br />

```bash
curl -H "Content-Type: application/json" -XPUT 127.0.0.1:9200/movies -d '{"mappings": {"movie": {"properties": {"year": {"type": "date"}}}}}'
wget http://media.sundog-soft.com/es/movies.json
curl -H "Content-Type: application/json" -XPUT 127.0.0.1:9200/_bulk?pretty --data-binary @movies.json
curl -H "Content-Type: application/json" -XGET 127.0.0.1:9200/movies/movie/_search?pretty
curl -H "Content-Type: application/json" -XPOST 127.0.0.1:9200/movies/movie/109487/_update -d '{"doc": {"title": "interstellar modify"}}'
```
