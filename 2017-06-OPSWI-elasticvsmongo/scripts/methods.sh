#!/bin/bash

while read path
do
  LINK=$path
  VERSION="$(echo ${LINK##*/})"
  echo $path
  cd $LINK/
  echo '' > methods.txt

  for f in *.jar
  do
    jar tf $f | grep '.class$' > $f.txt
    unzip -q $f -d temp

    while read LINE
    do
      echo "PATH: $LINE" >> methods.txt
      echo "VERSION: $VERSION" >> methods.txt
      javap -public "temp/$LINE" >> methods.txt
    done < $f.txt
  done

  #clean up
  rm -rf temp
  cd ~/.m2/repository

done < paths.txt
