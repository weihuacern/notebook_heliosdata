## Consul and Scanner

- Test: install consul, put key/value pair on it, and test to get value from key. <br />

```
helios/consul/0.X/Dockerfile:ENV CONSUL_VERSION=1.0.2
wget https://releases.hashicorp.com/consul/1.0.2/consul_1.0.2_linux_amd64.zip
```

- Make source.json and put it into consul KV store. <br />
- Run scanner and make it know the source. <br />
