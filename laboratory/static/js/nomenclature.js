var COLUMN_CLASSES = {
  '0': 'code',
  '1': 'name',
  '2': 'blanks',
  '3': 'biomaterials',
  '4': 'containers',
  '5': 'due-date',
  '6': 'result-type',
  '7': 'edit-link'
}


function get_data(field) {
  var data_from_server = $.get(url='/get_data', data=field);
  return data_from_server;
};


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
            if (COLUMN_CLASSES[col] != 'edit-link') {
              var column = $('<td></td>')
              column.text(json[group][subgroup][service][col])
              column.addClass(COLUMN_CLASSES[col])
              $(row).append(column)
              $(nom_table).append(row)
            } else {
              var column = $('<td></td>')
              column.addClass(COLUMN_CLASSES[col])
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

  $('form input').click(function (action) {
    var new_data = get_data('keycode')
    console.log(new_data.responseJSON)
    var input_id = action.currentTarget.name
    var column = $(`.${input_id}`)
    var column_class_list = column[0].classList
    if (!column_class_list.contains('visible')) {
      column.addClass('visible')
    } else {
      column.removeClass('visible')
    };
  });
});
