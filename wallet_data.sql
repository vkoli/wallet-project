INSERT INTO BANK_ACCOUNT VALUES('3441971410', '4044629434');
INSERT INTO ELEC_ADDRESS VALUES('707765583','1');
INSERT INTO USER_ACCOUNT VALUES('924777485', 'Jason Brown', '707765583', 8771.46, '3441971410', '4044629434', '1');
INSERT INTO BANK_ACCOUNT VALUES('1532451141', '8773187304');
INSERT INTO ELEC_ADDRESS VALUES('353592186','1');
INSERT INTO USER_ACCOUNT VALUES('920202377', 'Jacob Stein', '353592186', 7570.3, '1532451141', '8773187304', '1');
INSERT INTO BANK_ACCOUNT VALUES('8169489429', '3962319211');
INSERT INTO ELEC_ADDRESS VALUES('860998842','1');
INSERT INTO USER_ACCOUNT VALUES('107197584', 'Cody Brown', '860998842', 4868.61, '8169489429', '3962319211', '1');
INSERT INTO BANK_ACCOUNT VALUES('1857129745', '8587951712');
INSERT INTO ELEC_ADDRESS VALUES('351880454','1');
INSERT INTO USER_ACCOUNT VALUES('825768551', 'Larry Morales', '351880454', 1891.8, '1857129745', '8587951712', '1');
INSERT INTO BANK_ACCOUNT VALUES('5706017780', '1414647991');
INSERT INTO ELEC_ADDRESS VALUES('276538350','1');
INSERT INTO USER_ACCOUNT VALUES('833225780', 'Jessica Hendricks', '276538350', 4264.13, '5706017780', '1414647991', '1');
INSERT INTO BANK_ACCOUNT VALUES('1571370239', '1707380266');
INSERT INTO ELEC_ADDRESS VALUES('802505896','1');
INSERT INTO USER_ACCOUNT VALUES('360547341', 'Brian Moore', '802505896', 2733.41, '1571370239', '1707380266', '1');
INSERT INTO BANK_ACCOUNT VALUES('7266770787', '7590598733');
INSERT INTO ELEC_ADDRESS VALUES('549733498','1');
INSERT INTO USER_ACCOUNT VALUES('207270980', 'Scott Baker', '549733498', 3163.53, '7266770787', '7590598733', '1');
INSERT INTO BANK_ACCOUNT VALUES('7555985102', '6879588003');
INSERT INTO ELEC_ADDRESS VALUES('832375157','1');
INSERT INTO USER_ACCOUNT VALUES('609461418', 'Ruth Hoffman', '832375157', 4538.32, '7555985102', '6879588003', '1');
INSERT INTO BANK_ACCOUNT VALUES('6398958536', '4702637178');
INSERT INTO ELEC_ADDRESS VALUES('385281301','1');
INSERT INTO USER_ACCOUNT VALUES('790095205', 'Daniel George', '385281301', 5320.34, '6398958536', '4702637178', '1');
INSERT INTO BANK_ACCOUNT VALUES('9940441207', '5231640055');
INSERT INTO ELEC_ADDRESS VALUES('543211407','1');
INSERT INTO USER_ACCOUNT VALUES('349049296', 'David Moody', '543211407', 2748.08, '9940441207', '5231640055', '1');

            INSERT INTO SEND_TRANSACTION VALUES('78946', 56.32, '2021-12-12 23:25:28.206314', 'Demo',
                'None','707765583','920202377');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+56.32
            WHERE PhoneNo = '707765583';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-56.32
            WHERE SSN = '920202377';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('26971', 10.83, '2021-12-12 23:25:28.206326', 'Demo', '920202377');

        INSERT INTO RT_FROM VALUES('26971','707765583',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('36533', 47.54, '2021-12-12 23:25:28.206331', 'Demo',
                'None','353592186','107197584');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+47.54
            WHERE PhoneNo = '353592186';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-47.54
            WHERE SSN = '107197584';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('64688', 7.0, '2021-12-12 23:25:28.206333', 'Demo', '107197584');

        INSERT INTO RT_FROM VALUES('64688','353592186',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('50270', 89.6, '2021-12-12 23:25:28.206337', 'Demo',
                'None','860998842','825768551');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+89.6
            WHERE PhoneNo = '860998842';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-89.6
            WHERE SSN = '825768551';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('62477', 31.47, '2021-12-12 23:25:28.206339', 'Demo', '825768551');

        INSERT INTO RT_FROM VALUES('62477','860998842',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('67817', 7.76, '2021-12-12 23:25:28.206343', 'Demo',
                'None','351880454','833225780');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+7.76
            WHERE PhoneNo = '351880454';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-7.76
            WHERE SSN = '833225780';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('94198', 21.15, '2021-12-12 23:25:28.206345', 'Demo', '833225780');

        INSERT INTO RT_FROM VALUES('94198','351880454',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('68079', 88.3, '2021-12-12 23:25:28.206348', 'Demo',
                'None','276538350','360547341');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+88.3
            WHERE PhoneNo = '276538350';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-88.3
            WHERE SSN = '360547341';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('53736', 85.56, '2021-12-12 23:25:28.206350', 'Demo', '360547341');

        INSERT INTO RT_FROM VALUES('53736','276538350',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('64813', 64.59, '2021-12-12 23:25:28.206353', 'Demo',
                'None','802505896','207270980');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+64.59
            WHERE PhoneNo = '802505896';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-64.59
            WHERE SSN = '207270980';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('34941', 78.54, '2021-12-12 23:25:28.206355', 'Demo', '207270980');

        INSERT INTO RT_FROM VALUES('34941','802505896',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('78776', 45.21, '2021-12-12 23:25:28.206358', 'Demo',
                'None','549733498','609461418');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+45.21
            WHERE PhoneNo = '549733498';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-45.21
            WHERE SSN = '609461418';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('12350', 67.42, '2021-12-12 23:25:28.206360', 'Demo', '609461418');

        INSERT INTO RT_FROM VALUES('12350','549733498',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('83875', 31.72, '2021-12-12 23:25:28.206364', 'Demo',
                'None','832375157','790095205');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+31.72
            WHERE PhoneNo = '832375157';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-31.72
            WHERE SSN = '790095205';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('91539', 1.12, '2021-12-12 23:25:28.206366', 'Demo', '790095205');

        INSERT INTO RT_FROM VALUES('91539','832375157',1);

        
            INSERT INTO SEND_TRANSACTION VALUES('62074', 70.71, '2021-12-12 23:25:28.206369', 'Demo',
                'None','385281301','349049296');


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE+70.71
            WHERE PhoneNo = '385281301';


            UPDATE USER_ACCOUNT
            SET BALANCE = BALANCE-70.71
            WHERE SSN = '349049296';

        
        INSERT INTO REQUEST_TRANSACTION VALUES('43834', 96.9, '2021-12-12 23:25:28.206371', 'Demo', '349049296');

        INSERT INTO RT_FROM VALUES('43834','385281301',1);

        