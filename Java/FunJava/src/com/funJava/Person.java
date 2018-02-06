package com.funJava;

public class Person {
	private int age;
    private String name;
    private int cmHeight;
    public Person() {
    	this(20, "John Doe", 171); // use the constructor overload to create a "default" person name John Doe, 20 yrs, and 171 height
    	//in this case, the default MUST be the first statement in our constructor. 
    }
    public Person(int age, String name, int cmHeight) {
    	this.age = age;
    	this.name = name;
    	this.cmHeight = cmHeight;
    	System.out.println(this.name);
    	
    }
    public Person(int ageParam, String nameParam) {
        age = ageParam;
        name = nameParam;
    }
    public void objectMethods(Person anotherObject) {
        System.out.println("Class name: " + this.getClass().getSimpleName());
        System.out.println("toString: " + this.toString());
        System.out.println("Equals: " + this.equals(anotherObject));
    }

}
