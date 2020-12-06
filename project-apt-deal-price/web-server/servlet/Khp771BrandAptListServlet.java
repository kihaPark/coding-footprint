package com.dashboardweb.servlet;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.dashboardweb.vo.khpBrandAptInfoVO;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

@WebServlet(urlPatterns = { "/khp771/brand_apt_list" })
public class Khp771BrandAptListServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		String region = req.getParameter("region");
		String err_result = "";
		
		{	
			String path = "http://127.0.0.1:5000/khp771/brand_apt_pyung_price?region=" + region; 
			
			URL url = new URL(path);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			int status = conn.getResponseCode();
			if (status == 200) {
				InputStream is = conn.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				
				JsonReader reader = new JsonReader(isr);
				Gson gson = new Gson();
				
				khpBrandAptInfoVO[] baiList = gson.fromJson(reader, khpBrandAptInfoVO[].class);
				req.setAttribute("brand_apt_pyung_price", baiList);
				
			} else {
				err_result = String.format("%d 오류가 발생했습니다.", status);
			}

			conn.disconnect();
		}
		
		{
			String path = "http://127.0.0.1:5000/khp771/brand_apt_deal_count?region=" + region; 
			
			URL url = new URL(path);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			int status = conn.getResponseCode();
			if (status == 200) {
				InputStream is = conn.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				
				JsonReader reader = new JsonReader(isr);
				Gson gson = new Gson();
				
				khpBrandAptInfoVO[] baiList = gson.fromJson(reader, khpBrandAptInfoVO[].class);
				req.setAttribute("brand_apt_deal_count", baiList);
				
			} else {
				err_result = String.format("%d 오류가 발생했습니다.", status);
			}

			conn.disconnect();
		}
		
//		resp.setContentType("text/plain;charset=utf-8");
//		PrintWriter out = resp.getWriter();
//		out.println(err_result);
		
		RequestDispatcher rd = req.getRequestDispatcher("/WEB-INF/views/khp-brand-apt-list.jsp");
		rd.forward(req, resp);
	}
}
