#!/usr/bin/env sh

n=1

while [ $n -le 100 ]
do
	printf "		Mind Awake\n"
	printf "		Body Asleep\n"
	n=$(( $n + 1 ))
done
