'''9.Use the Datetime Module: Write a program that imports the datetime module and
uses it to: Get and print the current date and time . Calculate and print the number of
days between two dates. Format and print the current date in the format "DD-MM
YYYY"'''

from datetime import datetime, date
now = datetime.now()
print("Current date and time:", now)
date1 = date(2024, 1, 1)
date2 = date(2024, 12, 31)
diff = date2 - date1
print("Days between dates:", diff.days)
print("Formatted date:", now.strftime("%d-%m-%Y"))