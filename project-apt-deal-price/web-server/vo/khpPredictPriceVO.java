package com.dashboardweb.vo;

public class khpPredictPriceVO {

	private String region;
	private String regionSub;
	private float pyung;
	private int price;
	
	public String getRegion() {
		return region;
	}
	public void setRegion(String region) {
		this.region = region;
	}
	public String getRegionSub() {
		return regionSub;
	}
	public void setRegionSub(String regionSub) {
		this.regionSub = regionSub;
	}
	public float getPyung() {
		return pyung;
	}
	public void setPyung(float pyung) {
		this.pyung = pyung;
	}
	public int getPrice() {
		return price;
	}
	public void setPrice(int price) {
		this.price = price;
	}
	public String comma(int num) {
		return String.format("%,d", num);
	}
	public int totalPrice() {
		return (int)Math.round(price * pyung);
	}	
}
