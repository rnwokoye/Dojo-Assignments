package com.funJava;

public class PuzzleJava {
	public void printSumArray(int[] givenArr){
		int sum = 0; 
		for(int i=0; i < givenArr.length; i++) {
			sum+= givenArr[i]; 
			if(givenArr[i] > 10) {
				System.out.println(givenArr[i]);
			}
		}
		System.out.println(sum);
	}
	public void shuffleArr(String[] givenArr) {
		shuffleArray(givenArr); 
		
		
		
		
		
		for (int i=0; i < givenArr.length; i++) {
			System.out.print(givenArr[i] + " ");
		}
		System.out.println();
	}
	
	
	
	
	
	private void shuffleArray(String[] givenArr) {
		
		
	}

}
