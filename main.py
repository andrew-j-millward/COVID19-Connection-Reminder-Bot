############################################################
# COVID-19 Reminder Bot - main.py
############################################################
#
# Author: Andrew Joseph Millward
#
############################################################
# Imports
############################################################

import email_refresh, points_refresh, smtplib, ssl, datetime, SMS_push_notification
from datetime import datetime

############################################################
# Functions
############################################################


# Refresh list of emails and days to send.
email_list = email_refresh.refresh()

# Table of days with index corresponding to .weekday()
days = ["Mondays", "Tuesdays", "Wednesdays", "Thursdays",
        "Fridays", "Saturdays", "Sundays"]
carrier_dict = {
    'AT&T':    '@mms.att.net',
    'T-Mobile':'@tmomail.net',
    'Verizon':  '@vzwpix.com',
    'Sprint':   '@pm.sprint.com',
    'Xfinity Mobile':   '@mypixmessages.com',
    'Virgin Mobile':   '@vmpix.com',
    'Tracfone':   '@mmst5.tracfone.com',
    'Simple Mobile':   '@smtext.com',
    'Mint Mobile':   '@mailmymobile.net',
    'Red Pocket':   '@vtext.com',
    'Metro PCS':   '@mymetropcs.com',
    'Boost Mobile':   '@myboostmobile.com',
    'Cricket':   '@mms.cricketwireless.net',
    'Republic Wireless':   '@text.republicwireless.com',
    'Google Fi (Project Fi)':   '@msg.fi.google.com',
    'U.S. Cellular':   '@mms.uscc.net',
    'Ting':   '@message.ting.com',
    'Consumer Cellular':   '@mailmymobile.net',
    'C-Spire':   '@cspire1.com',
    'Page Plus':   '@vtext.com'
}

# Retrieve current day
today = datetime.date(datetime.now())
today = today.weekday()
today = days[today]

# Setup secure connection to gmail.
SMPT_SSL_Port = 465 
bot_address = "COVID.Connection.Reminder@gmail.com"
bot_password = "***********************" # Redacted

# SSL Context.
context = ssl.create_default_context()

# Login to server and send emails.
with smtplib.SMTP_SSL("smtp.gmail.com", SMPT_SSL_Port, context=context) as server:
    server.login(bot_address, bot_password)

    # Prevent duplicate emails
    received = []

    # Iterate through all emails signed up
    for email in email_list:
        try:
            if today in email[1] and email[0] not in received:
                received.append(email[0])
                recipient_address = email[0]
                points = str(points_refresh.refresh(recipient_address))
                message = """\
Subject: Daily reminder to contact family and friends
Good Morning, \n\nWe are just contacting you on behalf of the COVID Connections Reminder listserver to remind you to take some time to call or send a message to those you care about today to let them know you're there. We know how stressful times like this can be when distanced from those you care about most, so make sure to stay in touch with them, and we will stay in touch with you.\n\nWhen you finish touching base with everyone, please take some time to fill out the following forum to log your connection in order to earn more points: https://forms.gle/DqXdEeY9WbLFfgd96\n\nCurrently, your point total is: """ + points + """\n\nTake care,\n\n\nThe COVID Connections Reminder Team"""
                server.sendmail(bot_address, recipient_address, message)

                if email[2] == "Yes":
                    txt_msg = "Good morning, this is just a quick reminder to contact your friends and family today to remain close during these hard times! \n\n-The COVID Connections Team"
                    SMS_push_notification.send_text(txt_msg, bot_address, bot_password, email[3].replace("-",""), carrier_dict[email[4]])
        except:
            print("Invalid email address. Continuing...")