# This file is solely gonna be used to create a database that will contain 
# The data for the rest of the program. (Will most likely be removed at the 
# Once im done coding the rest of the program.)

import sqlite3

connection = sqlite3.connect('bank_information.db')

cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS bankinfo(
                  details Text,
                  date Text,
                  description Text,
                  amount Integer,
                  type Text,
                  balance Integer,
                  check_or_slip Text
                  )
                  """)

print("Command Executed Succesfully..")

connection.commit()

connection.close()

