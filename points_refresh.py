############################################################
# COVID-19 Reminder Bot - points_refresh.py
############################################################
#
# Author: Andrew Joseph Millward
#
############################################################
# Imports
############################################################

import requests
from bs4 import BeautifulSoup

############################################################
# Functions
############################################################

def refresh(address):

    # URL of public database
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT2wHHVNNwJpsnP6UEzxdEScufsG_EcMwbhlywGaFTt7_pnCSvKt47k2Rx73cfCitXmqDdJM3HailE9/pubhtml"

    # Create a request to the google database and store the HTML
    request = requests.get(url)
    data = request.text
    soup = BeautifulSoup(data, "html.parser")

    # Find the HTML table tag and isolate those features
    table = soup.findAll("table")[0]

    # Grab email addresses and a list of days for contact. Format the text and add to tuple.
    rows = table.tbody.findAll("tr")
    email_list = []
    for i in range(len(rows)-2):
        row_contents = rows[i+2].findAll("td")
        email_list.append([row_contents[1].text, row_contents[2].text])

    # Initial count value.
    count = 0

    # For every instance of the email responding yes, add one to the count.
    for email in email_list:
        if email[0] == address and email[1] == "Yes":
            count += 1

    # Return total point count.
    return count