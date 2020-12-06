<%@page import="com.dashboardweb.vo.khpPredictPriceVO"%>
<%@ page language="java" 
		 contentType="text/html; charset=utf-8"
    	 pageEncoding="utf-8" %>
    	 

           	
   <div class="row">
   <div class="col-12">
     <div class="card">
       <div class="card-header">
         <h3 class="card-title">가격 예측 결과</h3>
         
        </div>
       <!-- /.card-header -->
       <div class="card-body table-responsive p-0" style="height: 150px; text-align:center">
       <br>
        <% khpPredictPriceVO pred =
           		(khpPredictPriceVO)request.getAttribute("predict_price"); %>
    	<h4>
    	거래가 가장 많은 지역구는 <%= pred.getRegionSub()%> 입니다.
    	</h4>
    	<br>
    	<h3>
    	<%= pred.getRegion()%> <%= pred.getRegionSub()%> <%= pred.getPyung()%> 평 아파트 : <%= pred.comma(pred.totalPrice())%>원 ( 평당 <%= pred.comma(pred.getPrice())%>원 )
    	</h3>
       </div>
       <!-- /.card-body -->
     </div>
     <!-- /.card -->
   </div>
 </div>
        
 <div class="row">
   <div class="col-12">
     <div class="card">
       <div class="card-header">
         <h3 class="card-title">지역구 예측 가격</h3>

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
               <th>지역구</th>
               <th>평</th>
               <th>예측가격(원)</th>
               <th>평당 예측가격(원)</th>
             </tr>
           </thead>
           <tbody>
            <% khpPredictPriceVO[] ppList =
           		(khpPredictPriceVO[])request.getAttribute("predict_price_list"); %>
           	<% for (khpPredictPriceVO pp : ppList) { %>
             <tr>
               <td><%= pp.getRegion()%></td>
               <td><%= pp.getRegionSub()%></td>
               <td><%= pp.getPyung()%></td>
               <td><%= pp.comma(pp.totalPrice())%></td>
               <td><%= pp.comma(pp.getPrice())%></td>
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
            