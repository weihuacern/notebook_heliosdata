# Worknotes@Heliosdata
Working note and self-practice at heliosdata. <br />

```bash
sh revenue_setup.sh --device=ens192 --ipaddr=192.168.8.0 --netmask=255.255.255.0
sh client_setup.sh --device=ens192 --ipaddr=192.168.8.0 --netmask=255.255.255.0
```

```bash
http-server -c-1
```
## Git Operation
```bash
cd gitops/
sh big_file_git_ls.sh /root/notebook_heliosdata 10
sh big_file_git_rm.sh /root/gin_dev/helios/
```

## Design Document

### PlantUML
```bash
cd ./design_doc/svcmgr/
java -jar plantuml.jar svcmgr_source_state.uml
```
