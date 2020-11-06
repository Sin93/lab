// $(document).ready(function(){
//   $('button').click(function (action) {
//     var file = $('input');
//     var upload_file = new FormData();
//     upload_file.append('file', file[0].files)
//     var token = $("input[name~='csrfmiddlewaretoken']").attr('value')
//     console.log(typeof upload_file)
//     $.ajax({
//       type: "POST",
//       url: '/upload_file/49',
//       cache: false,
// 			contentType: false,
// 			processData: false,
//       data: upload_file,
//       dataType: 'json',
//       cookie: `csrftoken=${token}`
//     });
//   });
// });
