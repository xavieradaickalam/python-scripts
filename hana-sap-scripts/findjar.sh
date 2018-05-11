#!/bin/sh
echo "Class to be found : $1"
echo "Searching a Directory :  $2"
find "$1" -name "*.jar" -exec sh -c 'jar -tf {}|grep -H --label {} '$2'' \;
