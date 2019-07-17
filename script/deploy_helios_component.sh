# Description: Copy pub key to Helios machine to avoid input password
function copy_pub_key {
  scp ~/.ssh/id_rsa.pub root@$1:/root/.ssh/
  ssh root@$1 << EOF
    pushd /root/.ssh/
    rm -rf authorized_keys
    mv id_rsa.pub authorized_keys
    rm -rf id_rsa.pub
EOF
}

# Description: Release the Helios system from network hardening and enable all debug log
function make_helios_free_again {
  ssh root@$1 << EOF
    pushd /opt/helios/bin
    python3.6 debug_util.pyz -A -l debug
    popd
EOF
}

# Description: Hacky way to deploy api_server
function deploy_apiserver {
  pushd $1
    make
    rsync -r ./target/ root@$2:/opt/helios/bin/
    rsync -r ./helios/app/protoutils/ root@$2:/opt/helios/protoutils/
    ssh root@$2 << EOF
      pushd /opt/helios/docker
      docker-compose -f ./compose.yml restart api_server
      popd
EOF
  popd
}

# Description: Hacky way to deploy spark
function deploy_spark {
  pushd $1
    make
    rsync -r ./ root@$2:/mnt/code/
    rsync -r ./target/ root@$2:/opt/helios/bin/
    rsync -r ./helios/app/protoutils/ root@$2:/opt/helios/protoutils/
    scp -r ./helios/app/spark_data_processor/app.py root@$2:/opt/helios/bin/spark_data_processor.py
    scp -r ./helios/app/spark_kafka_listener/app.py root@$2:/opt/helios/bin/spark_kafka_listener.py
    scp -r ./helios/app/spark_ddn_analysis/app.py root@$2:/opt/helios/bin/spark_ddn_analysis.py
  popd
}

# Description: Hacky way to deploy svcmgr
function deploy_svcmgr {
  pushd $1
    make svcmgr_dev
    scp helios/svcmgr/svcmgr root@$2:/opt/helios/bin/
    ssh root@$2 << EOF
      docker container cp /opt/helios/bin/svcmgr svcmgr:/opt/helios/bin/
      pushd /opt/helios/docker
      docker-compose -f ./compose.yml restart svcmgr
      popd
EOF
  popd
}

# Description: Hacky way to deploy scanner
function deploy_scanner {
  pushd $1
    make scanner_dev
    scp helios/scanner/scanner root@$2:/opt/helios/bin/
    ssh root@$2 << EOF
      docker container cp /opt/helios/bin/scanner appscanner:/opt/helios/local/bin/
      pushd /opt/helios/docker
      docker-compose -f ./compose.yml restart appscanner
      popd
EOF
  popd
}

src=$1
host=$2

copy_pub_key $host
make_helios_free_again $host
#deploy_apiserver $src $host
#deploy_spark $src $host
#deploy_svcmgr $src $host
#deploy_scanner $src $host
