############################################################
# COVID-19 Reminder Bot - SMS_push_notifications.py
############################################################
#
# Author: Andrew Joseph Millward
#
############################################################
# Imports
############################################################

import smtplib

############################################################
# Functions
############################################################

def send_text(message, email, password, number, carrier_address):

	# Recipient address
	recip_add = number+carrier_address

	# Connect to Gmail server at port 587
	connection = smtplib.SMTP( "smtp.gmail.com", 587 )
	connection.starttls()
	connection.login(email, password)

	# Send text message through SMS gateway of destination number
	connection.sendmail( email, recip_add, message )