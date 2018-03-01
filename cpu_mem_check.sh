##! /bin/sh

# file list
LIST=$1

#check exist for list file

if [ ! -f "${LIST}" ]
then
        echo "List File ${LIST} Not Found"
        fi

# loop for list file

        for i in `cat $LIST`
        do

        echo "------------------------------------------------"
        echo $i
        rsh -x -l root $i "grep -c processor /proc/cpuinfo"
        rsh -x -l root $i 'cat /proc/cpuinfo | grep "model name"'
        rsh -x -l root $i "free"
        rsh -x -l root $i "df -h"
        done