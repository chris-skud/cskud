google.setOnLoadCallback(drawChart);
google.load('visualization', '1', {packages: ['corechart']});
function drawChart() {
  var data = google.visualization.arrayToDataTable([
    ['Weekly', 'Releases'],
    ['2-Sept', 5],
    ['9-Sept', 2],
    ['16-Sept', 0],
    ['23-Sept', 8],
    ['30-Sept', 2],
    ['2-Sept', 5],
    ['9-Sept', 2],
    ['16-Sept', 0],
    ['23-Sept', 8],
    ['30-Sept', 2],
    ['2-Sept', 5],
    ['9-Sept', 2],
    ['16-Sept', 0],
    ['23-Sept', 8],
    ['30-Sept', 2],
    ['2-Sept', 5],
    ['9-Sept', 2],
    ['16-Sept', 0],
    ['23-Sept', 8],
    ['30-Sept', 2],
    ['2-Sept', 5],
    ['9-Sept', 2],
    ['16-Sept', 0],
    ['23-Sept', 8],
    ['30-Sept', 2]
  ]);

  var options = {
      title: 'Releases Over Time',
      height: 600,
      width: 800,
      hAxis: {title: 'Weeks', titleTextStyle: {color: 'red'}, slantedText: true}
  };

  var chart = new google.visualization.ColumnChart(document.getElementById('chart_div'));
  chart.draw(data, options);
}