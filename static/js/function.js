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

$(document).ready(function() {
    //图片鼠标悬停事件
    $(function() {
        $('#wechat').mouseover(function() {
            $('#wechat-img').show();
        })
        $('#wechat').mouseleave(function() {
            $('#wechat-img').hide();
        })
    })
});