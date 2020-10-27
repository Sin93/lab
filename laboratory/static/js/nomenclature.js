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


$(document).ready(function (){
  $.getJSON('/get_nomenclature_data', {}, function (json){
    console.log('Document ready')
    for(var group in json) {
      var row = $('<tr></tr>')
      row.addClass('group')
      var cols = $('<td colspan=8></td>')
      cols.text(group)
      $(row).append(cols)
      nom_table = $('table')
      $(nom_table).append(row)

      for(subgroup in json[group]) {
        var row = $('<tr></tr>')
        row.addClass('subgroup')
        var cols = $('<td colspan=8></td>')
        cols.text(subgroup)
        $(row).append(cols)
        nom_table = $('table')
        $(nom_table).append(row)

        for(service in json[group][subgroup]) {
          nom_table = $('table')
          var row = $('<tr></tr>')
          row.attr('id', json[group][subgroup][service][0])

          for(col in json[group][subgroup][service]) {
            var column = $('<td></td>')
            column.addClass(COLUMN_CLASSES[col])

            if (COLUMN_CLASSES[col] != 'edit-link') {
              column.text(json[group][subgroup][service][col])
            } else {
              var edit_link = $('<a>Ред.</a>')
              edit_link.attr('href', json[group][subgroup][service][col])
              $(column).append(edit_link)
            };

            $(row).append(column)
            $(nom_table).append(row)
          };
        };
      };
    };
  });

  $('form input').click(function (action) {
    var condition = action.currentTarget.checked
    var input_id = action.currentTarget.name
    var new_data = $.getJSON(`/get_data/${input_id}`, function(json) {
      console.log(json['data'])
    });
    var column = $(`.${input_id}`)
    var column_class_list = column[0].classList
    if (condition) {
      column.removeClass('visible')
    } else {
      column.addClass('visible')
    };
  });
});
