$('#download_chart_emision').change(function(event) {
    $("#download_chart_emision").attr("disabled", true);
    report_type = $("#download_chart_emision").val()
    if (["csv", "xlsx"].indexOf(report_type) == -1) {
        $("#download_chart_emision").attr("disabled", false);
        return;
    }
    $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
    $("#icon_download").addClass("fa-spinner fa-spin text-primary");
    $(document.body).css({"cursor" : "wait"});
    token = getCookie('csrftoken');
    data = [{
        "name": "csrfmiddlewaretoken",
        "value": token
    }];
    
    data.push({
        "name": "oper",
        "value": "list-downloads"
    });
    if($('#taxpayer_id').val()){
        data.push({  
            "name": "taxpayer_id",
            "value": $('#taxpayer_id').val()
        })
    }

    //if (true) {}      

    data.push({
        "name": "get_report",
        "value": 'True'
    });

    $.ajax({
        type: 'POST',
        url: '/billing/generatereport_chart_emission/',
        data: data,
        cache: false,
        dataType: 'json',
    }).done(function(response) {
        $("#download_chart_emision").attr("disabled", false);
        $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
        $(document.body).css({"cursor" : "default"});
        if (response.success) {
            window.open(response.url);
        } else {
            error_message(response.message)
        }
    }).fail(function(jqXHR, status, errorThrown) {
        $("#download_chart_emision").attr("disabled", false);
        $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
        $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "default"});
    });
    
    $('#download_chart_emision').val("select").change();
});