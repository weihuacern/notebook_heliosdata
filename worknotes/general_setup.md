#### SMTP:
```bash
sudo yum install cyrus-sasl
sudo yum install cyrus-imapd
```
- https://www.digitalocean.com/community/tutorials/how-to-install-postfix-on-centos-6
- https://kb.op5.com/display/HOWTOs/Sending+outgoing+email+messages+%28notifications%29+through+an+SMTP+relay+server#sthash.PEJc0xaq.dpbs

#### Samba:
- install: https://www.tecmint.com/install-samba4-on-centos-7-for-file-sharing-on-windows/
- setup with windows: https://blog.csdn.net/u012322925/article/details/51388159

#### NFS:
- https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-centos-6
- https://www.howtoforge.com/nfs-server-and-client-on-centos-7

#### MSSQL:
- https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-red-hat?view=sql-server-linux-2017

#### MYSQL:
- install: https://www.linode.com/docs/databases/mysql/how-to-install-mysql-on-centos-7/
- uninstall: https://blog.csdn.net/hi_1234567/article/details/9176715

```bash
mysql -u root -p
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';
bind-address = 127.0.0.1 
```
#### Neo4j:
- https://neo4j.com/developer/kb/how-to-list-and-install-neo4j-versions-using-yum/
- https://neo4j.com/docs/operations-manual/current/installation/linux/systemd/
- https://github.com/neo4j/neo4j-python-driver

```bash
journalctl -e -u neo4j
```
