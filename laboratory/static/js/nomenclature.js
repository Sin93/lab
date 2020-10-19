$(document).ready(function (){
  $.getJSON('/get_nomenclature_data', {}, function (json){
    for(var group in json.result) {
      var row = $('<tr></tr>')
      var cols = $('<td colspan=8></td>')
      cols.text(group)
      $(row).append(cols)
      nom_table = $('table')
      $(nom_table).append(row)
      for(subgroup in json.result[group]) {
        var row = $('<tr></tr>')
        var cols = $('<td colspan=8></td>')
        cols.text(subgroup)
        $(row).append(cols)
        nom_table = $('table')
        $(nom_table).append(row)

        for(service in json.result[group][subgroup]) {
          nom_table = $('table')
          var row = $('<tr></tr>')
          for(col in service) {
            var column = $('<td></td>')
            column.text(col)
            $(row).append(column)
            $(nom_table).append(row)
          }

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

        }
      };
    };
  });
});
