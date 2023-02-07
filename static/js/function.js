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


// $(".page-item").change(function() {
//     let page_now = $(".active").id
//     let page = $(".page-item").val()
//     alert(page_now)
//
//    // $.ajax({
//    //     url: "/page",
//    //     data: {
//    //         "page-now": check1,
//    //         "page": page
//    //     }
//    //  })
// });

