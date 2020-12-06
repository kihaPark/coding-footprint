<%@page import="java.net.URLDecoder"%>
<%@ page language="java"
	     contentType="text/html; charset=utf-8"
	     pageEncoding="utf-8"%>

<div class="row">
<div class="col-12">
<!-- BAR CHART -->
<div class="card card-success">
<div class="card-header">
	<h3 class="card-title">매매 건수 비교 막대차트</h3>

<div class="card-tools">
	<button type="button" class="btn btn-tool" data-card-widget="collapse">
		<i class="fas fa-minus"></i>
	</button>
	<button type="button" class="btn btn-tool" data-card-widget="remove">
		<i class="fas fa-times"></i>
	</button>
</div>
</div>
<div class="card-body">
<div class="chart">
	<canvas id="barChart"
		style="min-height: 250px; height: 250px; max-height: 250px; max-width: 100%;"></canvas>
</div>
</div>
</div>
</div>
</div>

<% String region1 = (String)request.getAttribute("region1"); %>
<% String region2 = (String)request.getAttribute("region2"); %>
<!-- URLDecoder.decode(region1, "utf-8") -->
<!-- URLDecoder.decode(region2, "utf-8") -->

<br>

<div class="row">
<div class="col-12">
<!-- LINE CHART -->
<div class="card card-info">
<div class="card-header">
	<h3 class="card-title">매매 건수 비교 선차트</h3>

<div class="card-tools">
	<button type="button" class="btn btn-tool" data-card-widget="collapse">
    	<i class="fas fa-minus"></i>
    </button>
    <button type="button" class="btn btn-tool" data-card-widget="remove">
    	<i class="fas fa-times"></i>
    </button>
</div>
</div>
<div class="card-body">
<div class="chart">
	<canvas id="lineChart"
		style="min-height: 250px; height: 250px; max-height: 250px; max-width: 100%;"></canvas>
</div>
</div>
</div>
</div>
</div>


<!-- jQuery -->
<script src="/dashboard-web/plugins/jquery/jquery.min.js"></script>
<!-- Bootstrap 4 -->
<script src="/dashboard-web/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- ChartJS -->
<script src="/dashboard-web/plugins/chart.js/Chart.min.js"></script>
<!-- AdminLTE App -->
<script src="/dashboard-web/dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="/dashboard-web/dist/js/demo.js"></script>
<!-- Page specific script -->

<script>
$(function () {
	$.ajax({
		"url": "khp771/compare_chart_data",
		"method": "get",
		"data": "type=area&region1=<%= region1 %>&region2=<%= region2 %>",
		"dataType": "json",
		"success": function(data, status, xhr) {
			
			var areaChartData = {
			  labels  : data.labels,
			  datasets: [
				{
				  label               : data.regions[0],
				  backgroundColor     : 'rgba(60,141,188,0.9)',
				  borderColor         : 'rgba(60,141,188,0.8)',
				  pointRadius          : false,
				  pointColor          : '#3b8bba',
				  pointStrokeColor    : 'rgba(60,141,188,1)',
				  pointHighlightFill  : '#fff',
				  pointHighlightStroke: 'rgba(60,141,188,1)',
				  data                : data.datasets[0]
				},
				{
				  label               : data.regions[1],
				  backgroundColor     : 'rgba(210, 214, 222, 1)',
				  borderColor         : 'rgba(210, 214, 222, 1)',
				  pointRadius         : false,
				  pointColor          : 'rgba(210, 214, 222, 1)',
				  pointStrokeColor    : '#c1c7d1',
				  pointHighlightFill  : '#fff',
				  pointHighlightStroke: 'rgba(220,220,220,1)',
				  data                : data.datasets[1]
				},
			  ]
			};
			
			var areaChartOptions = {
				 maintainAspectRatio : false,
				 responsive : true,
				 legend: {
				   display: false
				 },
				 scales: {
				   xAxes: [{
					 gridLines : {
					   display : false,
					 }
				   }],
				   yAxes: [{
					 gridLines : {
					   display : false,
					 }
				   }]
				 }
			   };
			
			//-------------
			//- BAR CHART -
			//-------------
			var barChartCanvas = $('#barChart').get(0).getContext('2d')
			var barChartData = $.extend(true, {}, areaChartData)
			var temp0 = areaChartData.datasets[0]
			var temp1 = areaChartData.datasets[1]
			barChartData.datasets[0] = temp1
			barChartData.datasets[1] = temp0
		
			var barChartOptions = {
			  responsive              : true,
			  maintainAspectRatio     : false,
			  datasetFill             : false
			}
		
			var barChart = new Chart(barChartCanvas, {
			  type: 'bar',
			  data: barChartData,
			  options: barChartOptions
			})
			
			//-------------
			//- LINE CHART -
			//--------------
			var lineChartCanvas = $('#lineChart').get(0).getContext('2d')
			var lineChartOptions = $.extend(true, {}, areaChartOptions)
			var lineChartData = $.extend(true, {}, areaChartData)
			lineChartData.datasets[0].fill = false;
			lineChartData.datasets[1].fill = false;
			lineChartOptions.datasetFill = false;

			var lineChart = new Chart(lineChartCanvas, {
			type: 'line',
			data: lineChartData,
			options: lineChartOptions
			});
		},
		"error": function(xhr, status, err) {
			console.log(err.message);
		}
	});
});

</script>
