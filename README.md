# wallet-project
CS631 Data Management System Design Project  
   
# Requirements (Install as Need be) 
- Python 3.7 >= 
- psycopy2 2.8.6
- psql 9.1 >=  
(homebrew: `brew install postgresql`)  
- faker 9.8.2
- prettytable 2.4.0

# Set-Up  
1. `git clone ssh://git@github.com:vkoli/wallet-project.git`
2. Create a new $USER, who also has superuser permissions, in psql and add a $PASSWORD to the $USER
  `psql createuser -P -s -e $USER`
3. Create a database called *wallet*  
  `psql createdb wallet`
4. Create **database.ini** text file and copy paste the following text, substituting values as needed  
  ```  
  [postgresql]  
  host=localhost  
  database=wallet  
  user=$USER
  password=$PASSWORD
  ```
5. Add the database.ini file to the main folder  

# Run the Program
1. Start psql in terminal `sudo service postgresql start`  
    - For homebrew: `brew services start postgresql`
2. Run connect.py program `python connect.py`  
    - You should see the psql version being outputted
3. Log in to psql and check whether wallet database has 8 new tables created 

## Notes
- view db info: `psql -U $USER -d wallet`
