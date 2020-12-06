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

import com.dashboardweb.vo.khpSizeDealCountVO;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

@WebServlet(urlPatterns = { "/khp771/size_pyung_price" })
public class Khp771SizePyungPriceServlet extends HttpServlet {

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		{
			String region = req.getParameter("region");
			
			String path = "http://127.0.0.1:5000/khp771/size_pyung_price?region=" + region; 
			
			// 자바 프로그램에서 다른 서버에 요청을 보내고 응답을 수신하는 도구
			URL url = new URL(path);
			HttpURLConnection conn = (HttpURLConnection) url.openConnection();
			conn.setRequestMethod("GET");

			String result = "";

			int status = conn.getResponseCode();
			if (status == 200) {
				// 네트워크를 통해 수신된 데이터를 읽는 도구(IO 객체)
				InputStream is = conn.getInputStream();
				InputStreamReader isr = new InputStreamReader(is);
				
				JsonReader reader = new JsonReader(isr);
				Gson gson = new Gson();
				
				khpSizeDealCountVO[] sdcList = gson.fromJson(reader, khpSizeDealCountVO[].class);
				// System.out.println("sl : " + irisList[0].getSepalLength());
				// JSP에서 사용할 수 있도록 request에 데이터 저장
				req.setAttribute("size_pyung_price", sdcList);
				
			} else {
				result = String.format("%d 오류가 발생했습니다.", status);
			}

			conn.disconnect();
		}
				
		// 브라우저에게 응답
		RequestDispatcher rd = req.getRequestDispatcher("/WEB-INF/views/khp-size-pyung-price-list.jsp");
		rd.forward(req, resp);
		
	}

}
