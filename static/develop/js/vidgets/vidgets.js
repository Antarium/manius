var main = function () {
  google.charts.load('current', {'packages':['gauge','line', 'corechart','controls','table'], 
    'language': 'ru'});
  //google.charts.setOnLoadCallback(drawChartMain);
  google.charts.setOnLoadCallback(drawChart);
  //google.charts.setOnLoadCallback(drawTable);
}

function drawChartGauge(){

  //получаем данные из data полей
  var balance = document.getElementById("balance").getAttribute('data-balance');
  balance = parseInt(balance);
  var start = document.getElementById("start").getAttribute('data-balance');
  start = parseInt(start)
  var redzone = document.getElementById("redzone").getAttribute('data-balance');
  redzone = parseInt(redzone)
  var greenzone = document.getElementById("greenzone").getAttribute('data-balance');
  greenzone = parseInt(greenzone)

  var data = google.visualization.arrayToDataTable([
    ['Label', 'Value'],
    ['Кошелек', balance],
  ]);
  var options = {
    redFrom: 0, redTo: redzone,
    greenFrom: greenzone, greenTo: start*2,
    minorTicks: 50,
    min: 0,
    max: start*2
  };
        
  var chart = new google.visualization.Gauge(document.getElementById('chart_div'));
  chart.draw(data, options);
}

function drawChart() {

  drawChartGauge();

//-------JQuery request---------------------
  jQuery.ajax({
    type: 'POST',
    url: 'get_full_data/',
      success: function(msg){
        data_list = jQuery.parseJSON(JSON.stringify(msg));
        account_list = data_list['account_list'];
        
        //----------------------Line Chart--------------------------
        var linechartDiv = document.getElementById('linechart_div');

        var data = new google.visualization.DataTable();
        data.addColumn('date', 'Дата');
        data.addColumn('number', "Баланс");
        
        for (var i = 0; i < account_list.length; i++) {
          data.addRows([
            [new Date(account_list[i]['year'], account_list[i]['month'], account_list[i]['day']), 
                      account_list[i]['balance']]
          ]);
        }

        // Create a dashboard.
        var dashboard = new google.visualization.Dashboard(
          document.getElementById('dashboard_div'));

        // Create a range slider, passing some options
        var RangeSlider = new google.visualization.ControlWrapper({
          'controlType': 'ChartRangeFilter',
          'containerId': 'filter_div',
          'options': {
            'filterColumnLabel': 'Дата',
            'ui': {'labelStacking': 'vertical'}
          }
        });

        var chart = new google.visualization.ChartWrapper({
          'chartType': 'LineChart',
          'containerId': 'linechart_div',
          'options': {
          //'title': 'Уникальные посетители и просмотры',
          'curveType': 'function',
          }
        });

        dashboard.bind(RangeSlider, chart);

        dashboard.draw(data);
      //---------------TABLE-----------------------------
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Дата');
        data.addColumn('string', 'Изменение счета');
        data.addColumn('string', 'Цель');
        data.addColumn('string', 'Баланс');
        for (var i = 0; i < account_list.length; i++) {
          data.addRows([
            [account_list[i]['date_string'], String(account_list[i]['change'])  , 
            account_list[i]['target'], String(account_list[i]['balance'])]
          ]);
        }

        var table = new google.visualization.Table(document.getElementById('history_table_div'));

        table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
            }
  });

}

$(document).ready(main);

