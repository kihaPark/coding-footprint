<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Home</title>
    
    <!-- Google Font: Source Sans Pro -->
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
    <!-- Font Awesome -->
    <link rel="stylesheet" href="/shoseo-one//plugins/fontawesome-free/css/all.min.css">
    <!-- Theme style -->
    <link rel="stylesheet" href="/shoseo-one//dist/css/adminlte.min.css">
</head>
<!-- <body class="hold-transition sidebar-mini layout-fixed"> -->
<body class="hold-transition sidebar-collapse">

<div class="wrapper">
<jsp:include page="/WEB-INF/views/modules/header.jsp" />

<!-- Content Wrapper. Contains page content -->
<div class="content-wrapper">

<!-- Content Header (Page header) -->
<section class="content-header">
    <div class="container-fluid">
        <div class="row mb-2">
            <div class="col-sm-12">
                <h1>코스피 선물 자동매매 시스템</h1>
            </div>
        </div>
    </div>
    <!-- /.container-fluid -->
</section>

<!-- Main content -->
<section class="content">
<div class="container-fluid">
    <div class="row">
        <div class="col-md-12">

            <!-- BAR CHART -->
            <div class="card card-success">
                <div class="card-header">
                    <h3 class="card-title">차트 정보</h3>

                    <div class="card-tools">
                        <button type="button" class="btn btn-tool"
                            data-card-widget="collapse">
                            <i class="fas fa-minus"></i>
                        </button>
                        <button type="button" class="btn btn-tool"
                            data-card-widget="remove">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                </div>

                <div class="card-body">
                    <div id="chart_div" class="chart"
                        style="min-height: 300px; height: 100%; width: 100%;"></div>
                </div>
                <!-- /.card-body -->
            </div>
            <!-- /.card -->
        </div>
        <!-- /.col (RIGHT) -->
    </div>


    <div class="row">
        <div class="col-md-12">
            <div class="card card-default">
                <div class="card-body">
                    <button id="begin-trade-btn" type="button"
                        class="btn btn-primary btn-lg">거래 시작(초기화)</button>
                    <button id="next-trade-btn" type="button"
                        class="btn btn-danger btn-lg" disabled="disabled">다음 거래</button>
                   
                </div>
            </div>
        </div>
    </div>


    <div class="row">
        <div class="col-md-12">
            <div class="card card-success">
                <div class="card-header">
                    <h3 class="card-title">계좌 현황</h3>
                </div>
                
                <div class="card-body">
                    <p class="text-xl-left" id="account-date-info"></p>
                    <p class="text-xl-left" id="account-postion-info"></p>
                    <p class="text-xl-left" id="account-profit-info"></p>
                </div>
            </div>
        </div>
    </div>


    <div class="row">
        <div class="col-12">
            <div class="card card-success">
                <div class="card-header">
                    <h3 class="card-title">거래 내역(수수료 제외)</h3>
                </div>
                <!-- /.card-header -->
                
                <div id="iris-container" class="card-body table-responsive p-0" style="height: 300px;">
                <table class="table table-head-fixed text-nowrap">
                  <thead>
                    <tr>
                      <th>날짜</th>
                      <th>시간</th>
                      <th>포지션</th>
                      <th>계약지수</th>
                      <th>계약수</th>
                      <th>손익</th>
                    </tr>
                  </thead>
                  <tbody id="trade-info-table"> 
                  </tbody>
                </table>
                </div>
                <!-- /.card-body -->
            </div>
            <!-- /.card -->
        </div>
    </div>
    <!-- /.row -->

</div>
<!-- /.container-fluid -->
</section>
<!-- /.content -->

</div>
<!-- /.content-wrapper -->
        
<jsp:include page="/WEB-INF/views/modules/footer.jsp" />

</div>
<!-- ./wrapper -->

<!-- jQuery -->
<script src="/shoseo-one//plugins/jquery/jquery.min.js"></script>
<!-- Bootstrap 4 -->
<script src="/shoseo-one//plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- ChartJS -->
<script src="/shoseo-one//plugins/chart.js/Chart.min.js"></script>
<!-- AdminLTE App -->
<script src="/shoseo-one//dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="/shoseo-one//dist/js/demo.js"></script>
<!-- Google Chart -->
<script src="https://www.gstatic.com/charts/loader.js"></script>
<!-- Page specific script -->
<script>
  $(function () {
	  var ChartData = function(
			  date, time, open, high, low, close, volume) {
	      this.date = date;
	      this.time = time;
	      this.open = open;
	      this.high = high;
	      this.low = low;
	      this.close = close;
	      this.volume = volume;
	      return this;
	  }

      var AccountData = function(
    	      date, time, cCount, cPoint, cPosition,
    	      pValue, iBalance, balance, profitLoss) {
    	  this.date = date;
          this.time = time;
          this.cCount = cCount;
          this.cPoint = cPoint;
          this.cPosition = cPosition; // 0:없음, 1:매수, 2:매도
          this.pValue = pValue;
          this.iBalance = iBalance;
          this.balance = balance;
          this.profitLoss = profitLoss;
          return this;
      }

      var TradeData = function(
    	      date, time, cCount, cPoint, cPosition, pValue, action) {
          this.date = date;
          this.time = time;
          this.cCount = cCount;
          this.cPoint = cPoint;
          this.cPosition = cPosition; // 0:없음, 1:매수, 2:매도
          this.pValue = pValue;
          this.action = action; // 0:신규매수, 1:신규매도, 2:포지션 보유or관망, 3:포지션청산
          return this;
      }

      var cdArray = [];
      var adArray = [];
      var tdArray = [];

      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      var chartObj
      var chartD
      var chartOpt
      
      function drawChart() {
          chartD = new google.visualization.DataTable();
          chartD.addColumn('string', 'datetime');
          chartD.addColumn('number', 'low');
          chartD.addColumn('number', 'open');
          chartD.addColumn('number', 'close');
          chartD.addColumn('number', 'close');
          // 상승캔들 = low, open, close, high
          // 하락캔들 = high, open, close, high

          chartOpt = {
            legend:'none',
            candlestick: {
                fallingColor: { stroke: '#2c2ac7', fill: '#2c2ac7' }, // blue
                risingColor: { stroke: '#db352a', fill: '#db352a' }   // red
            }
          };

          chartObj = new google.visualization.CandlestickChart(document.getElementById('chart_div'));
          chartObj.draw(chartD, chartOpt);
      }

      function addChartData(data) {
    	  // 상승캔들 = low, open, close, high
          // 하락캔들 = high, open, close, high
          var info = [data.time, data.low, data.open, data.close, data.high]
          if (data.open > data.close) {
              info = [data.time, data.high, data.open, data.close, data.low]
          }
          chartD.addRow(info);
          chartObj.draw(chartD, chartOpt);
      }

      function clearChartData() {
          var rowCount = chartD.getNumberOfRows();
          if (rowCount == 0)
              return;
          
          chartD.removeRows(0, rowCount);
          chartObj.draw(chartD, chartOpt);
      }

      function updateChart(data) {
          var chart = new ChartData(
              data.chartData, data.chartTime, data.chartOpen, data.chartHigh,
              data.chartLow, data.chartClose, data.chartVolume);
          cdArray.push(chart);

          addChartData(chart);
      }

      function convertPosition(position) {
          var strPos = "없음";
          if (position == 1) {
              strPos = "매수";
          } else if (position == 2) {
              strPos = "매도";
          }
          return strPos;
      }

      function convertAction(action) {
          var strAct = "관망"; // action == 2
          if (action == 0) {
              strAct = "매수";
          } else if (action == 1) {
              strAct = "매도";
          } else if (action == 3) {
              strAct = "청산";
          }
          return strAct;
      }

      function commas(x) {
          return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }

      function updateAccount(data) {
          var account = new AccountData(
	          data.chartDate, data.chartTime, data.contractCount, data.contractPoint,
	          data.contractPosition, data.positionValue, data.initBalance, data.balance, data.profitLoss);
	       adArray.push(account);

	       var accDate = "- 일시:&nbsp&nbsp<b>" + account.date + "  " + account.time + "</b>";
	       $('#account-date-info').html(accDate);
	       
	       var posTxt = convertPosition(account.cPosition);
	       var accTxt1 = "- 보유 포지션:&nbsp&nbsp<b>" + posTxt + ",&nbsp&nbsp" +
	                     account.cPoint + "&nbsp포인트,&nbsp&nbsp" + account.cCount + "&nbsp계약 </b>";
	       
	       var pValue = (account.cCount == 0) ? 0 : commas(account.pValue);
	       var colorTag1 = (account.pValue >= 0) ? "<b style=\"color:red\">" : "<b style=\"color:blue\">";
	       if (account.cCount == 0) {
	    	   colorTag1 = "<b style=\"color:red\">";
		   }
	       var accTxt2 = "- 보유 포지션 손익:&nbsp&nbsp" + colorTag1 + pValue + "</b>";
	       
	       var accTxt12 = accTxt1 + "<br>" + accTxt2;
	       $('#account-postion-info').html(accTxt12);
	       
	       var accTxt3 = "- 예탁금:&nbsp&nbsp<b>" + commas(account.balance) + "</b>";

	       var profit = account.balance - account.iBalance;
	       var profitRatio = (profit / account.iBalance * 100).toFixed(2)
	       var colorTag2 = (profit >= 0.0) ? "<b style=\"color:red\">" : "<b style=\"color:blue\">";
	       var accTxt4 = "- 실현수익:&nbsp&nbsp" + colorTag2 + commas(profit) +
	                     "</b>,&nbsp&nbsp&nbsp수익률:&nbsp&nbsp" + colorTag2 + profitRatio + "&nbsp% </b>";

	       var accTxt34 = accTxt3 + "<br>" + accTxt4;
	       $('#account-profit-info').html(accTxt34);
      }

      function updateTrade(data) {
          // 보유 혹은 관망일 경우 패스
          if (data.agentAction == 2)
              return;
          
          var trade = new TradeData(
              data.chartDate, data.chartTime, data.contractCount,
              data.contractPoint, data.contractPosition, data.positionValue,
              data.agentAction);
          tdArray.push(trade);

          var posAct = convertAction(data.agentAction);
          var colorTag = "<b style=\"color:black\">";
          if (trade.pValue > 0) {
        	  colorTag = "<b style=\"color:red\">";
          } else if (trade.pValue < 0) {
        	  colorTag = "<b style=\"color:blue\">";
          }
          var row = "<tr><td>" + trade.date + "</td><td>" + trade.time + "</td><td>" +
                    posAct + "</td><td>" + trade.cPoint + "</td><td>" + trade.cCount + "</td><td>" +
                    colorTag + commas(trade.pValue) + "</b></td></tr>";
          
          $("#trade-info-table").prepend(row);
      }


	  $('#begin-trade-btn').on('click', function(event) {
          event.preventDefault();
          event.stopPropagation();
         
          $.ajax({
              "url": "begin-trade",
              "method": "GET",
              "dataType": "json",
              "success": function(data, status, xhr) {
                  cdArray = [];
                  adArray = [];
                  tdArray = [];

                  clearChartData();
                  $('#account-date-info').empty();
                  $('#account-position-info').empty();
                  $('#account-profit-info').empty();
                  $("#trade-info-table").empty()

                  updateChart(data);
                  updateAccount(data);
                  updateTrade(data);

                  $('#next-trade-btn').prop('disabled', false);
              }, 
              "error": function(xhr, status, err) {
                  console.log(err);
              }
          });
      });

	  $('#next-trade-btn').on('click', function(event) {
          event.preventDefault();
	      event.stopPropagation();
          
          $.ajax({
              "url": "next-trade",
              "method": "GET",
              "dataType": "json",
              "success": function(data, status, xhr) {
                  updateChart(data);
                  updateAccount(data);
                  updateTrade(data);
              }, 
              "error": function(xhr, status, err) {
                  console.log(err);
              }
          });
	  });

  })
</script>
</body>
</html>



