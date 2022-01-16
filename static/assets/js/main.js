// $(document).ready(function () {
        
//     $('#postform').submit(function (e) { 
//         e.preventDefault();
//             var url = $(this).attr("action"); 
//             // var url = "{% url 'first:postsend' %}"
//             var formdata = $(this).serialize(); 
//             $.ajax({
//                 type: "POST",
//                 url: url,
//                 data: formdata,
//                 success: function (res) {
//                     console.log(res)
//                     $("#ajaxdiv").html("<h2><center>This is the Ajax Div</center></h2>")
//                 },
//                 error: function (res) {
//                     console.log(res)
//                     $("#ajaxdiv").html("<h2><center>An error occured </center></h2>")
//                 },
                
//             });

//     });
// });

$(document).ready(function () {
    setInterval(() => {
        $.ajax({
            type: 'GET',
            url: "{% url 'getprofiles' %}",
            // data: "data",
            // dataType: "dataType",
            success: (res) => {
                console.log(res)
            },error: (res) => {
                $('#msg').html(res);
            }
        });        
    }, 10);
});






