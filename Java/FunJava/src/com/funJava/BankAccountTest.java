package com.funJava;

public class BankAccountTest {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		BankAccount account1 = new BankAccount(50.00, 40.00);
		BankAccount account2 = new BankAccount(200.0, 100.50);
		BankAccount account3 = new BankAccount();
		account1.depositMoney("checking", 250);
		account1.depositMoney("savings", 100);
		account1.withdrawMoney("checking", 50);
		account1.withdrawMoney("savings", 100);
		account1.withdrawMoney("Savings",  400);
		account1.withdrawMoney("Checking",  400);
		System.out.println("The total number of accounts is " + BankAccount.numberOfAccounts);

	}

}
