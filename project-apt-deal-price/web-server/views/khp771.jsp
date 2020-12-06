<%@page import="com.dashboardweb.vo.khpDealCountVO"%>

<%@ page language="java" contentType="text/html; charset=utf-8" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Table Template</title>
	
	<!-- Google Font: Source Sans Pro -->
	<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,400i,700&display=fallback">
	<!-- Font Awesome -->
	<link rel="stylesheet" href="/dashboard-web/plugins/fontawesome-free/css/all.min.css">
	<!-- Theme style -->
	<link rel="stylesheet" href="/dashboard-web/dist/css/adminlte.min.css">
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
          <div class="col-sm-6">
            <h1>아파트 거래 통계, 예측 페이지</h1>
          </div>
          <div class="col-sm-6">
            <ol class="breadcrumb float-sm-right">
              <li class="breadcrumb-item"><a href="#">Home</a></li>
              <li class="breadcrumb-item active"></li>
            </ol>
          </div>
        </div>
      </div><!-- /.container-fluid -->
    </section>

    <!-- Main content -->
    <section class="content">
      <div class="container-fluid">
        
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-header">
                <h3 class="card-title">전국 아파트 매매 건수</h3>

                <div class="card-tools">
                  <div class="input-group input-group-sm" style="width: 150px;">
                    <input type="text" name="table_search" class="form-control float-right" placeholder="Search">

                    <div class="input-group-append">
                      <button type="submit" class="btn btn-default">
                        <i class="fas fa-search"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /.card-header -->
              <div class="card-body table-responsive p-0" style="height: 500px;">
                <table class="table table-head-fixed text-nowrap">
                  <thead>
                    <tr>
                      <th>지역</th>
                      <th>2012년</th>
                      <th>2013년</th>
                      <th>2014년</th>
                      <th>2015년</th>
                      <th>2016년</th>
                      <th>2017년</th>
                      <th>2018년</th>
                      <th>2019년</th>
                      <th>2020년</th>
                    </tr>
                  </thead>
                  <tbody>
                    <% khpDealCountVO[] dcList =
                  		(khpDealCountVO[])request.getAttribute("deal_count"); %>
                  	<% for (khpDealCountVO dc : dcList) { %>
                    <tr>
                      <td><%= dc.getRegion() %></td>
                      <td><%= dc.comma(dc.getY2012())%></td>
                      <td><%= dc.comma(dc.getY2013())%></td>
                      <td><%= dc.comma(dc.getY2014())%></td>
                      <td><%= dc.comma(dc.getY2015())%></td>
                      <td><%= dc.comma(dc.getY2016())%></td>
                      <td><%= dc.comma(dc.getY2017())%></td>
                      <td><%= dc.comma(dc.getY2018())%></td>
                      <td><%= dc.comma(dc.getY2019())%></td>
                      <td><%= dc.comma(dc.getY2020())%></td>
                    </tr>
                    <% } %>
                  </tbody>
                </table>
              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
          </div>
        </div>
        
        <br>
        <hr>
         
        <div class="row">
          <div class="col-12">
            <div class="card">
              <div class="card-header">
                <h3 class="card-title">전국 아파트 평당 평균 가격(원)</h3>

                <div class="card-tools">
                  <div class="input-group input-group-sm" style="width: 150px;">
                    <input type="text" name="table_search" class="form-control float-right" placeholder="Search">

                    <div class="input-group-append">
                      <button type="submit" class="btn btn-default">
                        <i class="fas fa-search"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
              <!-- /.card-header -->
              <div class="card-body table-responsive p-0" style="height: 500px;">
                <table class="table table-head-fixed text-nowrap">
                  <thead>
                    <tr>
                      <th>지역</th>
                      <th>2012년</th>
                      <th>2013년</th>
                      <th>2014년</th>
                      <th>2015년</th>
                      <th>2016년</th>
                      <th>2017년</th>
                      <th>2018년</th>
                      <th>2019년</th>
                      <th>2020년</th>
                    </tr>
                  </thead>
                  <tbody>
                    <% khpDealCountVO[] ppList =
                  		(khpDealCountVO[])request.getAttribute("pyung_price"); %>
                  	<% for (khpDealCountVO pp : ppList) { %>
                    <tr>
                      <td><%= pp.getRegion() %></td>
                      <td><%= pp.comma(pp.getY2012())%></td>
                      <td><%= pp.comma(pp.getY2013())%></td>
                      <td><%= pp.comma(pp.getY2014())%></td>
                      <td><%= pp.comma(pp.getY2015())%></td>
                      <td><%= pp.comma(pp.getY2016())%></td>
                      <td><%= pp.comma(pp.getY2017())%></td>
                      <td><%= pp.comma(pp.getY2018())%></td>
                      <td><%= pp.comma(pp.getY2019())%></td>
                      <td><%= pp.comma(pp.getY2020())%></td>
                    </tr>
                    <% } %>
                  </tbody>
                </table>
              </div>
              <!-- /.card-body -->
            </div>
            <!-- /.card -->
          </div>
        </div>
        
        <br>
        <hr>
        
        <div class="form-group">
		   <form id="selectform">
           <label>지역선택</label>
           <select name="region" id="region" class="form-control select2" style="width: 100%;">
             <option selected="selected" >서울특별시</option>
             <option>경기도</option>
			 <option>강원도</option>
			 <option>경상남도</option>
			 <option>경상북도</option>
			 <option>광주광역시</option>
			 <option>대구광역시</option>
			 <option>대전광역시</option>
			 <option>부산광역시</option>
			 <option>세종특별자치시</option>
			 <option>울산광역시</option>
			 <option>인천광역시</option>
			 <option>전라남도</option>
			 <option>전라북도</option>
			 <option>제주특별자치도</option>
			 <option>충청남도</option>
			 <option>충청북도</option>
           </select>
           </form>
         </div>
         
		<div style="text-align:center">
			<button id="region-search" type="button" class="btn btn-block btn-primary btn-lg">선택 지역 현황</button>
		</div>
		<br>
		
		<div id="khp-size-deal-count-list"></div>
		
		<br>
        
		<div id="khp-size-pyung-price-list"></div>
		
		<br>
        <hr>
        
        <div style="text-align:center">
			<button id="brand-apt-search" type="button" class="btn btn-block btn-primary btn-lg">브랜드 아파트 정보</button>
		</div>
		<br>
		<div id="khp-brand-apt-list"></div>
		
		<br>
        <hr>
        
        <div style="text-align:center">
			<button id="recent-deal-search" type="button" class="btn btn-block btn-primary btn-lg">최근 거래 세부정보</button>
		</div>
		<br>
		<div id="khp-recent-deal-list"></div>
		
		<br>
        <hr>
        
        <div style="text-align:center">
			<button id="apply-home-search" type="button" class="btn btn-block btn-primary btn-lg">분양 아파트 가격 예측</button>
		</div>
		<br>
		<div id="khp-apply-home-list"></div>
		
		<br>
        <hr>
        
        <div class="form-group">
            <form id="inputform">
            <label>원하는 평수를 입력하세요</label>
            <input type="text" name="pyung" id="pyung">
            </form>
        </div>
        
		<div style="text-align:center">
			<button id="predict-price-req" type="button" class="btn btn-block btn-primary btn-lg">입력 평수 가격 예측</button>
		</div>
		<br>
		<div id="khp-predict-price-result"></div>
		
		<br>
        <hr>
        
        <div class="form-group">
		   <form id="compare-select">
           <label>차트: 비교지역1</label>
           <select id="comregion1" name="comregion1" class="form-control select2" style="width: 100%;">
             <option selected="selected" >서울특별시</option>
             <option>경기도</option>
			 <option>강원도</option>
			 <option>경상남도</option>
			 <option>경상북도</option>
			 <option>광주광역시</option>
			 <option>대구광역시</option>
			 <option>대전광역시</option>
			 <option>부산광역시</option>
			 <option>세종특별자치시</option>
			 <option>울산광역시</option>
			 <option>인천광역시</option>
			 <option>전라남도</option>
			 <option>전라북도</option>
			 <option>제주특별자치도</option>
			 <option>충청남도</option>
			 <option>충청북도</option>
           </select>
           
           <br>
           
           <label>차트: 비교지역2</label>
           <select id='comregion2' name="comregion2" class="form-control select2" style="width: 100%;">
             <option selected="selected" >경기도</option>
             <option>서울특별시</option>
			 <option>강원도</option>
			 <option>경상남도</option>
			 <option>경상북도</option>
			 <option>광주광역시</option>
			 <option>대구광역시</option>
			 <option>대전광역시</option>
			 <option>부산광역시</option>
			 <option>세종특별자치시</option>
			 <option>울산광역시</option>
			 <option>인천광역시</option>
			 <option>전라남도</option>
			 <option>전라북도</option>
			 <option>제주특별자치도</option>
			 <option>충청남도</option>
			 <option>충청북도</option>
           </select>
           </form>
         </div>
         
        <div style="text-align:center">
			<button id="compare-chart1" type="button" class="btn btn-block btn-primary btn-lg">매매 건수 비교 차트</button>
		</div>
		<br>
		<div id="khp-compare-chart-view"></div>
		
		<br>
        <hr>
        
        <div style="text-align:center">
			<button id="compare-price-chart" type="button" class="btn btn-block btn-primary btn-lg">평당 가격 비교 차트</button>
		</div>
		<br>
		<div id="khp-compare-price-chart-view"></div>
		
		<br>
        <hr>
        
		<script src="http://code.jquery.com/jquery-3.5.1.js"></script>
		<script type="text/javascript">
		$(function() {
			$('#region-search').on('click', function(event) {
				var params = $('#selectform').serialize().replace(/%/g, '%25');
				//$( '#khp-size-pyung-price-list' ).text( params );
				
				$.ajax({
					"url": "khp771/size_deal_count",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-size-deal-count-list').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
				
				$.ajax({
					"url": "khp771/size_pyung_price",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-size-pyung-price-list').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
			
			$('#brand-apt-search').on('click', function(event) {
				var params = $('#selectform').serialize().replace(/%/g, '%25');
				//$( '#khp-brand-apt-list' ).text( params );
				
				$.ajax({
					"url": "khp771/brand_apt_list",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-brand-apt-list').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
			
			$('#recent-deal-search').on('click', function(event) {
				var params = $('#selectform').serialize().replace(/%/g, '%25');
				//$( '#khp-brand-apt-list' ).text( params );
				
				$.ajax({
					"url": "khp771/recent_deal_list",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-recent-deal-list').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
			
			$('#apply-home-search').on('click', function(event) {
				var params = $('#selectform').serialize().replace(/%/g, '%25');
				//$( '#apply-home-list' ).text( params );
				
				$.ajax({
					"url": "khp771/apply_home_list",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-apply-home-list').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
			
			$('#predict-price-req').on('click', function(event) {
				if($('#pyung').val() == 0) {
					$( '#khp-predict-price-result' ).text("평수를 입력하시오.");
					return;
				}
				
				var params1 = $('#selectform').serialize().replace(/%/g, '%25');
				var params2 = $('#inputform').serialize();
				var data = params1 + "&" + params2
				
				$.ajax({
					"url": "khp771/predict_price_req",
					"method": "get",
					"data": data,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-predict-price-result').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});	
			});
			
			$('#compare-chart1').on('click', function(event) {
				var params = $('#compare-select').serialize();
				//$( '#khp-compare-chart-view' ).text( params );
				
				$.ajax({
					"url": "khp771/compare_chart",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-compare-chart-view').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
			
			$('#compare-price-chart').on('click', function(event) {
				var params = $('#compare-select').serialize();
				//$( '#khp-compare-chart-view2' ).text( params );
				
				$.ajax({
					"url": "khp771/compare_price_chart",
					"method": "get",
					"data": params,
					//"async": false,
					"success": function(result, status, xhr) {
						$('#khp-compare-price-chart-view').html(result);
					},
					"error": function(xhr, status, err) {
						
					}
				});
			});
		});
		</script>
      </div><!-- /.container-fluid -->
    </section>
    <!-- /.content -->
  </div>
  <!-- /.content-wrapper -->
	    	
	<jsp:include page="/WEB-INF/views/modules/footer.jsp" />

</div>
<!-- ./wrapper -->

<!-- jQuery -->
<script src="/dashboard-web/plugins/jquery/jquery.min.js"></script>
<!-- Bootstrap 4 -->
<script src="/dashboard-web/plugins/bootstrap/js/bootstrap.bundle.min.js"></script>
<!-- AdminLTE App -->
<script src="/dashboard-web/dist/js/adminlte.min.js"></script>
<!-- AdminLTE for demo purposes -->
<script src="/dashboard-web/dist/js/demo.js"></script>
</body>
</html>