package com.funJava;

// This is the lecture of Vehicle Class to demonstrate instance variables with setters and getters
// Note that member variables; instance variables; attributes; fields all refer to the same thing
// You should almost ALWAYS declare instance variables as "private" in java

public class Vehicle {
	    // declare the instance variables numberOfWheels and color
		private int numberOfWheels;
	    private String color;
	    
	 // setter 'set' keyword sets the value for the instance variable NumberOfWheels. Note that I prefer to set before getting
	    
	    public void setNumberOfWheels(int number) {  
	        numberOfWheels = number;
	    }
	    // getter
	    public int getNumberOfWheels() {
	        return numberOfWheels;
	    }
	    
	 // setter
	    public void setColor(String color) {
	        this.color = color;        // 1
	    }
	    // getter
	    public String getColor() {
	        return color;
	    }
	    
}
