var pieChart = null;
var num_ingreso = null;
var num_egreso = null;
var total_ingreso = null;
var total_total_egreso = null;
//var year = null;
//var month = null;
var titulo = null;
function oilChart1(year=null, month =null){
    var oilCanvas = document.getElementById("oilChart_1").getContext('2d');
    if (pieChart != null){
        pieChart.destroy();
    }

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;
    
    var num1=0;
    var num2=0;
    var num3=0;
    var num4=0;
    var num5=0;

    var oilChartForm1 = new FormData();
    oilChartForm1.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    //oilChartForm1.append('oper', 'oil-chart1');
    if (year != null && month != null && year != 'T' && month != 'A'){
          oilChartForm1.append('year', year);
          oilChartForm1.append('month', month);
    }
    //return oilChartForm1;
    $.ajax({
      type: 'POST',
      async: true,
      data: oilChartForm1,
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      success: function(response){

        
        //if (titulo == null){
        //  titulo = $('#titulo').text('');
        //}
        //titulo = $('#titulo').text(response.month + ' ' + response.year);
        year = response.year;
        month = response.month;
        if (month == null){
          var total_pue = 0.00;
          total_pue = $('#total_pue_em').text(total_pue);
          $('#total_pue_em').each(function () {
            var total_pue = $(this).text();
            var num = Number(total_pue).toLocaleString('en', { style: 'currency', currency: 'USD' });    
            
            $(this).text(num);    
          });
        }else{
          total_pue = $('#total_pue_em').text(response.total_pue);
          $('#total_pue_em').each(function () {
              var total_pue = $(this).text();
              var num = Number(total_pue).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);    
          });
        }
        if (month == null){
          var total_ppd = 0.00;
          total_ppd = $('#total_ppd_em').text(total_ppd);
          $('#total_ppd_em').each(function () {
            var total_ppd = $(this).text();
            var num = Number(total_ppd).toLocaleString('en', { style: 'currency', currency: 'USD' });    
            
            $(this).text(num);    
          });
        }else{
          total_ppd =  $('#total_ppd_em').text(response.total_ppd);
          $('#total_ppd_em').each(function () {
              var total_ppd = $(this).text();
              var num = Number(total_ppd).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (month == null){
          var total_egreso = 0.00;
          total_egreso = $('#total_egre_em').text(total_egreso);
          $('#total_egre_em').each(function () {
            var total_egreso = $(this).text();
            var num = Number(total_egreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
            
            $(this).text(num);    
          });
        }else{
          total_egreso= $('#total_egre_em').text(response.total_egreso); 
          $('#total_egre_em').each(function () {
              var total_egreso = $(this).text();
              var num = Number(total_egreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (month == null){
          var total_tras = 0.00;
          total_tras = $('#total_tras_em').text(total_tras);
          $('#total_tras_em').each(function () {
            var total_tras = $(this).text();
            var num = Number(total_tras).toLocaleString('en', { style: 'currency', currency: 'USD' });    
            
            $(this).text(num);    
          });
        }else{
          var total_tras= $('#total_tras_em').text(response.total_tras);
          $('#total_tras_em').each(function () {
              var total_tras = $(this).text();
              var num = Number(total_tras).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (month == null){
          var total_pago = 0.00;
          total_pago = $('#total_pagos_em').text(total_pago);
          $('#total_pagos_em').each(function () {
            var total_pago = $(this).text();
            var num = Number(total_pago).toLocaleString('en', { style: 'currency', currency: 'USD' });    
            
            $(this).text(num);    
          });
        }else{
          var total_pago=$('#total_pagos_em').text(response.total_pago);
          $('#total_pagos_em').each(function () {
              var total_pago = $(this).text();
              var num = Number(total_pago).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          }); 
        }
        if (response.month == null){
          var total_ingreso1 = 0.00;
          
          total_ingreso = $('#total_ingreso').text(total_ingreso1);     
          $('#total_ingreso').each(function () {
              var total_ingreso = $(this).text();
              num_ingreso = Number(total_ingreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num_ingreso);
          });
        }else{
          
          var total_ingreso1 = parseFloat(response.total_pue) + parseFloat(response.total_pago) - parseFloat(response.total_egreso)
          total_ingreso = $('#total_ingreso').text(total_ingreso1);     
          $('#total_ingreso').each(function () {
              var total_ingreso = $(this).text();
              num_ingreso = Number(total_ingreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num_ingreso);
              
          });
        }
        if (response.month == null){
          var total_total_egreso1 = 0.00;
          total_total_egreso = $('#total_total_egreso').text(total_total_egreso1);
          $('#total_total_egreso').each(function () {
              var total_total_egreso = $(this).text();
              num_egreso = Number(total_total_egreso).toLocaleString('en', { style: 'currency', currency: 'USD'});    
              
              $(this).text(num_egreso);
              
          });

        }else{
          var total_total_egreso1 = parseFloat(response.total_rec_pue) + parseFloat(response.total_rec_pago) - parseFloat(response.total_rec_egreso)
          total_total_egreso = $('#total_total_egreso').text(total_total_egreso1);
          $('#total_total_egreso').each(function () {
              var total_total_egreso = $(this).text();
              num_egreso = Number(total_total_egreso).toLocaleString('en', { style: 'currency', currency: 'USD'});    
              
              $(this).text(num_egreso);
              
          });
        }
        
        if (parseFloat(total_ingreso1) == parseFloat(total_total_egreso1)){
            
            total_ingreso = document.getElementById('total_ingreso').style.color="black";
            total_total_egreso = document.getElementById('total_total_egreso').style.color="black";

        }

        if (parseFloat(total_ingreso1) > parseFloat(total_total_egreso1)){
            
            total_ingreso = document.getElementById('total_ingreso').style.color="green";

        }
        if(parseFloat(total_ingreso1) < parseFloat(total_total_egreso1)){
            total_total_egreso = document.getElementById('total_ingreso').style.color="red";

        }

        var total_num_pue = response.total_num_pue;
        var total_num_ppd = response.total_num_ppd;
        var total_num_egreso = response.total_num_egreso;
        var total_num_transfer = response.total_num_transfer;
        var total_num_payment = response.total_num_payment;

        var oilData = {
          labels: [
            "#PUE",
            "#PPD",
            "#EGRESOS",
            "#TRASLADOS",
            "#PAGOS"
        ],
        datasets: [
            {
                data: [total_num_pue, total_num_ppd, total_num_egreso, total_num_transfer, total_num_payment],
                backgroundColor: [
                    "#B5BF00",
                    "#E42B0A",
                    "#916215",
                    "#F9890B",
                    "#FFC300"
                ]
            }]
        }
        pieChart = new Chart(oilCanvas, {
          type: 'doughnut',
          data: oilData,
        });

      }
  });

}
var pieChart2 = null;

function oilChart2(year=null, month=null){

    var oilCanvas = document.getElementById("oilChart_2").getContext('2d');
    if (pieChart2 != null){
        pieChart2.destroy();
    }

    Chart.defaults.global.defaultFontFamily = "Lato";
    Chart.defaults.global.defaultFontSize = 18;


    var num1=0;
    var num2=0;
    var num3=0;
    var num4=0;
    var num5=0;
    

    var oilChartForm1 = new FormData();
    oilChartForm1.append('csrfmiddlewaretoken', getCookie('csrftoken'));
    if (year != null && month != null && year != 'T' && month != 'A'){
      oilChartForm1.append('year', year);
      oilChartForm1.append('month', month);
    }
    $.ajax({
      type: 'POST',
      async: true,
      data: oilChartForm1,
      dataType: 'json',
      cache: false,
      contentType: false,
      processData: false,
      success: function(response){

        if (response.month == null){
          var total_rec_pue = 0.00;
          
          total_rec_pue = $('#total_pue_rec').text(total_rec_pue);     
          $('#total_pue_rec').each(function () {
              var total_rec_pue = $(this).text();
              num = Number(total_rec_pue).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
          });
        }else{
          total_rec_pue= $('#total_pue_rec').text(response.total_rec_pue);
          $('#total_pue_rec').each(function () {
              var total_rec_pue = $(this).text();
              var num = Number(total_rec_pue).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (response.month == null){
          var total_rec_ppd = 0.00;
          
          total_rec_ppd = $('#total_ppd_rec').text(total_rec_ppd);     
          $('#total_ppd_rec').each(function () {
              var total_rec_ppd = $(this).text();
              num = Number(total_rec_ppd).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
          });
        }else{

          var total_rec_ppd= $('#total_ppd_rec').text(response.total_rec_ppd);
          $('#total_ppd_rec').each(function () {
              var total_rec_ppd = $(this).text();
              var num = Number(total_rec_ppd).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (response.month == null){
          var total_rec_egreso = 0.00;
          
          total_rec_egreso = $('#total_egre_rec').text(total_rec_egreso);     
          $('#total_egre_rec').each(function () {
              var total_rec_egreso = $(this).text();
              num = Number(total_rec_egreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
          });
        }else{
          total_rec_egreso= $('#total_egre_rec').text(response.total_rec_egreso);
          $('#total_egre_rec').each(function () {
              var total_rec_egreso = $(this).text();
              var num = Number(total_rec_egreso).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }if (response.month == null){
          var total_rec_tras = 0.00;
          
          total_rec_tras = $('#total_tras_rec').text(total_rec_tras);     
          $('#total_tras_rec').each(function () {
              var total_rec_tras = $(this).text();
              num = Number(total_rec_tras).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
          });
        }else{
          var total_rec_tras= $('#total_tras_rec').text(response.total_rec_tras);
          $('#total_tras_rec').each(function () {
              var total_rec_tras = $(this).text();
              var num = Number(total_rec_tras).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        if (response.month == null){
          var total_rec_pago = 0.00;
          
          total_rec_pago = $('#total_pagos_rec').text(total_rec_pago);     
          $('#total_pagos_rec').each(function () {
              var total_rec_pago = $(this).text();
              num = Number(total_rec_pago).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
          });
        }else{

          var total_rec_pago= $('#total_pagos_rec').text(response.total_rec_pago);
          $('#total_pagos_rec').each(function () {
              var total_rec_pago = $(this).text();
              var num = Number(total_rec_pago).toLocaleString('en', { style: 'currency', currency: 'USD' });    
              
              $(this).text(num);
              
          });
        }
        
        var total_num_pue_rec = response.total_num_pue_rec
        var total_num_ppd_rec = response.total_num_ppd_rec
        var total_num_egreso_rec = response.total_num_egreso_rec
        var total_num_transfer_rec = response.total_num_transfer_rec
        var total_num_payment_rec = response.total_num_payment_rec

         var oilData = {
           labels: [
             "#PUE",
             "#PPD",
             "#EGRESOS",
             "#TRASLADOS",
             "#PAGOS"
         ],
         datasets: [
             {
                 data: [total_num_pue_rec, total_num_ppd_rec, total_num_egreso_rec, total_num_transfer_rec, total_num_payment_rec],
                 backgroundColor: [
                     "#B5BF00",
                     "#E42B0A",
                     "#916215",
                     "#F9890B",
                     "#FFC300"
                 ]
             }]
         }

        pieChart2 = new Chart(oilCanvas, {
           type: 'doughnut',
           data: oilData,
         });
        }

    });
}

$(document).on("click", "#clean-filter", function(event){

  $("#select_year, #select_month").prop("selectedIndex",0).change();
  $("#total_pue_em").text("$0.00");
  $("#total_ppd_em").text("$0.00"); 
  $("#total_egre_em").text("$0.00");
  $("#total_tras_em").text("$0.00");
  $("#total_pagos_em").text("$0.00");
  $("#total_ingreso").text("$0.00").css('color', 'black');
  $("#total_total_egreso").text("$0.00").css('color', 'black');
  $("#total_pue_rec").text("$0.00");
  $("#total_ppd_rec").text("$0.00");
  $("#total_egre_rec").text("$0.00");
  $("#total_tras_rec").text("$0.00"); 
  $("#total_pagos_rec").text("$0.00");
  $('#titulo').text(' ');
  pieChart.destroy();
  pieChart2.destroy();

});
var meses = [" ",
  "Enero", "Febrero", "Marzo",
  "Abril", "Mayo", "Junio", "Julio",
  "Agosto", "Septiembre", "Octubre",
  "Noviembre", "Diciembre"
]

$(document).ready(function(){
    oilChart1();
    oilChart2();
    $('#select_year , #select_month').change(function(){
        year = $('#select_year').val();
        month = $('#select_month').val();
        
        if (year != null && month != null && year != 'T' && month != 'A'){
          //titulo = $('#titulo').text(response.month + ' ' + response.year);
          //mes = Date.parse(month);
          titulo = $('#titulo').text(meses[month] + ' ' + year);
          oilChart1(year, month)
          oilChart2(year, month)

        }
        
    });
    
    var currentDate = new Date();
      $('#select_year').val(currentDate.getFullYear()).trigger('change');
      $('#select_month').val(currentDate.getMonth()+1).trigger('change');
})