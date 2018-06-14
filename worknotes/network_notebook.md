## Network Knowledge

### Promiscuous mode

```bash
yum install net-tools
ifconfig ens192
ens192: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 192.168.7.16  netmask 255.255.255.0  broadcast 192.168.7.255
        inet6 fe80::8d9b:9c6:3035:8bf  prefixlen 64  scopeid 0x20<link>
        inet6 2602:306:3005:584f:28e4:e4e3:31c1:bf5  prefixlen 64  scopeid 0x0<global>
        ether 00:0c:29:6e:35:ff  txqueuelen 1000  (Ethernet)
        RX packets 246957  bytes 38230937 (36.4 MiB)
        RX errors 0  dropped 152  overruns 0  frame 0
        TX packets 227840  bytes 41582287 (39.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ifconfig ens192 promisc
ifconfig ens192
ens192: flags=4419<UP,BROADCAST,RUNNING,PROMISC,MULTICAST>  mtu 1500
        inet 192.168.7.16  netmask 255.255.255.0  broadcast 192.168.7.255
        inet6 fe80::8d9b:9c6:3035:8bf  prefixlen 64  scopeid 0x20<link>
        inet6 2602:306:3005:584f:28e4:e4e3:31c1:bf5  prefixlen 64  scopeid 0x0<global>
        ether 00:0c:29:6e:35:ff  txqueuelen 1000  (Ethernet)
        RX packets 247185  bytes 38259839 (36.4 MiB)
        RX errors 0  dropped 152  overruns 0  frame 0
        TX packets 228077  bytes 41614215 (39.6 MiB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

ifconfig ens192 -promisc
```
