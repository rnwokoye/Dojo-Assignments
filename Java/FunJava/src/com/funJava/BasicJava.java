package com.funJava;

import java.util.ArrayList;

public class BasicJava {
	public void printNums(){
		for(int i=1; i < 256; i++){
			System.out.println(i);
		} 
	}
	public void printOddNums(){
		for(int i=1; i < 256; i++){
			if(i % 2 != 0){
				System.out.println(i);
			}
		}
	}
	public void printSum(){
		int sum = 0;
		for(int i=0; i < 256; i++){ 
			sum+= i; 
			System.out.println("New number: " + i + " Sum: " + sum);
		}
	}
	public void printArray(int[] givenArr){
		for(int i=0; i < givenArr.length; i++) {
			System.out.println(givenArr[i]);
		}
	}
	public void printMax(int[] givenArr) {
		int max = givenArr[0];
		for(int i=0; i < givenArr.length; i++) {
			if (givenArr[i] > max) {
				max = givenArr[i]; 	
			} 
		}
		System.out.print(max);
	}
	public void printAve(int[] givenArr) { 
		double sum = 0;
		for(int i=0; i < givenArr.length; i++){
			sum+= givenArr[i]; 
		}
		double ave = sum / givenArr.length; 
		System.out.println(ave);	
	}
	public void oddArray() {
		int[] array = new int[128]; 
		int counter = 0;
	
		for(int i= 0; i < 256; i++) {
//			array[i]= i*2+1; 
			
			if (i % 2 != 0) {
				array[counter] = i;
				counter++;
			}
		}
		System.out.println(array);
		for(int i= 0; i < array.length; i++) {
			System.out.println(array[i]);
		}
	}
	public void greaterThanY(int[] givenArr, int number) {
		int counter = 0; 
		for(int i=0; i < givenArr.length; i++) {
			if(givenArr[i] > number) {
				counter++; 
			}
		}
		System.out.println(counter);
//		System.out.println(givenArr); Ask about this tomorrow. How to print out the Array, rather than the memory location.
	}
	public void squareTheValues(int[] givenArr) {
		ArrayList <Integer> myArray = new ArrayList<>(); 
		for(int i=0; i< givenArr.length; i++) {
			myArray.add(givenArr[i]*givenArr[i]); 
		}System.out.println(myArray);
	}
	public void eliminateNegNums(Integer[] givenArr) {
		ArrayList <Integer> eliminateNegNums = new ArrayList<>(); 
		for(int i=0; i< givenArr.length; i++) {
			if(givenArr[i] < 0) {
				eliminateNegNums.add(0);
			}
			else {
				eliminateNegNums.add(givenArr[i]); 
			}
		}
		System.out.println(eliminateNegNums);
	}
	public void minMaxAvg(Integer [] givenArr) {
		ArrayList<Integer> minMaxAvgArr = new ArrayList<>();
		int min = givenArr[0];
		int max = givenArr[givenArr.length-1];
		int sum = 0; 
		
		for(int i=0; i< givenArr.length; i++) {
			sum+= givenArr[i]; 
			if(givenArr[i] < min) {
				min = givenArr[i];  
			}
			else if (givenArr[i] > max) {
				max = givenArr[i]; 
				}
			}
		minMaxAvgArr.add(min); 
		minMaxAvgArr.add(max);
		minMaxAvgArr.add(sum / givenArr.length); 
		System.out.println(minMaxAvgArr);
		}
	
	public void shiftVal(Integer[] givenArr) {
		for(int i=0; i< givenArr.length; i++) {
			try {
			givenArr[i] = givenArr[i + 1]; 
		}
		
			catch(ArrayIndexOutOfBoundsException s) {
				givenArr[i] =0; 
			}
		}
		System.out.println(java.util.Arrays.toString(givenArr));
	}
}

