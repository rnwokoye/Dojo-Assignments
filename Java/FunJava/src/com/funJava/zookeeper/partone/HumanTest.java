package com.funJava.zookeeper.partone;

public class HumanTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Human person1 = new Human();
		Human person2 = new Human();
		Human person3 = new Human();
		Ninja ninja1 = new Ninja();
		Wizard wizard1 = new Wizard();
		Samurai samurai1 = new Samurai();
		Samurai samurai2 = new Samurai();
		Samurai samurai3 = new Samurai();
		person1.attack(person2);
		wizard1.fireBall(person2);
		wizard1.heal(person2);
		person1.attack(samurai1);
		person1.attack(wizard1);
		person1.getHealth();
		ninja1.steal(person3);
		ninja1.attack(samurai1);
		ninja1.runsAway();
		samurai1.deathBlow(wizard1);
		samurai1.deathBlow(ninja1);
		samurai1.meditate();
		samurai1.howMany();
		samurai3.deathBlow(samurai1);
		samurai1.howMany();
	}

}
