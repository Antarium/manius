var main = function () {
  google.charts.load('current', {'packages':['gauge','line', 'corechart','controls','table'], 
    'language': 'ru'});
  google.charts.setOnLoadCallback(drawChartMain);
  google.charts.setOnLoadCallback(drawChart);
  google.charts.setOnLoadCallback(drawTable);
}

function drawChartMain(){

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
      var linechartDiv = document.getElementById('linechart_div');

      var data = new google.visualization.DataTable();
      data.addColumn('date', 'Дата');
      data.addColumn('number', "Баланс");

      data.addRows([
        [new Date(2014, 0, 1),  5.7],
        [new Date(2014, 0, 5),  3],
        [new Date(2014, 0, 10),  5],
        [new Date(2014, 0, 15),  4],
        [new Date(2014, 0, 20),  6],
        [new Date(2014, 0, 25),  6],
        [new Date(2014, 0, 30),  10],
        [new Date(2014, 1,1),   8.7],
        [new Date(2014, 2,1),   12],
        [new Date(2014, 3,1),  15.3],
        [new Date(2014, 4,1),  18.6],
        [new Date(2014, 5,1),  20.9],
        [new Date(2014, 6,1), 19.8],
        [new Date(2014, 7,1), 16.6],
        [new Date(2014, 8,1),  13.3],
        [new Date(2014, 9,1),  9.9],
        [new Date(2014, 10,1), 6.6],
        [new Date(2014, 11,1), 4.5]
      ]);

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
    }

function drawTable() {
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Дата');
        data.addColumn('string', 'Изменение счета');
        data.addColumn('string', 'Цель');
        data.addColumn('string', 'Баланс');
        data.addRows([
          ['01.01.2017', '-10000' , 'Не указано', '60000'],
          ['01.01.2017', '-10000' , 'Не указано', '50000'],
          ['02.01.2017', '-20000' , 'Не указано', '30000'],
          ['03.01.2017', '10000' , 'Не указано', '40000'],
          ['04.01.2017', '10000' , 'Не указано', '50000'],
          ['04.01.2017', '30000' , 'Не указано', '80000'],
          ['07.01.2017', '-10000' , 'Не указано', '70000'],

        ]);

        var table = new google.visualization.Table(document.getElementById('history_table_div'));

        table.draw(data, {showRowNumber: true, width: '100%', height: '100%'});
    }

$(document).ready(main);

