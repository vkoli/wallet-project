#!/usr/bin/python
import sys
import connect

MAIN_MENU = 'MAIN MENU\n[1] Account\n[2] Send Money\n[3] Request Money\n[4] Statements\n[5] Search Transactions\n[6] Sign out\n'
ACCOUNT_MENU = 'ACCOUNT FUNCTIONS MENU\n[1] Account Info\n[2] Modify Name\n[3] Add Email Address\n[4] Remove Email Address\n[5] Add Phone Number\n[6] Remove Phone Number\n[7] Add Bank Account\n[8] Remove Bank Account\n'
STATEMENT_MENU = 'STATEMENT FUNCTIONS MENU\n[1] Get statement by dates\n[2] Get statement by month\n[3] Get highest amount of transactions per month\n[4] Get best users\n'
STATEMENT_SEARCH_MENU = 'STATEMENT SEARCH MENU\n[1] User SSN\n[2] User Email\n[3] User Phone\n[4] Transaction Type\n'

def main():
	# connect.connect()
	print('Welcome to WALLET!\nWould you like to sign in or sign up?')
	while True:
		cred_step = int(input("Enter 1 to sign in or 2 to sign up: "))
		if cred_step == 1:
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))

			#TODO replaced with sql query to check for user in db
			print(f'\nUser {user_ssn} with phone {user_phone} has signed in\n')
			
			while(True):
				print(MAIN_MENU)
				main_choice = int(input("Enter option from main menu: "))

				if main_choice == 1:
					print(ACCOUNT_MENU)

				elif main_choice == 2:
					send_user_elec_id = input("Enter the sender's email address or phone number: ")
					send_amount = float(input("Enter a valid amount to send: "))
					send_memo = input("Enter reason for sending money: ")
					
					#TODO replaced with sql query to add send transaction in db
					print(f'Sending ${send_amount} to {send_user_elec_id} for {send_memo}\n')

				elif main_choice == 3:
					request_user_elec_ids = input("Enter the user's email addresses or phone numbers separated by commas ',': ")
					request_amount = float(input("Enter a valid amount to send: "))
					request_memo = input("Enter reason for requesting money: ")

					#TODO replaced with sql query to add request transaction in db
					print(f'Sending ${request_amount} to {request_user_elec_ids} for {request_memo}\n')

				elif main_choice == 4:
					print(STATEMENT_MENU)

				elif main_choice == 5:
					print(STATEMENT_SEARCH_MENU)
				
				elif main_choice == 6:
					break

		elif cred_step == 2:
			user_name = input("Enter your first and last name: ")
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))
			user_email = input("Enter your email address: ")

			#TODO replaced with sql query to add user in db
			print(f'\nUser {user_name} identified by {user_ssn} with phone {user_phone} and email {user_email} has signed up. Please sign in to access account.\n') 

if __name__ == '__main__':
    main()
