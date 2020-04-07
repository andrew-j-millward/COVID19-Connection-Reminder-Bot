############################################################
# COVID-19 Reminder Bot - main.py
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

def refresh():

    # URL of public database
    url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRcVOpz90S0GzA_2qncNfbGZbQIeP136zpMKIIvuDSMcwnSmPZOi5y3hiDyT5F6L7bmh7-OKk2ucgJd/pubhtml"

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
        email_list.append([row_contents[1].text, row_contents[2].text.replace(" ", "").split(",")])

    return email_list