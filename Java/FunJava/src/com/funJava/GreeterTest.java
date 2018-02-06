package com.funJava;

public class GreeterTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Greeter g = new Greeter(); 
		
		String greeting = g.greet(); 
		String greetingWithFirstName = g.greet("Michael");
		String greetingWithBothNames = g.greet("Richard", "Nwokoye");
		System.out.println(greetingWithBothNames);
		System.out.println(greetingWithFirstName);
		System.out.println(greeting);
		
//		if (greeting.equals("Hello World") || greetingWithName.equals ("Hello Eduardo")) {
//			System.out.println("Test successful");
//		}
//		else {
//			System.out.println("Test Fail");
//		}
	}

}
