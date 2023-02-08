/*
 * @author: yuyuyuj1e 807152541@qq.com
 * @github: https://github.com/yuyuyuj1e
 * @csdn: https://blog.csdn.net/yuyuyuj1e
 * @date: 2023-02-07 16:21:12
 * @last_edit_time: 2023-02-08 11:32:15
 * @file_path: /Conference-Deadlines/static/js/timer.js
 * @description: 实现多倒计时
 */

/**
 * @description: 倒计时函数
 * @param {*} remain_time: 从当前时间到截至时间所省时间，单位秒
 * @param {*} index: 目标索引，通过 $(this) 传递
 */
function timer(remain_time, index) {
    function fn() {
        if (remain_time > 0) {
            // 计算天数
            let day = Math.floor(remain_time / 86400)
            day = day < 10 ? "0" + day : day;
            // 计算小时数
            let hour = Math.floor((remain_time % 86400) / 3600)
            hour = hour < 10 ? "0" + hour : hour;
            // 计算分钟数
            let minutes = Math.floor((remain_time % 3600) / 60)
            minutes = minutes < 10 ? "0" + minutes : minutes;
            // 计算秒数
            let seconds = Math.floor(remain_time % 60)
            seconds = seconds < 10 ? "0" + seconds : seconds;
            let msg = day + " day " + hour + " h " + minutes + " m " + seconds + " s ";

            $(index).find('.timer').html(msg)
            --remain_time;
        }
        else {
            clearInterval(timer);
            $(index).find('.timer').html("time out!");
            $(index).addClass('timeout');
        }
    }

    fn();  // 避免开始的一秒延迟
    setInterval(function () {
        fn();
    }, 1000);
}

$(document).ready(function () {
    $(".conference-item").each(function () {
        // 获取结束时间
        var time = $(this).find('.deadline span').text();
        // 获取当前时间的时间戳（单位毫秒）
        let now_time = new Date();
        // 获取截止时间的时间戳（单位毫秒）
        let remain_time = (new Date(time) - now_time) / 1000;
        // 开启定时器
        timer(remain_time, $(this));
    });
});