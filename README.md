# mypkg
[![test](https://github.com/yossyhira/mypkg/actions/workflows/test.yml/badge.svg)](https://github.com/yossyhira/mypkg/actions/workflows/test.yml)

ロボットシステム学2023のROS2講義用リポジトリ

## このリポジトリで使用可能なノード
* talker

* listener

## インストール方法
下記のコードをホームディレクトリでクローンしてください
```
git clone https://github.com/yossyhira/mypkg.git
```
cdコマンドを使い、mypkgディレクトリに移動してください
```
cd mypkg
```
下記の方法でtalkerとlistenerを実行してください

## ノードの機能と実行方法
### talker
* 機能

 実行すると０から0.5秒おきに１ずつ足された結果をメッセージとして送信する

* 実行方法


```bash
$ ros2 run mypkg talker #<-実行結果は何も表示されない
```

### listener
* 機能

talkerからメッセージを受信する

* 実行方法

talkerとは別の端末で下記のコードを実行

```bash
$ ros2 run mypkg listener
[INFO] [1700712742.234721050] [listener]: Listen:130
[INFO] [1700712742.724570259] [listener]: Listen:131
[INFO] [1700712743.224212712] [listener]: Listen:132
[INFO] [1700712743.724288274] [listener]: Listen:133
[INFO] [1700712744.223597699] [listener]: Listen:134
[INFO] [1700712744.723681795] [listener]: Listen:135
[INFO] [1700712745.223837187] [listener]: Listen:136
[INFO] [1700712745.723885839] [listener]: Listen:137
```

## launch

* 機能

talkerとlistenerを同時に実行する

* 実行方法

```bash
$ ros2 launch mypkg talk_listen.launch.py
[INFO] [launch]: All log files can be found below /home/hirata/.ros/log/2023-11-23-14-01-33-241579-yoshi-5735
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [5736]
[INFO] [listener-2]: process started with pid [5738]
[listener-2] [INFO] [1700715694.139548983] [listener]: Listen:0
[listener-2] [INFO] [1700715694.625656000] [listener]: Listen:1
[listener-2] [INFO] [1700715695.125553813] [listener]: Listen:2
[listener-2] [INFO] [1700715695.625907021] [listener]: Listen:3
[listener-2] [INFO] [1700715696.125882861] [listener]: Listen:4
[listener-2] [INFO] [1700715696.625900558] [listener]: Listen:5
[listener-2] [INFO] [1700715697.125842379] [listener]: Listen:6
```


## 動作環境
### 必要なソフトウェア　

* python
  * テスト済み：3.7 ~ 3.10

### テスト環境
* ubuntu 22.04.2 LTS

## ライセンス
* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
  


  * このパッケージのtest.ymlとlistener.py以外のコードは，[こちら](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです.

  * © 2023 Yoshitaka Hirata
