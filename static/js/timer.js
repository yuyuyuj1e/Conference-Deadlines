function timer(end_time, index) {
    // 获取当前时间的时间戳（单位毫秒）
    let now_time = new Date();
    // 获取截止时间的时间戳（单位毫秒）
    let remain_time = (new Date(end_time) - now_time) / 1000

    setInterval(function() {
        if(remain_time > 0) {
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
    }, 1000);
}


$(document).ready(function() {
    $(".conference-item").each(function () {
        var time = $(this).find('.deadline span').text();
        timer(time, $(this));
    });
});