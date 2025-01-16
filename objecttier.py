import datatier
import csv
import re

state_abbreviations = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 
    'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 
    'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 
    'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]
class Statement:
    def __init__(self, D, PD, Desc, Amt, Tp, Bal, CorS):
        self._details = D
        self._posting_date = PD
        self._description = Desc
        self._amount = Amt
        self._type = Tp
        self._balance = Bal
        self._check_or_slip = CorS
        
    @property
    def Details(self):
        return self._details
    
    @property
    def Posting_Date(self):
        return self._posting_date
    
    @property
    def Description(self):
        return self._description
    
    @property
    def Amount(self):
        return self._amount
    
    @property
    def Type(self):
        return self._type
    
    @property
    def Balance(self):
        return self._balance
    
    @property
    def Check_or_Slip(self):
        return self._check_or_slip
    
####################################################################################
# clear_table_entries()
#
# This command will simply delete the current database in order to create a new one with the 
# new csv file data. 
#
def clear_table_entries(dbConn):
    dbConn.execute("""DELETE FROM bankinfo""")
    dbConn.commit()

####################################################################################
# clean_desc()
#
# clean_desc is meant to clean up the description from the CSV file and abbreviate any 
# state that may be icluded in the description. It is an attempt to make the displaying of the 
# description a look nicer whenever we need to display it.
#
def clean_desc(description):
    pattern = r'\b(' + '|'.join(state_abbreviations) + r')\b'
    match = re.search(pattern,description)
    
    if match:
        return description[:match.end()].strip()
    
    return description.strip()

####################################################################################
# num_transac()
#
# num_transac checks the database to see if there are any entries from previous csv's or 
# if anything has been loaded. If nothing exists we return -1 to let the calling function 
# know that the database has entries. Otherwise we return the actual amount of entries. 
#
def num_transac(dbConn):
    sql = """SELECT Count(*)
                From bankinfo"""
    total_transactions = datatier.select_one_row(dbConn, sql)
    
    if total_transactions[0] == 0:
        return -1
    
    return total_transactions

####################################################################################
# check_if_number()
#
# This helper function will just check to make sure that the relevant information is (amount and balance) 
# are not empty ex: " ". That way the information can be added to the database.
# In the case of the amount there will always be one regarding values simply because the bank statement 
# Will show how much you spent or is pending. For balance however we have to write 0.0 in the cases that the bank 
# does not report the actual balance for the account because the transaction had no way to know how much you had in your account
# at the time of purchase.
#
def check_if_number(lines, text):
    if(lines[text] == ' '):
        return 0.0
    else:
        return float(lines[text])
    

####################################################################################
# load_data_to_db()
#
# load_data_to_db will be primarily used to load the data from the CSV file into the database.
# each line in the csv will be turned into an entry for our database. 
# for the entries that require number/decimals they will be converted accordingly. 
#
def load_data_to_db(dbConn,filename):
    t_amt = "Amount"
    t_bal = "Balance"
    with open(filename, mode='r') as file:
        csv_file = csv.DictReader(file)
        for lines in csv_file:
            amount  = check_if_number(lines, t_amt)
            balance = check_if_number(lines, t_bal)
            cleaned_desc = clean_desc(lines["Description"])
            dbConn.execute("""
                                INSERT INTO bankinfo (details, date, description, amount, type, balance, check_or_slip)
                                VALUES (?, ?, ?, ?, ?, ?, ?)""",
                                (lines["Details"], lines["Posting Date"], cleaned_desc, amount, lines["Type"], balance, lines["Check or Slip #"]))
    dbConn.commit()

def find_biggest_purchase(dbConn):
    sql = """SELECT date, description, MAX(amount), type
             FROM bankinfo
             WHERE type NOT IN ('ATM', 'ACCT_XFER', 'ACH_CREDIT')"""
             
    biggest_purchase = datatier.select_n_rows(dbConn, sql)
    
    for purchase in biggest_purchase:
        print(f"Biggest Expenditure --> Date: {purchase[0]} | Description: {purchase[1]} | Amount: ${purchase[2]:,} | Payment Type/Entry Type: {purchase[3]}")
    
def purchases_by_company(dbConn):
    userInput = input("Enter company name/or partial part of the name (You can wrap the name with %name%' for better results)")
    print()
    sql = """SELECT description, Sum(amount)
             FROM bankinfo
             WHERE description LIKE ?
             GROUP BY description"""
             
    companies = datatier.select_n_rows(dbConn, sql, [userInput])
    
    if companies == None:
        print("No company exist by that name in the database")
        return 0
    else:
        for comp in companies:
            print(f"{comp[0]} | ${comp[1]:,.2f}")
