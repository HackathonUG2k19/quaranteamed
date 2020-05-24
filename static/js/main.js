$('.like').click(function(){
    console.log($(this).attr(("value")));

    var id = $(this).attr("value");
    var p =  $(this)
    $.ajax(
        {
            type:"GET",
            url:"/articles/like",
            async:true,

            data:{post_id:id},
            success: function(data){
                p.toggleClass("like-btn");
                console.log(data);
                $(`#like${id}`).html(data);
            }
        }
    )

});
$('.star').click(function(){
    $(this).toggleClass("like-btn");

});
$(document).ready(function(){
    $('.like').each(function(){
        var id = $(this).attr("value");
    var p =  $(this)
    $.ajax(
        {
            type:"GET",
            url:"/articles/liked",
            async:true,

            data:{post_id:id},
            success: function(data){
                if(data==1)  p.toggleClass("like-btn");
            }
        }
    )
        
    })

});