<%@page import="com.dashboardweb.vo.khpBrandAptInfoVO"%>
<%@ page language="java" 
		 contentType="text/html; charset=utf-8"
    	 pageEncoding="utf-8" %>
    	 

  <div class="row">
  <div class="col-12">
    <div class="card">
      <div class="card-header">
        <h3 class="card-title">브랜드 아파트 평당 가격(원)</h3>

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
      <div class="card-body table-responsive p-0" style="height: 300px;">
        <table class="table table-head-fixed text-nowrap">
          <thead>
            <tr>
      		   <th>지역</th>
              <th>브랜드</th>
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
           <% khpBrandAptInfoVO[] pList =
          		(khpBrandAptInfoVO[])request.getAttribute("brand_apt_pyung_price"); %>
          	<% for (khpBrandAptInfoVO p : pList) { %>
            <tr>
              <td><%= p.getRegion()%></td>
              <td><%= p.getBrand()%></td>
              <td><%= p.comma(p.getY2012())%></td>
              <td><%= p.comma(p.getY2013())%></td>
              <td><%= p.comma(p.getY2014())%></td>
              <td><%= p.comma(p.getY2015())%></td>
              <td><%= p.comma(p.getY2016())%></td>
              <td><%= p.comma(p.getY2017())%></td>
              <td><%= p.comma(p.getY2018())%></td>
              <td><%= p.comma(p.getY2019())%></td>
              <td><%= p.comma(p.getY2020())%></td>
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

<div class="row">
   <div class="col-12">
     <div class="card">
       <div class="card-header">
         <h3 class="card-title">브랜드 아파트 매매 건수</h3>

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
       <div class="card-body table-responsive p-0" style="height: 300px;">
         <table class="table table-head-fixed text-nowrap">
           <thead>
             <tr>
       		   <th>지역</th>
               <th>브랜드</th>
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
            <% khpBrandAptInfoVO[] dList =
           		(khpBrandAptInfoVO[])request.getAttribute("brand_apt_deal_count"); %>
           	<% for (khpBrandAptInfoVO d : dList) { %>
             <tr>
               <td><%= d.getRegion()%></td>
               <td><%= d.getBrand()%></td>
               <td><%= d.comma(d.getY2012())%></td>
               <td><%= d.comma(d.getY2013())%></td>
               <td><%= d.comma(d.getY2014())%></td>
               <td><%= d.comma(d.getY2015())%></td>
               <td><%= d.comma(d.getY2016())%></td>
               <td><%= d.comma(d.getY2017())%></td>
               <td><%= d.comma(d.getY2018())%></td>
               <td><%= d.comma(d.getY2019())%></td>
               <td><%= d.comma(d.getY2020())%></td>
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
                