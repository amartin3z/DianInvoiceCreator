function formatRFCResult(state){
    if (!state.id) {
      return state.text;
    }
    var state = $("<span><strong>" + state.id + "</strong> - <small>" + state.text + "</small></span>");
    return state;
}


function formatRFCSelection(state){
    if (!state.id) {
      return state.text;
    }
    var state = $("<strong>" + state.id + "</strong>");
    return state;
}

function initSelect2(){
    var select2 = $('#taxpayer_id');
    if (select2.length > 0){
      var oper = 'get-employee';
      if (select2.hasClass("select2-hidden-accessible")) {
        select2.select2('destroy');
      }
      select2.select2({
        ajax:{
          url: '/billing/client/',
          method: 'POST',
          dataType: 'json',
          delay: 250,
          data: function(params){
            return { 
              oper: oper,
              csrfmiddlewaretoken: getCookie('csrftoken'),
              taxpayer_id: params.term
            }
          },
          processResults: function(data){
            return {
              results: $.map(data.data, function(item, idx){
                console.log(item);
                return {
                  text: item.des,
                  id: item.code, 
                }
              }),
            }
          },
          cache: true
        },
        allowClear: true,
        width: '100%',
        templateResult: formatRFCResult,
        templateSelection: formatRFCSelection,
        language: "es",
        inputTooShort: function (left) {
          console.log(left);
          return 'Faltan X caracteres';
        },
        placeholder: 'RFC',
        minimumInputLength: 5,
        maximumSelectionLength: 13,
        theme: "bootstrap",
      });
      $.fn.select2.defaults.set( "theme", "bootstrap" );
      select2.on('select2:select', function (e) {
        generateGraph();
      });
      select2.on('select2:unselect', function (e) {
        generateGraph();
      });
    }
  
  }

var chartNumbers = null;

var chartJSON =  {
    type: 'bar',
    data: {},
    fill: false,
    options: {
      legend:{
        position: 'right',
      },
      scales: {
        yAxes: [{
          stacked: true,
          ticks: {
            beginAtZero: true
          }
        }],
        xAxes: [{
          stacked: true,
          ticks: {
            beginAtZero: true
          }
        }]
  
      }
    }
  }

function generateGraph(reset=false){
    var dataToGraph = new FormData();
    dataToGraph.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    var taxpayerID = $('#taxpayer_id').val();
    if (taxpayerID !== "" && taxpayerID !== null && taxpayerID != undefined){
      dataToGraph.append('taxpayer_id', taxpayerID);
    }
    $.ajax({
      type: 'POST',
      url: '/billing/report/payroll/',
      async: true,
      data: dataToGraph,
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      success: function(response){
        const toRenderResponse = {...chartJSON};
        toRenderResponse.data = {
          labels: response.labels,
          datasets: response['get-payroll'],
        }
        const ctt = document.getElementById('chartPayRoll').getContext('2d');
        if (chartNumbers !== null){
          chartNumbers.destroy();
        }
        chartNumbers = new Chart(ctt, toRenderResponse);
          
      }
    });
  }

  $(document).ready(function() {
    $('#inicio').addClass('active');
    initSelect2();
    generateGraph();

    $('#download_chart_emision').change(function(event) {
        $("#download_chart_emision").attr("disabled", true);
        report_type = $("#download_chart_emision").val()
        if (["csv", "png"].indexOf(report_type) == -1) {
            $("#download_chart_emision").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        token = getCookie('csrftoken');
        taxpayer_id = $('#taxpayer_id').val();

        data = [{
            "name": "csrfmiddlewaretoken",
            "value": token
        }];
        
        data.push({
            "name": "oper",
            "value": "list-downloads"
        });
       
        data.push({
            "name": "get_report_nomina",
            "value": 'True'
        });

        data.push({
            "name": "report_type",
            "value": report_type
        });

        data.push({
            "name": "taxpayer_id",
            "value": taxpayer_id
        });


        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_payroll/',
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
        
        $('#download_chart_emision').val("select").change();
    });

  });