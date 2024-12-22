from datetime import datetime

input_date = input("Please enter a date in format: DD-MM-YEAR\n")
current_year = datetime.now().year

input_split = input_date.split('-')
print(current_year - int(input_split[2]))
