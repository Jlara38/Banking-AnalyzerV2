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
    
    # clear_table_entries
    #
    # This command will simply delete the current database in order to create a new one with the 
    # new csv file data. 
    #
    def clear_table_entries(dbConn):
        dbConn.execute("""DELETE FROM bankinfo""")
        dbConn.commit()