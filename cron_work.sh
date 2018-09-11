#!/bin/sh
export LANG="zh_CN.UTF-8"

exec_dir=/root/news/
port=9004

cd $exec_dir

if [ $# -eq 1 ]
then
    mode=$1
elif [ $# -eq 0 ]
then
    mode="start"
else
    echo "wrong parameter count"
    exit 1
fi

ps axjf|grep "python main.py 9004"|grep -v "grep"
if [ $? -eq 0 ]
then
    proc_exist=1
    previous_pid=`ps axjf |grep "python main.py 9004"|grep -v "grep"|awk {'print $2'}`
else
    proc_exist=0
fi

if [ "$mode" = "start" ]
then
    if [ $proc_exist -eq 0 ]
    then
        python main.py 9004 &
    fi
elif [ "$mode" = "restart" ]
then
    if [ $proc_exist -eq 1 ]
    then 
        kill $previous_pid
    fi    
    python main.py 9004 &
elif [ "$mode" = "stop" ]
then
    if [ $proc_exist -eq 1 ]
    then
        kill $previous_pid
    fi
fi

