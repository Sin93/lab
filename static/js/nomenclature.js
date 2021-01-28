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

    for(var group in json) {
      if (group != 'Нет') {
        var row = $('<tr></tr>')
        row.addClass('group')
        var cols = $('<td colspan=8></td>')
        cols.text(group)
        $(row).append(cols)
        nom_table = $('table')
        $(nom_table).append(row)
      }

      for(subgroup in json[group]) {
        if (subgroup != 'Нет') {
          if (json[group][subgroup].length > 0) {
            var row = $('<tr></tr>')
            row.addClass('subgroup')
            var cols = $('<td colspan=8></td>')
            cols.text(subgroup)
            cols.css('background-color', 'DarkOrange')
            $(row).append(cols)
            nom_table = $('table')
            $(nom_table).append(row)
          }
        }

        for(service in json[group][subgroup]) {
          console.log(json[group][subgroup][service]['pk'])
          nom_table = $('table')
          var row = $('<tr></tr>')
          row.addClass('service')
          row.click(function(event) {
            if (event.currentTarget.classList.value.indexOf('active') == -1) {
              $(event.currentTarget).addClass('active')
              console.log(event)
            } else {
              $(event.currentTarget).removeClass('active')
              console.log(event)
            };
          });

          row.attr('id', json[group][subgroup][service][7])

          var name = json[group][subgroup][service][1] == null ? '' : json[group][subgroup][service][1]
          var blanks = json[group][subgroup][service][2] == null ? '' : json[group][subgroup][service][2]
          var biomaterials = json[group][subgroup][service][3] == null ? '' : json[group][subgroup][service][3]
          var containers = json[group][subgroup][service][4] == null ? '' : json[group][subgroup][service][4]
          var due_date = json[group][subgroup][service][5] == null ? '' : json[group][subgroup][service][5]
          var result_type = json[group][subgroup][service][6] == null ? '' : json[group][subgroup][service][6]

          var a = $(`<td class="code">${json[group][subgroup][service][0]}</td>` +
            `<td class="name">${name}</td>` +
            `<td class="blanks">${blanks}</td>` +
            `<td class="biomaterials">${biomaterials}</td>` +
            `<td class="containers">${containers}</td>` +
            `<td class="due_date">${due_date}</td>` +
            `<td class="result_type">${result_type}</td>` +
            `<td class="edit-link"><a href="/services_view/${json[group][subgroup][service][7]}" target="_blank" class="btn btn-success btn-sm">ИНФО</a></td>`)
          $(row).append(a)
          $(nom_table).append(row)
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
