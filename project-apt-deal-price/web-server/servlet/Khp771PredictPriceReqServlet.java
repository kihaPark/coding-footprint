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

import com.dashboardweb.vo.khpPredictPriceVO;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

@WebServlet(urlPatterns = { "/khp771/predict_price_req" })
public class Khp771PredictPriceReqServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		{
			String path = String.format(
					"%s?region=%s&region_sub=%s&pyung=%s",
					"http://127.0.0.1:5000/khp771/predict_price",
					req.getParameter("region"),
					req.getParameter("region_sub"),
					req.getParameter("pyung")); 
				
			URL url = new URL(path);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			int status = conn.getResponseCode();
			if (status == 200) {
				InputStream is = conn.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				
				JsonReader reader = new JsonReader(isr);
				Gson gson = new Gson();
				
				khpPredictPriceVO predict = gson.fromJson(reader, khpPredictPriceVO.class);
				req.setAttribute("predict_price", predict);
				
			} else {
				String err_result = String.format("%d 오류가 발생했습니다.", status);
			}

			conn.disconnect();
		}
		
		{
			String path = String.format(
					"%s?region=%s&pyung=%s",
					"http://127.0.0.1:5000/khp771/predict_price_all",
					req.getParameter("region"),
					req.getParameter("pyung")); 
				
			URL url = new URL(path);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			int status = conn.getResponseCode();
			if (status == 200) {
				InputStream is = conn.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				
				JsonReader reader = new JsonReader(isr);
				Gson gson = new Gson();
				
				khpPredictPriceVO[] ppList = gson.fromJson(reader, khpPredictPriceVO[].class);
				req.setAttribute("predict_price_list", ppList);

			} else {
				String err_result = String.format("%d 오류가 발생했습니다.", status);
			}

			conn.disconnect();
		}
		
		
		RequestDispatcher rd = req.getRequestDispatcher("/WEB-INF/views/khp-predict-price-result.jsp");
		rd.forward(req, resp);
	}
}
