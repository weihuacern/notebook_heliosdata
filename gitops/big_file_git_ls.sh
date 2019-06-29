#!/bin/bash
#set -x 
#Input: $1, git root dir, $2, number of big files to listed, file size descending order

echo "Time: `date`"
echo "Repo: `git config --get remote.origin.url`"

pushd $1 > /dev/null

# set the internal field separator to line break, so that we can iterate easily over the verify-pack output
IFS=$'\n';

# list all objects including their size, sort by size, take top $1
objects=`git verify-pack -v .git/objects/pack/pack-*.idx | grep -v chain | sort -k3nr | head -$2`

echo "All sizes are in kB's. The pack column is the size of the object, compressed, inside the pack file."

output="size,pack,SHA,location"
allObjects=`git rev-list --all --objects`
for y in $objects
do
    # extract the size in bytes
    size=$((`echo $y | cut -f 5 -d ' '`/1024))
    # extract the compressed size in bytes
    compressedSize=$((`echo $y | cut -f 6 -d ' '`/1024))
    # extract the SHA
    sha=`echo $y | cut -f 1 -d ' '`
    # find the objects location in the repository tree
    other=`echo "${allObjects}" | grep $sha`
    #lineBreak=`echo -e "\n"`
    output="${output}\n${size},${compressedSize},${other}"
done

echo -e $output | column -t -s ', '

popd > /dev/null