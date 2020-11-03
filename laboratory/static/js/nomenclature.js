var COLUMN_CLASSES = {
  '0': 'code',
  '1': 'name',
  '2': 'blanks',
  '3': 'biomaterials',
  '4': 'containers',
  '5': 'due_date',
  '6': 'result_type',
  '7': 'edit-link',
  '8': 'type',
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
          row.attr('id', json[group][subgroup][service][7])

          for(col in json[group][subgroup][service]) {
            var column = $('<td></td>')
            column.addClass(COLUMN_CLASSES[col])

            if (COLUMN_CLASSES[col] != 'edit-link') {
              column.text(json[group][subgroup][service][col])
            } else {
              var edit_link = $('<a>ИНФО</a>')
              edit_link.attr('href', `/services_view/${json[group][subgroup][service][col]}`)
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
    var groups = $('.group').children('td')
    var current_colspan = groups.attr('colspan')
    var subgroups = $('.subgroup').children('td')
    var condition = action.currentTarget.checked
    var input_id = action.currentTarget.name
    var model = action.target.attributes.model.textContent
    var column = $(`.${input_id}`)
    if (column.length > 1) {
      if (condition) {
        column.removeClass('visible')
        var new_colspan = Number(current_colspan) + 1
        groups.attr('colspan', new_colspan)
        subgroups.attr('colspan', new_colspan)
      } else {
        column.addClass('visible')
        var new_colspan = Number(current_colspan) - 1
        groups.attr('colspan', new_colspan)
        subgroups.attr('colspan', new_colspan)
      };
    } else {
      var new_data = $.getJSON(`/get_data/${model}/${input_id}`, function(json) {
        var new_colspan = Number(current_colspan) + 1
        groups.attr('colspan', new_colspan)
        subgroups.attr('colspan', new_colspan)
        for (itm in json) {
          var selector = "#" + itm
          var row = $(selector)
          var column = $('<td></td>')
          column.addClass(input_id)
          column.text(json[itm])
          $(row).append(column)
        };
      });
    };
  });
});
