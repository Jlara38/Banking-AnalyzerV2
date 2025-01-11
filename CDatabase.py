# This file is solely gonna be used to create a database that will contain 
# The data for the rest of the program. (Will most likely be removed at the 
# Once im done coding the rest of the program.)

import sqlite3



connection = sqlite3.connect('bank_information.db')

cursor = connection.cursor()

# If testing values and want to remake the database just uncomment this line to delete it and 
# Create the new table. 
# cursor.execute("""DELETE FROM bankinfo""")

cursor.execute("""CREATE TABLE IF NOT EXISTS bankinfo(
                  details Text,
                  posting_date Text,
                  description Text,
                  amount Integer,
                  payment_type Text,
                  balance Integer,
                  check_or_slip Text
                  )
                  """)

# This is just an example insert of data to make sure that the database is indeed 
# Being created and allowing data to be added. 
cursor.execute("""INSERT INTO bankinfo VALUES (
                'DEBIT',
                '07/12/2023',
                'Zelle payment to Hermano',
                '-13.00',
                'QUICKPAY_DEBIT',
                '218.78',
                'n/a'
                )"""
              )

print("Command Executed Succesfully..")

connection.commit()

connection.close()

