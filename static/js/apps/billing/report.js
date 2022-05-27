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

var chartNumbers = null;
var chartNumbersCancelled = null;
var chartTotals = null;
var chartTotalsCancelled = null;

function getParams(){
  var search = location.search;
  var params = {}
  if (search){
      var queries = search.split('&');
      queries.map(query => {
          query = query.replace('?', '');
          values = query.split('=');
          params[values[0]] = values[1];
      });
  }
  return params;
}

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
    var param = getParams();
    var oper = param.section == 'emission'? 'get-client' : 'get-provider';
    if (param.data == 'payroll'){
      oper = 'get-employee';
    }
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
              //console.log(item);
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
        //console.log(left);
        return 'Faltan X caracteres';
      },
      placeholder: 'RFC',
      minimumInputLength: 5,
      maximumSelectionLength: 13,
      theme: "bootstrap",
    });
    $.fn.select2.defaults.set( "theme", "bootstrap" );
    select2.on('select2:select', function (e) {
      generateGraph(destroy=true);
    });
    select2.on('select2:unselect', function (e) {
      generateGraph(destroy=true);
    });
  }

}

function getFormData(){
  var params = getParams();
  var dataToGraph = new FormData();
  var taxpayerID = $('#taxpayer_id').val();
  var section = params.section;
  if (section !== undefined){
    dataToGraph.append('view', params.section);
  }
  dataToGraph.append('oper', params.data);
  if (taxpayerID !== "" && taxpayerID !== null && taxpayerID != undefined){
    dataToGraph.append('taxpayer_id', taxpayerID);
  }
  dataToGraph.append('csrfmiddlewaretoken', getCookie('csrftoken'));
  return dataToGraph;
}

function generateGraph(reset=false){
  dataToGraph = getFormData();
  $.ajax({
    type: 'POST',
    url: '/billing/report/',
    async: true,
    data: dataToGraph,
    dataType: 'json',
    cache: false,
    contentType: false,
    processData: false,
    success: function(response){
      $.map([
          {id: 'chartNumbers', chartData: 'get-numbers'}, 
          {id: 'chartNumbersCancelled', chartData: 'get-numbers-cancelled'}, 
          {id: 'chartTotals', chartData: 'get-totals'}, 
          {id: 'chartTotalsCancelled', chartData: 'get-totals-cancelled'}], 
        function(chartResponse){
          const toRenderResponse = {...chartJSON};
          toRenderResponse.data = {
            labels: response.labels,
            datasets: response[chartResponse.chartData],
          }
          if (chartResponse.id === 'chartNumbers'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartNumbers !== null){
              chartNumbers.destroy();
            }
            chartNumbers = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartNumbersCancelled'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartNumbersCancelled !== null){
              chartNumbersCancelled.destroy();
            }
            chartNumbersCancelled = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartTotals'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartTotals !== null){
              chartTotals.destroy();
            }
            chartTotals = new Chart(ctt, toRenderResponse);
          }else if (chartResponse.id === 'chartTotalsCancelled'){
            const ctt = document.getElementById(chartResponse.id).getContext('2d');
            if (chartTotalsCancelled !== null){
              chartTotalsCancelled.destroy();
            }
            chartTotalsCancelled = new Chart(ctt, toRenderResponse);
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
function generate_report(){
  var param = getParams();
  if (param.section=='emission') {
    if (param.data=='income-pue') {
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
    }
    if(param.data == 'income-ppd'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_emissionPPD/',
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
    }
    if(param.data == 'expense'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_emissionE/',
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
    }
    if(param.data == 'payment'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_emissionP/',
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
    }
    if(param.data == 'transfer'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_emissionT/',
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
    }
    if(param.data == 'payroll'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_emissionN/',
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
    }
  }
  if (param.section=='reception') {
    if (param.data=='income-pue') {
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepPUE/',
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
    }
    if(param.data == 'income-ppd'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepPPD/',
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
    }
    if(param.data == 'expense'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepE/',
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
    }
    if(param.data == 'transfer'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepT/',
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
    }
    if(param.data == 'payment'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepP/',
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
    }
    if(param.data == 'payroll'){
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

        data.push({
            "name": "get_report",
            "value": 'True'
        });

        $.ajax({
            type: 'POST',
            url: '/billing/generatereport_chart_recepN/',
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
    }
  }

}


    

$(document).ready(function() {
  $('#inicio').addClass('active');
  initSelect2();
  generateGraph();
  generate_report();
});