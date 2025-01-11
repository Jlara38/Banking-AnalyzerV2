import sqlite3

####################################################################################
#
# This function is strictly used to get file name input from the user at the begining of the program and where else a file name 
# May be needed at.
# 
def input_fileName():
    file_name = input("Please insert the filename (current file type supported is .csv's from Chase and their formatting): ")
    print("Is this the correct filename ----> " + file_name)
    answer = input("Yes or No (type in Y or N): ")
    while answer.upper() != "Y":
        file_name = input("Please insert the filename (current file type supported is .csv's from Chase and their formatting): ")
        print("Is this the correct filename ----> " + file_name)
        answer = input("Yes or No (type in Y or N): ")
    
    return file_name


####################################################################################
#
# Main 
#

print("** Welcome to the Banking Analyzer App **")

file_name = input_fileName()

dbConn = sqlite3.connect('bank_information.db')

dbConn.commit()