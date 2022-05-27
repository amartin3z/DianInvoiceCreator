function number_format(number, decimals, dec_point, thousands_sep) {
    number = (number + '').replace(',', '').replace(' ', '');
    var n = !isFinite(+number) ? 0 : +number,
            prec = !isFinite(+decimals) ? 0 : Math.abs(decimals),
            sep = (typeof thousands_sep === 'undefined') ? ',' : thousands_sep,
            dec = (typeof dec_point === 'undefined') ? '.' : dec_point,
            s = '',
            toFixedFix = function (n, prec) {
                var k = Math.pow(10, prec);
                return '' + Math.round(n * k) / k;
            };
    s = (prec ? toFixedFix(n, prec) : '' + Math.round(n)).split('.');
    if (s[0].length > 3) {
        s[0] = s[0].replace(/\B(?=(?:\d{3})+(?!\d))/g, sep);
    }
    if ((s[1] || '').length < prec) {
        s[1] = s[1] || '';
        s[1] += new Array(prec - s[1].length + 1).join('0');
    }
    return s.join(dec);
}

var chartJSON =  {
  type: 'line',
  data: {},
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true,
          callback: function(value, index, values) {
            return number_format(value);
          }
        }
      }]
    },
    tooltips: {
      callbacks: {
        label: function(tooltipItem, chart){
          var datasetLabel = chart.datasets[tooltipItem.datasetIndex].label || '';
            return datasetLabel + ' ' + number_format(tooltipItem.yLabel, 2);
          }
        }
      }
  }
}

var chartPUE = null;
var chartPPD = null;
var chartExpense = null;
var chartPayroll = null;
var chartPayment = null;

function generateGraph(){
  dataToGraph = new FormData();
  branchName = $('#branch_filter').val();
  console.log(branchName);
  if (branchName === '' || branchName === null){
    branchName = '';
  }
  $('#strong-branch-name').text(branchName);
  dataToGraph.append('csrfmiddlewaretoken', getCookie('csrftoken'));
  dataToGraph.append('branch_name', branchName);
  $.ajax({
    type: 'POST',
    url: '/billing/branch-detail/',
    async: true,
    data: dataToGraph,
    dataType: 'json',
    cache: false,
    contentType: false,
    processData: false,
    success: function(response){
      $.map([
          {id: 'chartPUE', chartData: 'get-pue'}, 
          {id: 'chartPPD', chartData: 'get-ppd'}, 
          {id: 'chartExpense', chartData: 'get-expense'}, 
          {id: 'chartPayroll', chartData: 'get-payroll'}, 
          {id: 'chartPayment', chartData: 'get-payment'}],
        function(chartResponse){
          const toRenderResponse = {...chartJSON};
          toRenderResponse.data = {
            labels: response.labels,
            datasets: [response[chartResponse.chartData]],
          }
          if (chartResponse.id === 'chartPUE'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartPUE !== null){
              chartPUE.destroy();
            }
            chartPUE = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartPPD'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartPPD !== null){
              chartPPD.destroy();
            }
            chartPPD = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartExpense'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartExpense !== null){
              chartExpense.destroy();
            }
            chartExpense = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartPayroll'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartPayroll !== null){
              chartPayroll.destroy();
            }
            chartPayroll = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartPayment'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartPayment !== null){
              chartPayment.destroy();
            }
            chartPayment = new Chart(ctt, toRenderResponse);
          }
        }
      );
      /*
      * To get how many chart instances has been created
      Chart.helpers.each(Chart.instances, function(instance){
        alert(instance.chart.canvas.id)
      });
      */
    }
  });
}

//$("#branch_filter").keyup(function(e) {
//    generateGraph();    
//});


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
  var select2 = $('#branch_filter');
  if (select2.length > 0){
    var oper = 'get-branch';
    if (select2.hasClass("select2-hidden-accessible")) {
      select2.select2('destroy');
    }
    select2.select2({
      ajax:{
        url: '/billing/branch-detail/',
        method: 'POST',
        dataType: 'json',
        delay: 250,
        data: function(params){
          return { 
            oper: oper,
            csrfmiddlewaretoken: getCookie('csrftoken'),
            branch: params.term
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
      placeholder: 'Nombre Sucursal',
      minimumInputLength: 2,
      //maximumSelectionLength: 13,
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

$(document).ready(function(e){
  initSelect2();
  generateGraph();

  $('#download_report_branch').change(function(event) {
        $("#download_report_branch").attr("disabled", true);
        report_type = $("#download_report_branch").val()
        if (["csv", "png"].indexOf(report_type) == -1) {
            $("#download_report_branch").attr("disabled", false);
            return;
        }
        $("#icon_download").removeClass("fa-download").addClass("fa-spinner fa-spin text-primary");
        $("#icon_download").addClass("fa-spinner fa-spin text-primary");
        $(document.body).css({"cursor" : "wait"});
        token = getCookie('csrftoken');
        branchName = $('#branch_filter').val();

        chartPUE = $('#chartPUE').get(0);
        chartPPD = $('#chartPPD').get(0);
        chartExpense = $('#chartExpense').get(0);
        chartPayment = $('#chartPayment').get(0);
        chartPayroll = $('#chartPayroll').get(0);

        chartPUE = chartPUE.toDataURL();
        chartPPD = chartPPD.toDataURL();
        chartExpense = chartExpense.toDataURL();
        chartPayment = chartPayment.toDataURL();
        chartPayroll = chartPayroll.toDataURL();

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
            "name": "branch_name",
            "value": branchName
        });

        data.push({
            "name": "chartPUE",
            "value": chartPUE
        });

        data.push({
            "name": "chartPPD",
            "value": chartPPD
        });

        data.push({
            "name": "chartExpense",
            "value": chartExpense
        });

        data.push({
            "name": "chartPayroll",
            "value": chartPayroll
        });

        data.push({
            "name": "chartPayment",
            "value": chartPayment
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_billing_branch_chart/',
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