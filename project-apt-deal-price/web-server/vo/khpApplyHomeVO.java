package com.dashboardweb.vo;

public class khpApplyHomeVO {

//	"공급위치": "서울특별시 양천구 신월2동 489-1",
//	"건설사": " (주)동양건설산업",
//	"아파트명": " 신목동 파라곤",
//	"전용면적": 74.64,
//	"평": 22.62,
//	"분양가격": 663300000,
//	"예측가격": 469717420,
//	"분양-예측": 193582580,
//	"분양/예측%": 141
	
	private String region;
	private String constFirm;
	private String aptName;
	private float area;
	private float pyung;
	private int applyPrice;
	private int predPrice;
	private int delta;
	private int percent;
	
	public String getRegion() {
		return region;
	}
	public void setRegion(String region) {
		this.region = region;
	}
	public String getConstFirm() {
		return constFirm;
	}
	public void setConstFirm(String constFirm) {
		this.constFirm = constFirm;
	}
	public String getAptName() {
		return aptName;
	}
	public void setAptName(String aptName) {
		this.aptName = aptName;
	}
	public float getArea() {
		return area;
	}
	public void setArea(float area) {
		this.area = area;
	}
	public float getPyung() {
		return pyung;
	}
	public void setPyung(float pyung) {
		this.pyung = pyung;
	}
	public int getApplyPrice() {
		return applyPrice;
	}
	public void setApplyPrice(int applyPrice) {
		this.applyPrice = applyPrice;
	}
	public int getPredPrice() {
		return predPrice;
	}
	public void setPredPrice(int predPrice) {
		this.predPrice = predPrice;
	}
	public int getDelta() {
		return delta;
	}
	public void setDelta(int delta) {
		this.delta = delta;
	}
	public int getPercent() {
		return percent;
	}
	public void setPercent(int percent) {
		this.percent = percent;
	}
	public String comma(int num) {
		return String.format("%,d", num);
	}
}
