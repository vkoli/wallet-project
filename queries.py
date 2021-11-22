#!/usr/bin/python
import sys
import connect

def user_sign_in(ssn, phone):
    #TODO replaced with sql query to check for user in db
    print(f'User {ssn} with {phone} has signed in')

def user_sign_up(name, ssn, phone, email):
    #TODO replaced with sql query to add user in db
	print(f'\nUser {name} identified by {ssn} with phone {phone} and email {email} has signed up.\nPlease sign in to access account.\n')

def account_summary():
    pass

def add_new_email():
    pass

def remove_email():
    pass

def add_new_phone():
    pass

def remove_phone():
    pass

def add_new_bank_acc():
    pass

def remove_bank_acc():
    pass

def send_transaction():
    pass

def request_transaction():
    pass

def statement_users_by_date_range():
    pass

def statement_users_by_month():
    pass

def max_transactions():
    pass

def best_users():
    pass

def statement_search(type='statement'):
    pass

