/*
 * @author: yuyuyuj1e 807152541@qq.com
 * @github: https://github.com/yuyuyuj1e
 * @csdn: https://blog.csdn.net/yuyuyuj1e
 * @date: 2023-02-07 16:21:12
 * @last_edit_time: 2023-02-08 14:06:52
 * @file_path: /Conference-Deadlines/static/js/function.js
 * @description: 头部注释配置模板
 */
document.write("<script src='./jquery-3.6.3.min.js'></script>");

$(".btn-check").change(function() {
    let check1 = $("#btncheck1").is(":checked")
    let check2 = $("#btncheck2").is(":checked")
    let check3 = $("#btncheck3").is(":checked")
    let check4 = $("#btncheck4").is(":checked")
    let search = $("#search").val()

   window.location.href = "?check1=" + check1
       + "&check2=" + check2
       + "&check3=" + check3
       + "&check4=" + check4
       + "&search=" + search
});
