package com.funJava.zookeeper.partone;

public class Gorilla extends Mammal{
	public Gorilla() {
		
	}
	public int throwsObjects() {
		System.out.println("The gorilla threw an object");
		setEnergyLevel(getEnergyLevel() - 5);
		return getEnergyLevel();	
	}	
	public int eatBananas() {
		System.out.println("hmmmm...yummy bananas");
		setEnergyLevel(getEnergyLevel() +10);
		return getEnergyLevel();	
	}
	public int climb() {
		System.out.println("The gorilla is up a tree now");
		setEnergyLevel(getEnergyLevel() -10);
		return getEnergyLevel();
	}

}

