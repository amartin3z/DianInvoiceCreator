$(document).ready(function() {

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;

    var pieCanvas = document.getElementById("billing-branch-pie");
    var pieChart;

    var dateReportBranch = new Date();
    dateReportBranch.setMonth(dateReportBranch.getMonth() - 1);

    $("#billing-branch-date").datetimepicker({
        locale: "es",
        format: "YYYY-MM",
        sideBySide: true,
        date: dateReportBranch
    });

    $('#billing-branch-date').data("DateTimePicker").minDate(new Date(2018, 12, 1));
    $('#billing-branch-date').data("DateTimePicker").maxDate(new Date());

    $("#billing-branch-date").on("dp.change", function(e) {

        var graph_date = $("#billing-branch-date-res").val();
        var data = new FormData();
        data.append('oper', 'billing-branch-total');
        data.append('csrfmiddlewaretoken', getCookie('csrftoken'));
        data.append('date', graph_date);

        $.ajax({
            type: 'POST',
            url: '/billing/branch/?data='+graph,
            async: true,
            data: data,
            dataType: 'json',
            cache: false,
            contentType: false,
            processData: false,
            success: function(response){
                if (pieChart != undefined) {
                    pieChart.destroy();
                }
                pieChart = new Chart(pieCanvas, {
                  type: 'doughnut',
                  data: response
                });
            }
          });

    });

    $( "#billing-branch-date" ).trigger( "dp.change" );


    $('#download_report_branch').change(function(event) {
        $("#download_report_branch").attr("disabled", true);
        report_type = $("#download_report_branch").val()
        if (["csv", "pdf"].indexOf(report_type) == -1) {
            $("#download_report_branch").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        token = getCookie('csrftoken');
        branch_date = $('#billing-branch-date-res').val();
        data = [{
            "name": "csrfmiddlewaretoken",
            "value": token
        }];
        
        data.push({
            "name": "oper",
            "value": "list-downloads"
        });
       
        data.push({
            "name": "get_report_branch",
            "value": 'True'
        });

        data.push({
            "name": "report_type",
            "value": report_type
        });

        data.push({
            "name": "branch_date",
            "value": branch_date
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_billing_branch_total/',
            data: data,
            cache: false,
            dataType: 'json',
        }).done(function(response) {
            $("#download_report").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $(document.body).css({"cursor" : "default"});
            if (response.success) {
                window.open(response.url);
            } else {
                error_message(response.message)
            }
        }).fail(function(jqXHR, status, errorThrown) {
            $("#download_report_branch").attr("disabled", false);
            $("#icon_download").removeClass("fa-spinner fa-spin").addClass("fa-download");
            $("#icon_download").removeClass("fa-spinner fa-spin text-primary");
            $(document.body).css({"cursor" : "default"});
        });
        
        $('#download_report_branch').val("select").change();
    });
    

});