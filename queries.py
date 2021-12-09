#!/usr/bin/python
import sys
import connect
from prettytable import PrettyTable

USER_PK = 0 #Used for table joins and transaction selection per user 

def user_sign_in(ssn, phone):
    USER_PK = ssn

    #TODO replaced with sql query to check for user in db
    print(f'User {ssn} with {phone} has signed in')

def user_sign_up(name, user_ssn, phone, email,verified=1):
    return connect.exec(f"""INSERT INTO ELEC_ADDRESS VALUES('{phone}','{verified}', 'PHONE');\n
                            INSERT INTO EMAIL VALUES('{email}','{user_ssn}');\n
                            INSERT INTO ELEC_ADDRESS VALUES('{email}','{verified}', 'EMAIL');\n
                            INSERT INTO USER_ACCOUNT(SSN, Name, PhoneNo) VALUES('{user_ssn}', '{name}', '{phone}');""")

def account_summary(user_ssn):
    print(connect.select_exec(f"""SELECT *
                                FROM USER_ACCOUNT
                                WHERE SSN='{user_ssn}';\n"""))

def add_new_email(email,user_ssn,verified=1):
    return connect.exec(f"""INSERT INTO ELEC_ADDRESS VALUES('{email}','{verified}', 'EMAIL');\n
                            INSERT INTO EMAIL VALUES('{email}','{user_ssn}');\n""")

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
    if choice==1 or choice==2:
        print(connect.select_exec(f"""SELECT * FROM 
                                (SELECT STid AS Id, Amount, Date_Time, Memo, Identifier 
                                FROM SEND_TRANSACTION 
                                WHERE Identifier='{input}' AND SSN='{USER_PK}' 
                                UNION 
                                SELECT REQUEST_TRANSACTION.RTid AS Id, Amount, Date_Time, Memo, Identifier 
                                FROM REQUEST_TRANSACTION, RT_FROM 
                                WHERE RT_FROM.RTid=REQUEST_TRANSACTION.RTid AND SSN='{USER_PK}' AND Identifier='{input}') Results 
                                ORDER BY Date_Time;\n"""))
    if choice==4:
        if input=='r':
            print(connect.select_exec(f"""SELECT REQUEST_TRANSACTION.RTid, Amount, Date_Time, Memo, Identifier 
                                        FROM REQUEST_TRANSACTION, RT_FROM 
                                        WHERE REQUEST_TRANSACTION.SSN='{USER_PK}' AND RT_FROM.RTid=REQUEST_TRANSACTION.RTid 
                                        ORDER BY Date_Time;\n"""))
        if input=='s':
            print(connect.select_exec(f"""SELECT STid, Amount, Date_Time, Memo, Identifier 
                                FROM SEND_TRANSACTION
                                WHERE SSN='{USER_PK}'
                                ORDER BY Date_Time;\n"""))
