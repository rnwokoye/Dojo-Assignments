package com.funJava.advancedOOP;

public class BicycleTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Bicycle b = new Bicycle(); 
		System.out.println(Bicycle.myConstant);
		b.sayHello();
		Bicycle.staticMethod();
		b.speedUp(3);
		b.applyBrakes(2);
		System.out.println(b.getSpeed());

	}

}
