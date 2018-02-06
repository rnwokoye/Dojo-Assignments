package com.funJava;

public class HelloWorldTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		HelloWorld hW = new HelloWorld();
		String greeting = hW.greet();
		String greetingWithName = hW.greet("Richard");
		if(greeting.equals("Hello World") || greetingWithName.equals("Hello Richard")) {
			System.out.println("Test successful");
		}else {
			System.out.println("Test fail");
		}
		
		 
	}
}
