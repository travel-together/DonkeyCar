# Travel-together donkeycar 介绍
## 1、Background 项目背景
近年来，有一些关于仿真到现实的研究，即先利用强化学习在虚拟模拟器中对汽车进行训练，然后将训练后的智能体转移到现实世界中。
本次实训项目主要基于开源无人驾驶控制项目Donkey car。
Donkey car是用Python编写的极简和模块化的自动驾驶库。主要面向无人驾驶爱好者和学生开发，重点是搭建快速的实践平台和便捷的社区贡献。
Donkey car可运行在raspberry pi（3B+以上）、JetsonNano等小体积的嵌入式控制平台上,也可以运行在基于Unity引擎的虚拟仿真环境中。
Donkey car的控制算法基于机器学习引擎Tensorflow，集摄像头图像数据采集、人工神经网络训练、人工神经网络自动驾驶驱动等功能于一体。
项目包含了一个复杂无人驾驶控制工程的内容，涉及到脚本设计、传感器驱动和数据传输、控制信息传递机制、控制行为决策等知识和技能。

开放式的平台，能让学生根据自身能力水平，实施不同的控制算法。是学习深度学习和自动驾驶非常出色的平台。

## 仓库目录结构

master分支中存储了本次项目的内容，包括：
笔记：有TensorFlow学习笔记，git学习笔记，和各天所学知识的笔记

文件：包含了此次实习的计划安排

模型：在mycar/models文件夹中，包括模拟器中的训练成果sim.h5，7.4V电池驱动带有避障功能的7.4v+避障.h5,12V电池驱动的12v.h5

配置文件：在mycar文件夹中，包括小车的所有配置文件

3D打印及印制电路板相关文件

## 2、Install 安装

虚拟小车：

用myconfig1.py覆盖小车文件夹中的myconfig.py

用`python manage.py drive`指令启动donkeysimulator进行驾驶和数据收集

实体小车:

用myconfig2.py覆盖小车文件夹中的myconfig.py

用`python manage.py drive`启动小车，可在网页端操控小车

或用`python manage.py drive --model <yourmodels path>`启动自动驾驶

模型可用文件中的.h5文件替换



## 3、项目过程

### 环境搭建

* miniconda 安装https://conda.io/miniconda.html

* 在miniconda prompt 中新建项目文件

  `mkdir projects`

  `cd projects`

* 从github上获取最新版本的驴车

  `git clone https://github.com/autorope/donkeycar` 

  `cd donkeycar` 

  `git checkout master`

* 创建python anaconda 环境

  `conda env create -f install\envs\windows.yml` 

  `conda activate donkey` 

  `pip install --user tensorflow-gpu==2.2.0` 

  `pip install -e .[pc]`

* 下载安装donkey simulatorhttps://github.com/tawnkramer/gym-donkeycar/releases

* 设置安装驴模拟器，下载gym-donkey

  `cd projects` 

  `git clone https://github.com/tawnkramer/gym-donkeycar` 

  `cd gym-donkeycar` 

  `conda activate donkey` 

  `pip install -e .[gym-donkeycar]`

* 创建新的小车文件夹

  `donkey createcar --path ~/mysim` 

  `cd mysim`

* 修改项目中的myconfig.py代码

  `DONKEY_GYM = True` 

  `DONKEY_SIM_PATH = "/home/<user-name>/projects/DonkeySimLinux/donkey_sim.x86_64"`

   `DONKEY_GYM_ENV_NAME = "donkey-generated-track-v0"`

### 模拟器中小车训练与测试

* 训练小车，生成训练模型

  `python manage.py drive`

  启动模拟器并自动连接，导航到http://localhost:8887/drive查看控制页面，用户模式下拖动鼠标即可控制小车。

  将训练时生成的图像合成模型文件

  `python manage.py train --model models/mypilot.h5`

* 测试训练模型

  `python manage.py drive --model models/mypilot.h5`

  然后导航到 Web 控制页面。设置为 Local Pilot(d)汽车应该开始行驶了。

### 实体小车组装

* 用激光切割制作小车底板、顶板和相机支架
* 按照安装视频完成小车组装

### 配置树莓派环境

* 为树莓派安装操作系统

  在https://downloads.raspberrypi.org/raspbian_lite_latest中下载树莓派的操作系统并用专用的安装工具安装到SD卡中。

* 创建一个设置wifi的文件，其中包含wifi的名称及密码。

* 创建ssh文件，通过ssh及IP地址连接到树莓派。

* 在树莓派中安装软件包及依赖库

  `sudo apt-get install build-essential python3 python3-dev python3-pip python3-virtualenv python3-numpy python3-picamera python3-pandas python3-rpi.gpio i2c-tools avahi-utils joystick libopenjp2-7-dev libtiff5-dev gfortran libatlas-base-dev libopenblas-dev libhdf5-serial-dev libgeos-dev git ntp`

* 安装OpenCV 的依赖项

  `sudo apt-get install libilmbase-dev libopenexr-dev libgstreamer1.0-dev libjasper-dev libwebp-dev libatlas-base-dev libavcodec-dev libavformat-dev libswscale-dev libqtgui4 libqt4-test`

* 在树莓派中创建虚拟环境

  `python3 -m virtualenv -p python3 env --system-site-packages`

  `echo "source env/bin/activate" >> ~/.bashrc`

  `source ~/.bashrc`

* 为树莓派安装DonkeyCar

```linux
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout master
pip install -e .[pi]
pip install numpy --upgrade

curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=1DCfoSwlsdX9X4E3pLClE1z0fvw8tFESP" > /dev/null
CODE="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${CODE}&id=1DCfoSwlsdX9X4E3pLClE1z0fvw8tFESP" -o tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
pip install tensorflow-2.2.0-cp37-cp37m-linux_armv7l.whl
```

* 安装OpenCV

  `sudo apt install python3-opencv`

  `pip install opencv-python`



### 校准油门和舵机

安装好小车并连接好树莓派后，在驾驶小车前要对油门和转向进行校准：

油门校准：

`donkey calibrate --channel <your_steering_channel> --bus=1`

舵机校准：

`donkey calibrate --channel <your_throttle_channel> --bus=1` 



### 开始驾驶

连接好摄像头，并设置好myconfig文件即可开始实地驾驶并收集数据。

`python manage.py drive`

可以登录IP：8887在网页端操作小车并记录数据，在user模式下可以选择鼠标、键盘、手柄或手机对小车进行控制。

将训练时生成的图像合成模型文件

`python manage.py train --model models/mypilot1.h5`

测试训练模型

`python manage.py drive --model models/mypilot1.h5`

然后导航到 Web 控制页面。设置为 Local Pilot(d)模式汽车可以开始行驶了。



## 小组成员及分工

小组成员群策群力，勠力同心，全程互相配合，分工协作，共同解决遇到的问题，所有过程小组成员均有参与，以下仅列出各成员的主要工作内容：

蒋卓彤：环境搭建，小车组装，树莓派环境配置，实地数据收集及训练

冯灏钰：资源查找与下载，模拟器中数据收集及训练，小车组装，文档撰写

陈鹏豪：过程记录，环境搭建，小车组装，实地数据收集及训练

崔永康：环境搭建及小车配置，小车组装，树莓派环境配置，文档撰写

曲国藩：小车组装，模拟器中数据收集及训练

