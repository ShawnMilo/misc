#!/usr/bin/env bash

# run a program every time it's changed

flag=$(mktemp)

script="$1"

if [ ! -f "$script" ]; then
    echo "no script name passed"
    exit
fi

D=$(dirname $script)
F=$(basename $script)
script="$D/$F"

while true; do 
    if [ $script -nt $flag ]; then
        echo "going to run"
        time $script
        touch $flag
    fi
    sleep 1
done

