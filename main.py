# -*- coding: utf-8 -*-
from flask import Flask, render_template, Response
from flask.sessions import NullSession
from flask import request
import time
import serial
import camera
import motor

app = Flask(__name__)
# 配置摄像头
video_task = camera.Video_task(0, 480, 640)
# 配置串口
ser = serial.Serial("/dev/ttyS5", 9600)

def UARTServo(servonum, angle):
    servonum = 64 + servonum
    date1 = int(angle/100 + 48)
    date2 = int((angle % 100)/10 + 48)
    date3 = int(angle % 10 + 48)
    cmd = bytearray([36, servonum, date1, date2, date3, 35])
    ser.write(cmd)
    time.sleep(0.05)

# 舵机位置初始化
UARTServo(9, 90)
UARTServo(10, 30)
UARTServo(11, 30)
UARTServo(13, 90)
UARTServo(1, 30)

Servo_9 = 90
gamepad_flag = 0

@app.route('/')  # 主页
def index():
    # jinja2模板，具体格式保存在index.html文件中
    return render_template('index.html')


@app.route('/video_feed/')  # 这个地址返回视频流响应
def video_feed():
    video_task.num += 1
    return Response(video_task.video_feed(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/get_button/', methods=['GET'])
def get_button():
    if request.method == 'GET':
        button_num = request.args.get('num')

        global gamepad_flag
        if gamepad_flag == 0:
            if button_num == "1":
                motor.move_forword()
                time.sleep(1)
                motor.stop()
            elif button_num == "2":
                motor.turn_left()
                time.sleep(1)
                motor.stop()
            elif button_num == "3":
                motor.turn_right()
                time.sleep(1)
                motor.stop()
            elif button_num == "4":
                motor.move_back()
                time.sleep(1)
                motor.stop()

            if button_num == "5":
                UARTServo(13, 100)#合爪子
            elif button_num == "6":
                UARTServo(13, 60)#开爪子
              
            if button_num == "7":
                # 翻筐
                UARTServo(1, 70)
            elif button_num == "8":
                # 收筐
                UARTServo(1, 30)

    return "ok"


@app.route('/get_switch/', methods=['GET'])
def get_switch():
    if request.method == 'GET':
        switch_num = request.args.get('num')
        switch_state = request.args.get('state')
        global gamepad_flag
        if switch_num == "1":
            camera_control(switch_state)

        if switch_num == "2":
            if switch_state == "true":
                gamepad_flag = 1
            else:
                gamepad_flag = 0

        print(switch_num + switch_state)
    return "ok"


@app.route('/get_gamepad/', methods=['GET'])
def get_gamepad():
    if request.method == 'GET':
        button_0 = int(request.args.get('button_0'))
        button_1 = int(request.args.get('button_1'))
        button_2 = int(request.args.get('button_2'))
        button_3 = int(request.args.get('button_3'))
        button_4 = int(request.args.get('button_4'))
        button_5 = int(request.args.get('button_5'))
        button_8 = int(request.args.get('button_8'))
        button_9 = int(request.args.get('button_9'))
        button_12 = int(request.args.get('button_12'))
        button_13 = int(request.args.get('button_13'))
        button_14 = int(request.args.get('button_14'))
        button_15 = int(request.args.get('button_15'))

        if button_0 == 1:
            UARTServo(13, 100)#合爪子
        elif button_1 == 1:
            UARTServo(13, 60)#开爪子


        # 机械臂翻转
        if button_2:
            UARTServo(10, 0)
            UARTServo(11, 30)
        elif button_3:
            UARTServo(10, 150)
            UARTServo(11, 90)

        # 机械臂旋转
        global Servo_9
        if button_4:
            Servo_9+=2
        elif button_5:
            Servo_9-=2

        if button_4 or button_5:
            if Servo_9>104:
                Servo_9 = 104
            elif Servo_9<76:
                Servo_9 = 76
            UARTServo(9, int(Servo_9))

        # 翻筐
        if button_8:
            UARTServo(1, 70)
        elif button_9:
            UARTServo(1, 30)

        # 底盘运动
        if button_12:
            motor.move_forword()
        elif button_13:
            motor.move_back()
        elif button_14:
            motor.turn_left()
        elif button_15:
            motor.turn_right()
        else:
            motor.stop()

    return "ok"


def camera_control(state):
    if state == "true":
        video_task.open_cam = True
    if state == "false":
        video_task.open_cam = False


if __name__ == '__main__':
    video_task.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
    # app.run(debug=False)
    video_task.join()
