function get_button(button_num) {
    get_data = {
        "num": button_num
    }
    $.get('/get_button/', get_data, function (data, status) { })
}

function get_switch(switch_num, switch_state) {
    get_data = {
        "num": switch_num,
        "state": switch_state
    }
    $.get('/get_switch/', get_data, function (data, status) { })
}


var show_data = document.getElementById("text2");
var user_data = show_data.getElementsByTagName("p");

function update_show_data(data) {
    for (i = 0; i < data.length; i++) {
        user_data[i].innerHTML = data[i];
    }
}

// setInterval(update_show_data, 100);

function runAnimation() {
    var gamepads = navigator.getGamepads();
    var pad = gamepads[0];
    // update_show_data(pad.axes);
    get_data = {
        "l_x": pad.axes[0],
        "l_y": pad.axes[1],
        "r_x": pad.axes[2],
        "r_y": pad.axes[3],
        "button_0": pad.buttons[0].value,
        "button_1": pad.buttons[1].value,
        "button_2": pad.buttons[2].value,
        "button_3": pad.buttons[3].value,
        "button_4": pad.buttons[4].value,
        "button_5": pad.buttons[5].value,
        "button_6": pad.buttons[6].value,
        "button_7": pad.buttons[7].value,
        "button_8": pad.buttons[8].value,
        "button_9": pad.buttons[9].value,
        "button_10": pad.buttons[10].value,
        "button_11": pad.buttons[11].value,
        "button_12": pad.buttons[12].value,
        "button_13": pad.buttons[13].value,
        "button_14": pad.buttons[14].value,
        "button_15": pad.buttons[15].value,
        "button_16": pad.buttons[16].value,
        // "button_17": pad.buttons[17].value,
    }
    $.get('/get_gamepad/', get_data, function (data, status) { })
    console.log("l_x:%f\nl_y:%f", pad.axes[0], pad.axes[1])
}

//当前执行时间
var nowTime = 0;
//上次执行时间
var lastTime = Date.now();
//控制信号发送间隔100/1000 = 10Hz
var diffTime = 100;
//获取手柄控制开关
var gamepad_switch = document.getElementsByName("switch2");

function animloop() {
    //记录当前时间
    nowTime = Date.now()
    // 当前时间-上次执行时间如果大于diffTime，那么执行动画，并更新上次执行时间
    if (nowTime - lastTime > diffTime) {
        lastTime = nowTime
        if (gamepad_switch[0].checked == true) {
            runAnimation();
        }
    }
    window.requestAnimationFrame(animloop);
}

//监听手柄连接
window.addEventListener("gamepadconnected", function (e) {
    console.log("控制器已连接于 %d 位: %s. %d 个按钮, %d 个坐标方向。",
        e.gamepad.index, e.gamepad.id,
        e.gamepad.buttons.length, e.gamepad.axes.length);
    //在浏览器窗口动画中扫描手柄的各种动态变化
    window.requestAnimationFrame(animloop);
});