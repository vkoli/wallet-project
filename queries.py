#!/usr/bin/python
import sys
import connect
from prettytable import PrettyTable

USER_PK = 0

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

def statement_users_by_date_range(user_name, start_date, end_date, ttype):
    if ttype == 's':
        print(connect.select_exec(f"""SELECT USER_ACCOUNT.Name, SUM(AMOUNT) AS Total 
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, SEND_TRANSACTION 
                                    WHERE USER_ACCOUNT.SSN=SEND_TRANSACTION.SSN 
                                        AND USER_ACCOUNT.Name='{user_name}' 
                                        AND SEND_TRANSACTION.Date_Time BETWEEN '{start_date}' AND '{end_date}'\n"""))
    if ttype=='r':
        print(connect.select_exec(f"""SELECT USER_ACCOUNT.NAME, SUM(Amount) AS Total
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, REQUEST_TRANSACTION NATURAL JOIN RT_FROM
                                    WHERE USER_ACCOUNT.Name='{user_name}'
                                    AND REQUEST_TRANSACTION.Date_Time BETWEEN '{start_date}' AND '{end_date}';\n"""))

def statement_users_by_month(user_name, month, ttype):
    if ttype == 's':
        print(connect.select_exec(f"""SELECT USER_ACCOUNT.Name, SUM(AMOUNT) AS Total 
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, SEND_TRANSACTION 
                                    WHERE USER_ACCOUNT.SSN=SEND_TRANSACTION.SSN 
                                        AND USER_ACCOUNT.Name='{user_name}' 
                                        AND EXTRACT(MONTH FROM SEND_TRANSACTION.Date_Time)={month};\n"""))
    if ttype=='r':
        print(connect.select_exec(f"""SELECT USER_ACCOUNT.NAME, SUM(Amount) AS Total
                                    FROM USER_ACCOUNT LEFT JOIN EMAIL ON USER_ACCOUNT.SSN=EMAIL.SSN, REQUEST_TRANSACTION NATURAL JOIN RT_FROM
                                    WHERE USER_ACCOUNT.Name='{user_name}'
                                        AND EXTRACT(MONTH FROM REQUEST_TRANSACTION.Date_Time)={month};\n"""))

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
