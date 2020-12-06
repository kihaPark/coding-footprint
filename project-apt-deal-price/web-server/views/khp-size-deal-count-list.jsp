<%@page import="com.dashboardweb.vo.khpSizeDealCountVO"%>
<%@ page language="java" 
		 contentType="text/html; charset=utf-8"
    	 pageEncoding="utf-8" %>
    	 

   <div class="row">
   <div class="col-12">
     <div class="card">
       <div class="card-header">
         <h3 class="card-title">크기별 아파트 매매 건수</h3>

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
       <div class="card-body table-responsive p-0" style="height: 350px;">
         <table class="table table-head-fixed text-nowrap">
           <thead>
             <tr>
               <th>지역</th>
               <th>크기(m²)</th>
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
            <% khpSizeDealCountVO[] sdcList =
           		(khpSizeDealCountVO[])request.getAttribute("size_deal_count"); %>
           	<% for (khpSizeDealCountVO sdc : sdcList) { %>
             <tr>
               <td><%= sdc.getRegion()%></td>
               <td><%= sdc.getApt_Size()%></td>
               <td><%= sdc.comma(sdc.getY2012())%></td>
               <td><%= sdc.comma(sdc.getY2013())%></td>
               <td><%= sdc.comma(sdc.getY2014())%></td>
               <td><%= sdc.comma(sdc.getY2015())%></td>
               <td><%= sdc.comma(sdc.getY2016())%></td>
               <td><%= sdc.comma(sdc.getY2017())%></td>
               <td><%= sdc.comma(sdc.getY2018())%></td>
               <td><%= sdc.comma(sdc.getY2019())%></td>
               <td><%= sdc.comma(sdc.getY2020())%></td>
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
        
                