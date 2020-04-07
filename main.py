############################################################
# COVID-19 Reminder Bot - main.py
############################################################
#
# Author: Andrew Joseph Millward
#
############################################################
# Imports
############################################################

import email_refresh, smtplib, ssl

############################################################
# Functions
############################################################

if __name__ == "__main__":

	# Refresh list of emails and days to send.
	email_list = email_refresh.refresh()

	# Setup secure connection to gmail.
	SMPT_SSL_Port = 465 
	bot_address = "COVID.Connection.Reminder@gmail.com"
	bot_password = "*****************" # Redacted

	# SSL Context.
	context = ssl.create_default_context()

	# Login to server and send emails.
	with smtplib.SMTP_SSL("smtp.gmail.com", SMPT_SSL_Port, context=context) as server:
	    server.login(bot_address, bot_password)
	    for email in email_list:
	    	reminder_address = email[0]
	    	message = """Good Afternoon, \n\nThis is a reminder to contact your loved ones today.\n\nSincerely,\n\n\nAndrew Millward"""
	    	server.sendmail(bot_address, reminder_address, message)