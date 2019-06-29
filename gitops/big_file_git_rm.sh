#!/bin/bash
set -o errexit

pushd $1 > /dev/null

# make sure we're at the root of git repo
if [ ! -d .git ]; then
    echo "Error: must run this script from the root of a git repository"
    exit 1
fi

# remove all paths passed as arguments from the history of the repo
big_files=("helios/app/PII_ML/FormLearning/tessdata/chi_tra.traineddata"
           "helios/utils/GeoLite2-City.mmdb"
           "helios/app/PII_ML/FormLearning/tessdata/chi_sim.traineddata"
           "helios/app/PII_ML/FormLearning/tessdata/eng.traineddata"
           "helios/svcmgr/svcmgr"
           "helios/manager/main"
           "helios/scanner/api"
           "helios/scanner/main"
           "src/libs/libcrypto.a"
           "helios/app/PII_ML/FormLearning/tessdata/ind.traineddata"
           "helios/scanner/main"
           "helios/app/PII_ML/FormLearning/tessdata/osd.traineddata"
           "helios/app/PII_ML/FormLearning/tessdata/enm.traineddata"
           "helios/eng-tools/bin/jsonnet_centos"
           "helios/ui/proj/static/js/bundle.js"
           "helios/scanner/scanner"
           "helios/app/PII_ML/FormLearning/tessdata/HanS.traineddata"
           "helios/scanner/scanner"
           "helios/app/PII_ML/FormLearning/tessdata/HanT_vert.traineddata"
           "helios/app/PII_ML/FormLearning/tessdata/HanT.traineddata"
           "helios/app/PII_ML/FormLearning/tessdata/HanS_vert.traineddata"
           "helios/ui/proj/static/js/bundle.js.map"
           "helios/app/PII_ML/FormLearning/pdf/form44.pdf"
           "helios/app/test/vagrant.img"
           "helios/app/PII_ML/FormLearning/tessdata/eng.traineddata"
           "helios/app/PII_ML/FormLearning/pdf/form13.pdf"
           "helios/app/PII_ML/FormLearning/pdf/form14.pdf"
           "helios/app/PII_ML/FormLearning/pdf/form38.pdf"
           "helios/app/PII_ML/FormCheck/form1.pdf"
           "helios/app/PII_ML/PII_IE/form9.pdf")

function rm_big_files_from_git_tree {
    arr=("$@")
    for i in "${arr[@]}"
    do
        echo "Processing file: $i ..."
        git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch $i" -- --all
        rm -rf .git/refs/original/ && rm -rf .git/logs/ && git gc --aggressive --prune=now
    done
}

rm_big_files_from_git_tree "${big_files[@]}"

popd > /dev/null
