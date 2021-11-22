#!/usr/bin/python
import sys
import connect

def user_sign_in(ssn, phone):
    #TODO replaced with sql query to check for user in db
    print(f'User {ssn} with {phone} has signed in')

def user_sign_up(name, ssn, phone, email):
    #TODO replaced with sql query to add user in db
	print(f'\nUser {name} identified by {ssn} with phone {phone} and email {email} has signed up.\nPlease sign in to access account.\n')