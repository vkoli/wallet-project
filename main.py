#!/usr/bin/python
import sys
import connect

def main():
	connect.connect()
	print('Welcome to WALLET!\nWould you like to sign in or sign up?')
	while True:
		cred_step = int(input("Enter 1 to sign in or 2 to sign up: "))
		if cred_step == 1:
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))

			#TODO replaced with sql query to check for user in db
			print(f'\nUser {user_ssn} with phone {user_phone} has signed in') 
		elif cred_step == 2:
			user_name = input("Enter your first and last name: ")
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))
			user_email = input("Enter your email address: ")

			#TODO replaced with sql query to check for user in db
			print(f'\nUser {user_name} identified by {user_ssn} with phone {user_phone} and email {user_email} has signed up. Please sign in to access account.') 

if __name__ == '__main__':
    main()
