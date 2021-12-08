#!/usr/bin/python
import sys
import connect
import queries

MAIN_MENU = 'MAIN MENU\n[1] Account\n[2] Send Money\n[3] Request Money\n[4] Statements\n[5] Search Transactions\n[6] Sign out\n'
ACCOUNT_MENU = 'ACCOUNT FUNCTIONS MENU\n[1] Account Info\n[2] Modify Name\n[3] Add Email Address\n[4] Remove Email Address\n[5] Add Phone Number\n[6] Remove Phone Number\n[7] Add Bank Account\n[8] Remove Bank Account\n[9] Go Back to Main Menu\n'
STATEMENT_MENU = 'STATEMENT FUNCTIONS MENU\n[1] Get statement by dates\n[2] Get statement by month\n[3] Get highest amount of transactions per month\n[4] Get best users\n[5] Go Back to Main Menu\n'
STATEMENT_SEARCH_MENU = 'STATEMENT SEARCH MENU\n[1] User Email\n[2] User Phone\n[3] Transaction Type\n[4] Go Back to Main Menu\n'

def main():
	# connect.connect()
	print('Welcome to WALLET!\nWould you like to sign in or sign up?')
	while True:
		cred_step = int(input("Enter 1 to sign in or 2 to sign up: "))
		if cred_step == 1:
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))
			queries.user_sign_in(user_ssn, user_phone)
			
			while(True):
				print(MAIN_MENU)
				main_choice = int(input("Enter option from main menu: "))

				if main_choice == 1:
					while(True):
						print(ACCOUNT_MENU)
						account_choice = int(input("Enter choice from account menu: "))
						if account_choice == 1:
							#TODO replaced with sql query to give user account summary, list phone no & email
							print('Selected Account Info')
						elif account_choice == 2:
							name = input("Enter new name: ")
							
							#TODO replaced with sql query to edit user name
							print('2')
						elif account_choice == 3:
							email = input("Enter new email to add: ")
							
							#TODO replaced with sql query to add email to user
							print('3')
						elif account_choice == 4:
							email = input("Enter email to remove: ")
							
							#TODO replaced with sql query to remove email from user
							print('4')	
						elif account_choice == 5:
							phone = input("Enter new phone number to add: ")
							
							#TODO replaced with sql query to add phone number to user
							print('5')
						elif account_choice == 6:
							phone = input("Enter phone number to remove: ")
							
							#TODO replaced with sql query to remove phone number from user
							print('6')							
						elif account_choice == 7:
							ba = input("Enter new bank account to link: ")
							
							#TODO replaced with sql query to add bank account to user
							print('7')
						elif account_choice == 8:
							ba = input("Enter bank account to remove: ")
							
							#TODO replaced with sql query to remove bacnk account 
							print('8')
						else:
							break
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
					while(True):
						print(STATEMENT_MENU)
						statement_choice = int(input("Enter choice from account menu: "))
						if statement_choice == 1:
							user_name = input("Enter user's full name: ")
							start = input("Enter start date in MM-DD-YYYY: ")
							end = input("Enter end date in MM-DD-YYYY: ")

							#TODO replaced with sql query to give total amount of money sent/recieved by a user in a range of dates
							print('1')

						elif statement_choice == 2:
							user_name = input("Enter user's full name: ")
							month = input("Enter the month as a two-digit number (e.g. January = 01): ")
							
							#TODO replaced with sql query to give total/average amount og money sent/recived by a user in a month
							print('2')

						elif statement_choice == 3:
							#TODO replaced with sql query to get the maximum amount of transactions per month
							print('3')
						elif statement_choice == 4:
							#TODO replaced with sql query to get users who have sent/recieved the maximum total amount of money
							print('4')
						else:
							break							
				elif main_choice == 5:
					while(True):
						print(STATEMENT_SEARCH_MENU)
						statement_search_choice = int(input("Enter choice from statement search menu: "))
						if statement_search_choice == 1:
							user_email = input("Enter user's email address: ")
							queries.statement_search(user_email, statement_search_choice)
						elif statement_search_choice == 2:
							user_phone = int(input("Enter user's phone number: "))
							queries.statement_search(user_phone, statement_search_choice)
						elif statement_search_choice == 3:
							ttype = input("Enter r - received or s - sent transactions: ")
							queries.statement_search(ttype, statement_search_choice)
						else:
							break
				else:
					break

		elif cred_step == 2:
			user_name = input("Enter your first and last name: ")
			user_ssn = int(input("Enter your SSN: "))
			user_phone = int(input("Enter your phone number: "))
			user_email = input("Enter your email address: ")
			print(queries.user_sign_up(user_name, user_ssn, user_phone, user_email))
			 

if __name__ == '__main__':
    main()
