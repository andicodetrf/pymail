import datetime as dt
import pandas
import random
import smtplib
import cred #credential saved in a diff file/module

now = dt.datetime.now()
today = (now.month, now.day)
data = pandas.read_csv("birthdays.csv")

# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
birthday_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
	my_email = cred.email
	pw = cred.pw
	random_lttr_idx = random.randint(1,3)
	with open(f"letter_templates/letter_{random_lttr_idx}.txt") as file:
		contents = file.read()
		name = birthday_dict[today]["name"]
		recipient_add = birthday_dict[today]["email"]
		output = contents.replace("[NAME]", name)
		print(output)

		message = 'To: {}\r\nSubject: {}\r\n\r\n{}'.format(recipient_add, "Happy Birthday!", output)

		with smtplib.SMTP('smtp.gmail.com') as connection:
			connection.starttls()
			connection.login(user=my_email, password=pw)
			connection.sendmail(my_email, recipient_add, message)

