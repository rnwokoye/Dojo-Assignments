package com.funJava;

public class Human extends Mammal {
	public void goToWork() {
		System.out.println("I'm going to work, something only humans can do.");
	}
/*	Override/extend a method of superclass by writing same method signature and return type. 
	Execute this method now for the child human class, since humans behave differently while sleeping!
	Note that this method is visible because it is public. 
*/
	public void regulateTemperature() {
			System.out.println("My temperature is just right for humans now. ");
		}
	//Override/extend a method of superclass by writing same method signature and return type
	public void startSleeping() {
		System.out.println("I toss and turn a lot");
		
	// To extend the startSleeping() parent (or super) class method, we use the super keyword:
		super.startSleeping();
		
		
//		// we use the super keyword to invoke the private superclass "start sleeping" method in the Human class. 
//		super.startSleeping();
	}

}
