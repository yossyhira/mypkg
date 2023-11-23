#!/bin/bash

dir=~  #～はホームディレクトリのこと

[ "$1" != "" ] && dir="$1" #何かコマンドの後に引数があったら～を＄１に書き換え　./コマンド a b c だったら$1=a

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log #10秒間コマンドを起動して中身を/tmp/mypkg.logに代入

cat /tmp/mypkg.log | grep 'Listen:10'
