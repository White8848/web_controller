# 机器人网页控制端(Robot Web Control Terminal)

## Introduction

本项目基于flask实现web服务器，搭载于树莓派等开发板，为机器人提供网页控制端。

This project is based on flask to implement the web server, which is loaded on the development board such as Raspberry Pi, to provide a web control terminal for the robot.

## Features

- Website vedio streaming (mjpg-streamer)

- Camera remote control

- Motor remote control

- Web key event communication

- Handle data transmission

## Usage

This project in test on OrangePI and based on python3.9

### 1.install dependencies

```bash
pip install -r requirements.txt
```

### 2.set up autostart

Add run.sh to /etc/rc.local

```bash
sudo vim /etc/rc.local
```

