import datatier
import csv
import re

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
    # clean_string()
    #
    # 
    # 
    #
    
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
    # load_data_to_db()
    #
    # load_data_to_db will be primarily used to load the data from the CSV file into the database.
    # each line in the csv will be turned into an entry for our database. 
    # for the entries that require number/decimals they will be converted accordingly. 
    #
    def load_data_to_db(dbConn,filename):
        with open(filename, mode='r') as file:
            csv_file = csv.DictReader(file)
            for lines in csv_file:
                return #Will be changed in the coming future
        dbConn.commit()
        
    
    