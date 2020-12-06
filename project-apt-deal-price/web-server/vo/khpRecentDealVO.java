package com.dashboardweb.vo;

public class khpRecentDealVO {

//	 ['region', 'region_sub', 'apt_name', 'completion_year',
//	  'apt_size', 'apt_floor','contract_price', 'contract_date',]
	
	private String address;
	private String aptName;
	private int completeYear;
	private float pyung;
	private int aptFloor;
	private int contractPrice;
	private String contractDate;
	
	public String getAddress() {
		return address;
	}
	public void setAddress(String address) {
		this.address = address;
	}
	public String getAptName() {
		return aptName;
	}
	public void setAptName(String aptName) {
		this.aptName = aptName;
	}
	public int getCompleteYear() {
		return completeYear;
	}
	public void setCompleteYear(int completeYear) {
		this.completeYear = completeYear;
	}
	public float getPyung() {
		return pyung;
	}
	public void setPyung(float pyung) {
		this.pyung = pyung;
	}
	public int getAptFloor() {
		return aptFloor;
	}
	public void setAptFloor(int aptFloor) {
		this.aptFloor = aptFloor;
	}
	public int getContractPrice() {
		return contractPrice;
	}
	public void setContractPrice(int contractPrice) {
		this.contractPrice = contractPrice;
	}
	public String getContractDate() {
		return contractDate;
	}
	public void setContractDate(String contractDate) {
		this.contractDate = contractDate;
	}
	public String comma(int num) {
		return String.format("%,d", num);
	}

}
