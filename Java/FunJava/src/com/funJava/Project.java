package com.funJava;

public class Project {
	private String name; 
	private String description; 
	
	public Project() {
		
	}
	public Project(String name) {
		this.name = name; 
		
	}
	
	public Project(String name, String description) {
		this.name = name; 
		this.description = description; 	
	}
	
	public void setName(String name) {
		this.name = name; 
	}
	public String getName() {
		return name; 
	}
	
	public void setDescription(String description) {
		this.description = description;
	}
	
	public String getDescription() {
		return description;
	}
	
	public String elevatorPitch() {
		return this.name + ": " + this.description; 
	}
	

}
