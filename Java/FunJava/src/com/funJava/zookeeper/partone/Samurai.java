package com.funJava.zookeeper.partone;

public class Samurai extends Human {
	public static int numberOfSamurai = 0;
	public Samurai() {
		setHealth(getHealth() + 100);
		numberOfSamurai++;
	}
	
	public void deathBlow(Human man) {
		int killer = man.getHealth();
		this.setHealth(this.getHealth() / 2);
		man.setHealth(man.getHealth() - killer);
		System.out.println("death blow. Killed by Samurai your health is " + man.getHealth());
		System.out.println("Samurai health is " + this.getHealth());

	}
	public void meditate() {
		int healing = getHealth()/2; 
		setHealth(getHealth() + healing); 
		System.out.println("samurai Meditate, added " + healing + " to health"); 	
	}
	public void howMany() {
		System.out.println("There are currently " + numberOfSamurai + " samurai here");
		 
	}

}
