var COLUMN_CLASSES = {
  '0': 'code',
  '1': 'name',
  '2': 'blanks',
  '3': 'biomaterials',
  '4': 'containers',
  '5': 'due_date',
  
}
$(document).ready(function (){
  $.getJSON('/get_nomenclature_data', {}, function (json){
    console.log('Document ready')
    for(var group in json) {
      var row = $('<tr></tr>')
      var cols = $('<td colspan=8></td>')
      cols.text(group)
      $(row).append(cols)
      nom_table = $('table')
      $(nom_table).append(row)

      for(subgroup in json[group]) {
        var row = $('<tr></tr>')
        var cols = $('<td colspan=8></td>')
        cols.text(subgroup)
        $(row).append(cols)
        nom_table = $('table')
        $(nom_table).append(row)

        for(service in json[group][subgroup]) {
          nom_table = $('table')
          var row = $('<tr></tr>')

          for(col in json[group][subgroup][service]) {
            if (col <= 6) {
              if (col == '2'){
                var column = $('<td></td>')
                column.text(json[group][subgroup][service][col])
                column.addClass('blanks')
                $(row).append(column)
                $(nom_table).append(row)
              } else {
                var column = $('<td></td>')
                column.text(json[group][subgroup][service][col])
                $(row).append(column)
                $(nom_table).append(row)
              }
            } else {
              var column = $('<td></td>')
              var edit_link = $('<a>Ред.</a>')
              edit_link.attr('href', json[group][subgroup][service][col])
              $(column).append(edit_link)
              $(row).append(column)
              $(nom_table).append(row)
            }
          };
        };
      };
    };
  });
  $('form input').click(function (className) {
    var inputclass = $(this).attr('id')
    var column = $('.blanks')
    column.toggle()
  });
});




          // var column = $('<td></td>')
          // column.text(service)
          // $(row).append(column)
          // $(nom_table).append(row)
          //
          // var column = $('<td></td>')
          // column.text(service.name)
          // $(row).append(column)
          // $(nom_table).append(row)
          //
          // $(row).append('<td></td>').text(service['blank'])
          // $(nom_table).append(row)
          // $(row).append('<td></td>').text(service['biomaterial'])
          // $(nom_table).append(row)
          // $(row).append('<td></td>').text(service['container'])
          // $(nom_table).append(row)
          // $(row).append('<td></td>').text(service['due_date'])
          // $(nom_table).append(row)
          // $(row).append('<td></td>').text(service['result_type'])
          // $(nom_table).append(row)
          // $(row).append('<td></td>').text(service['edit_link'])
