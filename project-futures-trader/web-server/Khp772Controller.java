package com.dashboardweb.controller;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import com.dashboardweb.vo.Khp772TradeVO;
import com.google.gson.Gson;
import com.google.gson.stream.JsonReader;

@Controller
@RequestMapping(path = { "/khp772" })
public class Khp772Controller {
	
	@GetMapping(path = { "/home" })
	public String showKhp772Home() {
		
		return "khp772/khp772-home";
		
	}
	
	
	@GetMapping(path = { "/begin-trade" }, produces = "application/json;charset=utf-8")
    @ResponseBody
    public String beginTrade() {
        URL url = null;        
        HttpURLConnection conn = null;
        
        String result = "";
        try {
            
            String path = String.format("http://127.0.0.1:5000/khp772/begin-trade");
                
            url = new URL(path);
            conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("GET");
            
            int status = conn.getResponseCode();
            if (status == 200) {
                // 네트워크를 통해 수신된 데이터를 읽는 도구 ( IO 객체 )
                InputStream is = conn.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                
                JsonReader reader = new JsonReader(isr);
                Gson gson = new Gson();
                
                Khp772TradeVO trade = gson.fromJson(reader, Khp772TradeVO.class);
                result = gson.toJson(trade);
                
            } else {
                result = String.format("%s 오류가 발생했습니다.", status);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
            try { conn.disconnect(); } catch (Exception ex2) {}
            result = "알 수 없는 오류가 발생했습니다.";
        }
        
        return result;  
	}
	
	
	@GetMapping(path = { "/next-trade" }, produces = "application/json;charset=utf-8")
    @ResponseBody
    public String nextTrade() {
        URL url = null;        
        HttpURLConnection conn = null;
        
        String result = "";
        try {
            
            String path = String.format("http://127.0.0.1:5000/khp772/next-trade");
                
            url = new URL(path);        
            conn = (HttpURLConnection)url.openConnection();
            conn.setRequestMethod("GET");
            
            int status = conn.getResponseCode();
            if (status == 200) {
                // 네트워크를 통해 수신된 데이터를 읽는 도구 ( IO 객체 )
                InputStream is = conn.getInputStream();
                InputStreamReader isr = new InputStreamReader(is);
                
                JsonReader reader = new JsonReader(isr);
                Gson gson = new Gson();
                
                Khp772TradeVO trade = gson.fromJson(reader, Khp772TradeVO.class);
                result = gson.toJson(trade);
                
            } else {
                result = String.format("%s 오류가 발생했습니다.", status);
            }
        } catch (Exception ex) {
            ex.printStackTrace();
            try { conn.disconnect(); } catch (Exception ex2) {}
            result = "알 수 없는 오류가 발생했습니다.";
        }
        
        return result;  
    }
	
}
