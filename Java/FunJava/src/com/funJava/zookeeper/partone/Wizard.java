package com.funJava.zookeeper.partone;

public class Wizard extends Human {
	public Wizard() {
		setHealth(getHealth() -50);
		setIntelligence(getIntelligence() +5);	
	}
	public void heal(Human man) {
		int healing = this.getIntelligence();
		man.setHealth(man.getHealth() + healing);
		System.out.println("healed by a Wizard. Added " + healing + " to your health");
	}
	public void fireBall(Human man) {
		int fireAttack = this.getIntelligence()*3;
		man.setHealth(man.getHealth() -fireAttack);
		System.out.println("Wizard fury, health is reduced by " + fireAttack + " remaining health = " + man.getHealth());
	}

}


