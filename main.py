import sqlite3
import objecttier

####################################################################################
# input_fileName()
#
# This function is strictly used to get file name input from the user at the begining
# of the program.
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
# clear_all_entries()
#
# This command will be used to clear all entries in the database in order to make sure that
# if any updates happen from the CSV file then it will properly reflect them once the 
# user puts the CSV file in and types the name in when the program runs. 
#
def clear_all_entries(dbConn):
    print("Clearing all data entries in the database")
    objecttier.clear_table_entries(dbConn)

####################################################################################
# load_database()
#
# load_database() will check if the database has any entries before attempting to load the data from the CSV file.
# Shouls no entries be found it will proceed to make a call to fucntions in the object tier in order to load the data
# into the database. Otherwise it will just let the user know that the database has data and that they should clear the 
# database before reading a new CSV. 
#
def load_database(dbConn, filename):
    number_of_transactions = objecttier.num_transac(dbConn)
    if(number_of_transactions == -1):
        print("Loading data from CSV into the database")
        objecttier.load_data_to_db(dbConn, filename)
    else:
        print("Data exists in database (Use the clear command before trying to load new data into the database.)")
        
####################################################################################
# print_gen_stats()
#
# print_gen_stats will simply print some general stats like the number of entries and 
# the biggest purchase found in your entry. 
def print_gen_stats(dbConn):
    number_of_entries = objecttier.num_transac(dbConn)
    print("The number entires is:",number_of_entries)
    objecttier.find_biggest_purchase(dbConn)
    
def instructions():
    print("Command 1: Will show you the amount spent per year (up to 3 years)")
    print("Command 2: Allows you to search spending by the company of your choosing (using wildcards: _ , %, etc.)")
    print("Command 3: Will clear all database entries")
    print("Command 4: Will allow you to load another file into the database.")
    

####################################################################################
#
# Main 
#
print("** Welcome to the Banking Analyzer App **")
print("*****************************************")

file_name = input_fileName()

dbConn = sqlite3.connect('bank_information.db')

dbConn.commit()

load_database(dbConn, file_name)

print("Here are some general stats: ")

print_gen_stats(dbConn)

instructions()
cmd = input("Please enter a command (1-4, x to exit): ")
print()

while cmd != "x":
    if cmd == "1":
        objecttier.amount_spent_perYear(dbConn)
    elif cmd == "2":
        objecttier.purchases_by_company(dbConn)
    elif cmd == "3":
        objecttier.clear_table_entries(dbConn)
    elif cmd == "4":
        file_name = input_fileName()
        load_database(dbConn,file_name)
        print("Here are some general stats: ")
        print_gen_stats(dbConn)
    else:
        print("**Error, unkown command, try again...")
    
    print()
    instructions()
    cmd = input("Please enter a command (1-4, x to exit): ")
    print()

dbConn.close()
print("Thank you for using this app, hopefully it helped better visualize your spending. ")