$(document).ready(function(){
  $('button').click(function (action) {
    var file = $('input');
    var upload_file = new FormData();
    upload_file.append('file', file[0].files[0])
    // $.post()
  });
});
