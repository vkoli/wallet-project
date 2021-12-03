#!/usr/bin/python
import sys
import connect

USER_PK = 0 #Used for table joins and transaction selection per user 

def user_sign_in(ssn, phone):
    USER_PK = ssn

    #TODO replaced with sql query to check for user in db
    print(f'User {ssn} with {phone} has signed in')

def user_sign_up(name, ssn, phone, email,verified=1):
    return connect.exec(f"""INSERT INTO ELEC_ADDRESS VALUES('{phone}','{verified}', 'PHONE');\n
                            INSERT INTO ELEC_ADDRESS VALUES('{email}','{verified}', 'EMAIL');\n
                            INSERT INTO USER_ACCOUNT(SSN, Name, PhoneNo) VALUES('{ssn}', '{name}', '{phone}');""")

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

def statement_search(input, choice, type='statement'):
    if choice==2 or choice==3:
        return connect.exec(f"""SELECT * FROM(SELECT * FROM send_transaction WHERE Identifier='{input}' AND SSN={USER_PK} UNION SELECT * FROM request_transactions, rt_from WHERE rt_from.RTid=request_transaction.RTid AND SSN={USER_PK} AND Identifier='{input}') Results ORDERBY Date_Time;\n""")
    if choice==4:
        if input=='r':
            return connect.exec(f"""SELECT * FROM ORDERBY Date_Time;\n""")
        if input=='s':
            return connect.exec(f"""SELECT * FROM ORDERBY Date_Time;\n""")

