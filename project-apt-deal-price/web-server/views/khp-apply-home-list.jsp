<%@page import="com.dashboardweb.vo.khpApplyHomeVO"%>
<%@ page language="java" 
		 contentType="text/html; charset=utf-8"
    	 pageEncoding="utf-8" %>
    	 

   <div class="row">
   <div class="col-12">
     <div class="card">
       <div class="card-header">
         <h3 class="card-title">분양 아파트 예측 가격</h3>

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
               <th>공급위치</th>
               <th>건설사</th>
               <th>아파트명</th>
               <th>전용면적(m²)</th>
               <th>평</th>
               <th>분양가격(원)</th>
               <th>예측가격(원)</th>
               <th>분양-예측(원)</th>
               <th>분양/예측%</th>
             </tr>
           </thead>
           <tbody>
            <% khpApplyHomeVO[] ahList =
           		(khpApplyHomeVO[])request.getAttribute("apply_home_list"); %>
           	<% for (khpApplyHomeVO ah : ahList) { %>
             <tr>
               <td><%= ah.getRegion()%></td>
               <td><%= ah.getConstFirm()%></td>
               <td><%= ah.getAptName()%></td>
               <td><%= ah.getArea()%></td>
               <td><%= ah.getPyung()%></td>
               <td><%= ah.comma(ah.getApplyPrice())%></td>
               <td><%= ah.comma(ah.getPredPrice())%></td>
               <td><%= ah.comma(ah.getDelta())%></td>
               <td><%= ah.getPercent()%></td>
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
        
                