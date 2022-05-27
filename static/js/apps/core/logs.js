$(document).ready(function () {
    var url_status = window.location.pathname;
    $('#logs').addClass('active');

    aoColumns = [
        {
            'sWidth': '15%',
            className: 'text-left',
            'bSortable': false,
        }, {
            'sWidth': '5%',
            'bSortable': false,
        }, {
            'sWidth': '10%',
            'bSortable': false,
        }, {
            'sWidth': '50%',
            className: 'text-left',
            'bSortable': false,
        }, {
            'sWidth': '12%',
            'bSortable': false,
        },
        {
            'sWidth': '8%',
            'bSortable': false,
        }
    ];

    var table_logs = $('#tlogs').DataTable({
        responsive: true,
        "sDom": 'l<"toolbar">frtip',
        language: language_datatable,
        "bProcessing": true,
        "bServerSide": true,
        stateSave: true,
        "searching": false,
        "columns": aoColumns,
        "PagingType": "full_numbers",
        "sAjaxSource": url_status,
        "columnDefs": [
            {
                className: "text-center",
                "targets": "_all",
            },
        ],
        fnServerData: function (sSource, aoData, fnCallback) {
            aoData.push({
                "name": "csrfmiddlewaretoken",
                "value": getCookie('csrftoken'),
            });
            aoData.push({
                "name": "oper",
                "value": "list-logs"
            });

            if ($('#log-admin').prop('checked')) {
                aoData.push({
                    "name": "log_admin",
                    "value": $("#log-admin").prop('checked')
                });
            }
            if ($('#exception-logs').prop('checked')) {
                aoData.push({
                    'name': 'exception-logs',
                    'value': $('#exception-logs').prop('checked')
                });
            }
            if ($("#log-user").val() != "") {
                aoData.push({
                    "name": "user",
                    "value": $("#log-user").val()
                });
            }
            if ($("#log-action").val() != "T") {
                aoData.push({
                    "name": "action",
                    "value": $("#log-action").val()
                });
            }
            if ($("#log-module").val() != "T") {
                aoData.push({
                    "name": "module",
                    "value": $("#log-module").val()
                });
            }
            if ($("#log-date-from-val").val()) {
                aoData.push({
                    "name": "date_from",
                    "value": $("#log-date-from-val").val()
                });
            }
            if ($("#log-date-to-val").val()) {
                aoData.push({
                    "name": "date_to",
                    "value": $("#log-date-to-val").val()
                });
            }


            $.ajax({
                "dataType": "json",
                "type": "POST",
                "url": sSource,
                "data": aoData,
                "success": function (json) {
                    fnCallback(json);
                    console.log(json);
                }
            });
        }
    });

    $("#log-admin, #exception-logs").change(function () {
        table_logs.ajax.reload();
    });
    $("#log-user").keyup(function (e) {
        len = $(this).val().length
        if ((0 == len || len > 2) && is_valid_key(e.which)) {
            table_logs.draw();
        }
    });
    $("#log-action").change(function (e) {
        table_logs.draw();
    });
    $("#log-module").change(function (e) {
        table_logs.draw();
    });
    $(function () {
        $("#log-date-from").datetimepicker({
            locale: language,
            format: "DD-MM-YYYY",
            sideBySide: true
        });
        $("#log-date-to").datetimepicker({
            locale: language,
            format: "DD-MM-YYYY",
            sideBySide: true
        });
    });
    $("#log-date-from").on("dp.change", function (e) {
        $("#log-date-to").data("DateTimePicker").minDate(e.date);
        if ($("#log-date-from-val").val() != "") {
            table_logs.draw();
        }
    });
    $("#log-date-to").on("dp.change", function (e) {
        $('#log-date-from').data("DateTimePicker").maxDate(e.date);
        if ($("#log-date-to-val").val() != "") {
            table_logs.draw();
        }
    });

    $(document).on("click", "#clean-logs", function (event) {
        $('#log-user').val("");
        $('#exception-logs').prop('checked', false)
        $("#log-action, #log-module").prop("selectedIndex", 0).change();
        $("#log-date-from-val").val("");
        $("#log-date-to-val").val("");
        table_logs.ajax.reload();
    });

    $("#refresh_logs").click(function () {
        table_logs.ajax.reload();
    });

    $('#multi-select').dropdown();
    $('.ui.multiple.dropdown').dropdown({
        onAdd: function (value, text, $selected) {
            var column = table_downloads.column($selected.attr('data-value'));
            visible = column.visible();
            if (visible)
                return
            column.visible(!visible);
        },
        onRemove: function (value, text, $selected) {
            var column = table_downloads.column($selected.attr('data-value'));
            visible = column.visible();
            if (!visible)
                return
            column.visible(!visible);
        }
    });

    // $(document).on('click', '.se', function(e){
    //     e.preventDefault();
    //     $("#show_exception").html($('.se').val());
    //     $('#show_exception_modal').modal('show');

    // });

});