package com.dashboardweb.servlet;

import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.dashboardweb.vo.khpDealCountVO;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

@WebServlet(urlPatterns = { "/khp771/compare_price_chart_data" })
public class Khp771ComparePriceChartDataServlet extends HttpServlet {
	
	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {

		String type = req.getParameter("type");
		String region1 = req.getParameter("region1");
		String region2 = req.getParameter("region2");
//		System.out.println(type + ":" + region1 + ":" + region2);
//		String region1 = URLDecoder.decode(req.getParameter("region1"), "UTF-8");
//		String region2 = URLDecoder.decode(req.getParameter("region2"), "UTF-8");
		
		String path = String.format(
				"%s?region1=%s&region2=%s",
				"http://127.0.0.1:5000/khp771/chart_pyung_price",
				URLEncoder.encode(region1, "utf-8"), URLEncoder.encode(region2, "utf-8")); 
		
		URL url = new URL(path);
		HttpURLConnection conn = (HttpURLConnection) url.openConnection();
		conn.setRequestMethod("GET");

		int status = conn.getResponseCode();
		
		if (status != 200) {
			String result = String.format("%d 오류가 발생했습니다.", status);
			conn.disconnect();
		
			PrintWriter out = resp.getWriter();
			out.println(result);
			return;
		}
		
		InputStream is = conn.getInputStream();
		InputStreamReader isr = new InputStreamReader(is);
		
		JsonReader reader = new JsonReader(isr);
		Gson gson = new Gson();
		
		khpDealCountVO[] compares = gson.fromJson(reader, khpDealCountVO[].class);
				
		String json = null;
		if (type.equals("area")) {
			AreaChartData areaChartData =
					loadAreaChartData(
							compares[0].getRegion(), compares[1].getRegion(),
							compares[0].getYearValues(), compares[1].getYearValues());
			json = gson.toJson(areaChartData);
		}
		
		conn.disconnect();

		resp.setContentType("text/plain;charset=utf-8");
		PrintWriter out = resp.getWriter();
		out.println(json);
	}	
	
	class AreaChartData {
		String[] labels;
		ArrayList<String> regions = new ArrayList<>();
		ArrayList<Object[]> datasets = new ArrayList<>();
		
		public AreaChartData() {}
		
		public AreaChartData(String[] labels, ArrayList<String> regions, ArrayList<Object[]> datasets) {
			this.labels = labels;
			this.regions = regions;
			this.datasets = datasets;
		}
		
		public String[] getLabels() {
			return labels;
		}
		public void setLabels(String[] labels) {
			this.labels = labels;
		}
		public void append(String region) {
			regions.add(region);
		}
		public List<Object[]> getDatasets() {
			return datasets;
		}
		public void setDatasets(ArrayList<Object[]> datasets) {
			this.datasets = datasets;
		}
		public void append(Object[] data) {
			datasets.add(data);
		}
	}
	
	private AreaChartData loadAreaChartData(
			String region1, String region2, Integer[] values1, Integer[] values2) {
		
		AreaChartData areaChartData = new AreaChartData();
		areaChartData.setLabels(new String[] {"y2012", "y2013", "y2014", "y2015", "y2016", "y2017", "y2018", "y2019", "y2020"});
		areaChartData.append( region1 );
		areaChartData.append( region2 );
		areaChartData.append( values1 );
		areaChartData.append( values2 );
		
		return areaChartData;
		
	}

}
