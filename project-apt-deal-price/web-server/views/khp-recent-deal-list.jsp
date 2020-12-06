<%@page import="com.dashboardweb.vo.khpRecentDealVO"%>
<%@ page language="java" 
		 contentType="text/html; charset=utf-8"
    	 pageEncoding="utf-8" %>
    	 

<div class="row">
  <div class="col-12">
    <div class="card">
      <div class="card-header">
        <h3 class="card-title">최근 거래 세부정보</h3>

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
      <div class="card-body table-responsive p-0" style="height: 550px;">
        <table class="table table-head-fixed text-nowrap">
          <thead>
            <tr>
              <th>주소</th>
              <th>아파트명</th>
              <th>완공년도</th>
              <th>평</th>
              <th>층수</th>
              <th>거래가격(원)</th>
              <th>거래일</th>
            </tr>
          </thead>
          <tbody>
           <% khpRecentDealVO[] rdList =
          		(khpRecentDealVO[])request.getAttribute("recent_deal_list"); %>
          	<% for (khpRecentDealVO rd : rdList) { %>
            <tr>
              <td><%= rd.getAddress()%></td>
              <td><%= rd.getAptName()%></td>
              <td><%= rd.getCompleteYear()%></td>
              <td><%= rd.getPyung()%></td>
              <td><%= rd.getAptFloor()%></td>
              <td><%= rd.comma(rd.getContractPrice())%></td>
              <td><%= rd.getContractDate()%></td>
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
        
                