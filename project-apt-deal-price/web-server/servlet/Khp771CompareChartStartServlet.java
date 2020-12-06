package com.dashboardweb.servlet;

import java.io.IOException;
import java.net.URLDecoder;
import java.net.URLEncoder;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet(urlPatterns = { "/khp771/compare_chart" })
public class Khp771CompareChartStartServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		
		String region1 = req.getParameter("comregion1");
		String region2 = req.getParameter("comregion2");
		req.setAttribute("region1", region1);
		req.setAttribute("region2", region2);
		
//		System.out.println("xxxxxx" + region1);
//		System.out.println("xxxxxx" + URLDecoder.decode(region1, "utf-8"));
		
//		resp.setContentType("text/plain;charset=utf-8");
//		PrintWriter out = resp.getWriter();
//		out.println(result);
		
		RequestDispatcher dispatcher = req.getRequestDispatcher("/WEB-INF/views/khp-compare-chart-view.jsp");
		dispatcher.forward(req, resp);

	}

}
