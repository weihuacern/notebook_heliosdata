## Zookeeper

[Apache Zookeeper](https://zookeeper.apache.org) <br />
[Quick Guide](https://www.tutorialspoint.com/zookeeper/zookeeper_quick_guide.htm) <br />
[Getting Started Guide](https://zookeeper.apache.org/doc/r3.3.3/zookeeperStarted.html) <br />
[More Insights](http://www.corejavaguru.com/bigdata/zookeeper/interview-questions-part-1.php) <br />

```
brew install zookeeper
zkServer start
zkCli
zkServer stop
```
zookeeper running on: localhost:2181(127.0.0.1:2181). Config info: /usr/local/etc/zookeeper/zoo.cfg <br />

## Kafka

[Apache Kafka](https://kafka.apache.org) <br />
[Quick Start](https://kafka.apache.org/quickstart) <br />

```
brew install kafka
zkServer start
kafka-server-start /usr/local/etc/kafka/server.properties
```
kafka running on: localhost:9092(127.0.0.1:9092). <br />

Check port usuage: <br />
```
netstat -vanp tcp
```
