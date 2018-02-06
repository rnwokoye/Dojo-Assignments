package com.funJava.zookeeper.partone;

public class Human {
	private int strength;
	private int intelligence;
	private int stealth; 
	private int health;
	public Human() {
		this(3,3,3,100);
	}
	
	public Human(int strength, int intelligence, int stealth, int health) {
		this.strength = strength;
		this.intelligence = intelligence;
		this.stealth = stealth;
		this.health = health;	
	}


	public int getStrength() {
		return strength;
	}
	public void setStrength(int strength) {
		this.strength = strength;
	}
	public int getIntelligence() {
		return intelligence;
	}
	public void setIntelligence(int intelligence) {
		this.intelligence = intelligence;
	}
	public int getStealth() {
		return stealth;
	}
	public void setStealth(int stealth) {
		this.stealth = stealth;
	}
	public int getHealth() {
		return health;
	}
	public void setHealth(int health) {
		this.health = health;
	}
	
	public void attack(Human man) {
		int damage = this.getStrength();
		man.setHealth(man.getHealth() - damage);
		System.out.println("Attacked by a human. you have " + man.getHealth() + " Health");
	}
	
	

}
