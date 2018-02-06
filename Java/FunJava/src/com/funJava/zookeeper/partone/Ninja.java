package com.funJava.zookeeper.partone;

public class Ninja extends Human {
	
	public Ninja() {
		setStealth(getStealth() +7);
	}
	
	public void steal(Human man) {
		int stole = this.getStealth();
		setHealth(getHealth() + stole);
		man.setHealth(man.getHealth() -stole);
		System.out.println("ninja stole your health by " + stole );
		System.out.println("Ninja's health = " + this.getHealth());
		System.out.println("you lost " + stole + " your health = " + man.getHealth());
	}
	public void runsAway() {
		int run = 10; 
		setHealth(getHealth() -run); 
		System.out.println("ninja escape. Health reduced by "+ run);
	}

}
