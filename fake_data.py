from faker import Faker
import random
import decimal
from datetime import datetime

fake = Faker()
fake.seed_instance(4321)
sql_file = open("wallet_data.sql","w")
commands = []

entries = 10

BIDs = random.sample(range(1000000000, 9999999999), entries)
BANs = random.sample(range(1000000000, 9999999999), entries)
SSNs = random.sample(range(100000000, 999999999), entries)
PNs = random.sample(range(100000000, 999999999), entries)
RTids = random.sample(range(10000, 99999), entries)
STids = random.sample(range(10000, 99999), entries)


for i in range(entries):
    SSN = SSNs[i]
    BID = BIDs[i]
    BAN = BANs[i]
    name = fake.name()
    PN = PNs[i]
    verified = 1
    balance = float(decimal.Decimal(random.randrange(0, 1000000))/100)
    
    commands.append(f"INSERT INTO BANK_ACCOUNT VALUES('{BID}', '{BAN}');\n")
    commands.append(f"INSERT INTO ELEC_ADDRESS VALUES('{PN}','{verified}');\n")
    commands.append(f"INSERT INTO USER_ACCOUNT VALUES('{SSN}', '{name}', '{PN}', {balance}, '{BID}', '{BAN}', '{verified}');\n")
    
    # send/request transaction:

for i in range(entries):
    if i > 0:
        SSN = SSNs[i]
        amount_send = float(decimal.Decimal(random.randrange(0, 10000))/100)
        amount_request = float(decimal.Decimal(random.randrange(0, 10000))/100)
        commands.append(f"""
            INSERT INTO SEND_TRANSACTION VALUES('{STids[i]}', {amount_send}, '{datetime.now()}', 'Demo',
                'None','{PNs[i-1]}','{SSN}');\n

            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+{amount_send}
            WHERE PhoneNo = '{PNs[i-1]}';\n

            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-{amount_send}
            WHERE SSN = '{SSN}';\n
        """)

        commands.append(f"""
        INSERT INTO REQUEST_TRANSACTION VALUES('{RTids[i]}', {amount_request}, '{datetime.now()}', 'Demo', '{SSN}');\n
        INSERT INTO RT_FROM VALUES('{RTids[i]}','{PNs[i-1]}',1);\n
        """)

        

    
sql_file.writelines(commands)
sql_file.close()