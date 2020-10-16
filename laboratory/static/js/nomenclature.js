$(document).ready(function (){
  $.getJSON('/get_nomenclature_data', {}, function (json){
    console.log(json.result.name)
    $('<tr><td colspan=8></td></tr>')
  });
});
