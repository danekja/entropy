#!/bin/bash

echo '' > paths.txt
for f in $(find -name '*.jar')
  do
    echo ${f%/*} >> paths.txt
  done
echo 'done'
