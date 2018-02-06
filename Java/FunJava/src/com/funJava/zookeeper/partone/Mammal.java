package com.funJava.zookeeper.partone;

public class Mammal {
	private int energyLevel;
	public Mammal() {
		this(100); 
	}
	public Mammal(int energyLevel) {
		this.energyLevel = energyLevel; 	
	}
	public void setEnergyLevel(int energyLevel) {
		this.energyLevel = energyLevel;	
	}
	public int getEnergyLevel() {
		return energyLevel; 
	}
	public int displayEnergy() {	
		System.out.println("This energy level is " + energyLevel);
		return energyLevel;	
	}
	
	
	

	
	
	
	
	
	
	
	
	
	
}
