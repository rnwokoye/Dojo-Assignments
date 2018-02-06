package com.funJava.zookeeper.partone;

public class Dragon extends Mammal {
	public Dragon() {
		setEnergyLevel(getEnergyLevel() +200); 
	}
	public void fly() {
		setEnergyLevel(getEnergyLevel() -50);
		System.out.println("Swoooosh the dragon is airbound ");
	}
	public void eatsHumans() {
		setEnergyLevel(getEnergyLevel() +25);
		System.out.println("So...well never mind ");
		
	}
	public void attackTown() {
		setEnergyLevel(getEnergyLevel() -100);
		System.out.println("The town is on fire...run!! ");
	}

}
