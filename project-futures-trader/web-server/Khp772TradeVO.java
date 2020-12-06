package com.dashboardweb.vo;

import lombok.Data;

@Data
public class Khp772TradeVO {
	
	private String chartDate;
	private String chartTime;
	private float chartOpen;
	private float chartHigh;
	private float chartLow;
	private float chartClose;
	private int chartVolume;
	private int contractCount;
	private float contractPoint;
	private int contractPosition;
	private int positionValue;
	private int initBalance;
	private int balance;
	private float profitLoss;
	private int agentAction;
	
}
