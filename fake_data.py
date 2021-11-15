from faker import Faker
import random
import decimal

fake = Faker()
fake.seed_instance(4321)
sql_file = open("wallet_data.sql","w")
commands = []

entries = 10

BIDs = random.sample(range(1000000000, 9999999999), entries)
BANs = random.sample(range(1000000000, 9999999999), entries)
SSNs = random.sample(range(100000000, 999999999), entries)
PNs = random.sample(range(100000000, 999999999), entries)


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
    
sql_file.writelines(commands)
sql_file.close()