
// 引入 header footer


$.ajax({
    url:'../header.htm',
    success:function(data){
        $("body").prepend(data)
    }
})

$.ajax({
    url:'../footer.htm',
    success:function(data){
        $("body").append(data)
    }
})