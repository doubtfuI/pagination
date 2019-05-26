$(function () {
    $('#page_jump_tag').click(function () {
        var page_num = $(this).prev().val();
        var default_url = $(this).attr('href');
        var rep = /(\S+)-1.html$/;
        var a = rep.exec(default_url);
        var url = a[1] + '-' + page_num + '.html';
        location.replace(url);
        return false
    });
});