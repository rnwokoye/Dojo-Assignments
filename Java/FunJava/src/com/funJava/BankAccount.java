package com.funJava;

import java.util.Random;

public class BankAccount {
	private String accountNumber;
	private double checkingBalance;
	private double savingsBalance;
	public static int numberOfAccounts = 0; 
	public double totalBankAmount = 0.00;
	
	public BankAccount() {
		String num = randNum();
		this.accountNumber = num;
		numberOfAccounts++; 	
	}
	
	public BankAccount(double checkingBalance, double savingsBalance) {
		String num = randNum();
		this.accountNumber = num;
		this.checkingBalance = checkingBalance; 
		this.savingsBalance = savingsBalance; 
		numberOfAccounts++; 
		totalBankAmount = checkingBalance + savingsBalance;
		System.out.println("checking Balance for account number: " + this.accountNumber + " is: " + this.checkingBalance);
		System.out.println("savings Balance for account number: " + this.accountNumber + " is: " + this.savingsBalance);
			
	}
	
	private String randNum() {
		Random rand = new Random(); 
		int n = 0;
		String y = "";
		for(int i=0; i< 10; i++) {
			n = rand.nextInt(10);
			y+= n;
		}
		System.out.println(y);
		return y;
		}
	public double getCheckingBalance() {
		return checkingBalance;
		
	}
	public double getSavingsBalance() {
		return savingsBalance;	
	}
	
	public double depositMoney(String accountType, double amount) {
		if(accountType == "checking" || accountType == "Checking") {
			this.setCheckingBalance(getCheckingBalance() + amount);
			System.out.println("deposited " + amount + " your checking bal: " + checkingBalance);
		}else {
			this.setSavingsBalance(getSavingsBalance() + amount);
			System.out.println("deposited " + amount + " your savings bal: " + savingsBalance);
		}
		this.totalBankAmount += amount; 
		System.out.println("Total bal: " + this.totalBankAmount);
		return totalBankAmount; 		
	}
	
	public void withdrawMoney(String accountType, double amount) {
		if(accountType == "checking" || accountType == "Checking") {
			if(this.getCheckingBalance() > amount) {
				this.setCheckingBalance(getCheckingBalance() - amount);
				this.totalBankAmount -= amount; 
				System.out.println("You've withdrwan $" + amount + " from checking account");	
			}else {
				System.out.println("you dont have suffcient funds in your checking account!");	
			}
		}else if (accountType == "savings" || accountType == "Savings") {
			if(this.getSavingsBalance() > amount) {
				this.setSavingsBalance(getSavingsBalance() - amount);
				this.totalBankAmount -= amount; 
				System.out.println("You've withdrawn $" + amount + " from your savings account");
			}else {
				System.out.println("you dont have suffcient funds in your savings account!");
			}
		}
		
		System.out.println("your checking bal: " + checkingBalance);
		System.out.println("your savings bal: " + savingsBalance);
		System.out.println("Total bank bal: " + this.totalBankAmount);  
		
	}
	
	private void setSavingsBalance(double d) {
		// TODO Auto-generated method stub
		savingsBalance = d;
		
		
	}

	private void setCheckingBalance(double d) {
		// TODO Auto-generated method stub
		checkingBalance = d;
		
	}

}
	
	
	

